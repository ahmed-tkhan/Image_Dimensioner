#!/usr/bin/env python3
"""
Image Dimensioner - A standalone application for measuring dimensions on diagrams.

This application allows users to:
1. Load images (PNG, JPG, JPEG, BMP, GIF)
2. Calibrate measurements using a known distance
3. Measure distances on the image using the calibrated scale
"""

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
from PIL import Image, ImageTk
import math
from datetime import datetime


class ImageDimensioner:
    """Main application class for the Image Dimensioner tool."""
    
    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.root.title("Image Dimensioner")
        self.root.geometry("1000x700")
        
        # Application state
        self.image = None
        self.photo = None
        self.canvas_image = None
        self.mode = "calibration"  # "calibration" or "measurement"
        self.points = []
        self.calibration_factor = None
        self.unit = "mm"
        self.zoom_factor = 1.0
        
        # Available units
        self.available_units = ["mm", "cm", "m", "inches", "feet"]
        
        # Measurement logs
        self.measurement_logs = []
        
        # Canvas items for visual feedback
        self.lines = []
        self.point_markers = []
        
        # Create UI
        self.create_menu()
        self.create_controls()
        self.create_canvas()
        self.create_logs_console()
        self.create_status_bar()
        
    def create_menu(self):
        """Create the application menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Image", command=self.load_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Mode menu
        mode_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Mode", menu=mode_menu)
        mode_menu.add_command(label="Calibration", command=self.set_calibration_mode)
        mode_menu.add_command(label="Measurement", command=self.set_measurement_mode)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Instructions", command=self.show_instructions)
        
    def create_controls(self):
        """Create the controls panel."""
        controls_frame = tk.Frame(self.root)
        controls_frame.pack(fill=tk.X, padx=5, pady=2)
        
        # Unit selection
        tk.Label(controls_frame, text="Units:").pack(side=tk.LEFT, padx=(0, 5))
        self.unit_var = tk.StringVar(value=self.unit)
        unit_combo = ttk.Combobox(
            controls_frame, 
            textvariable=self.unit_var, 
            values=self.available_units,
            state="readonly",
            width=8
        )
        unit_combo.pack(side=tk.LEFT, padx=(0, 10))
        unit_combo.bind("<<ComboboxSelected>>", self.on_unit_changed)
        
        # Clear logs button
        clear_btn = tk.Button(
            controls_frame, 
            text="Clear Logs", 
            command=self.clear_logs,
            bg="#ff6b6b",
            fg="white"
        )
        clear_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
    def create_canvas(self):
        """Create the canvas for displaying images."""
        # Create frame for canvas and scrollbars
        canvas_frame = tk.Frame(self.root)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create scrollbars
        v_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL)
        h_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL)
        
        # Create canvas
        self.canvas = tk.Canvas(
            canvas_frame,
            bg="gray",
            yscrollcommand=v_scrollbar.set,
            xscrollcommand=h_scrollbar.set
        )
        
        v_scrollbar.config(command=self.canvas.yview)
        h_scrollbar.config(command=self.canvas.xview)
        
        # Pack widgets
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Bind mouse click event
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        
        # Bind scroll and zoom events
        self.canvas.bind("<Control-MouseWheel>", self.on_zoom)
        self.canvas.bind("<MouseWheel>", self.on_vertical_scroll)
        self.canvas.bind("<Shift-MouseWheel>", self.on_horizontal_scroll)
        
        # Make canvas focusable for key events
        self.canvas.focus_set()
        
    def create_logs_console(self):
        """Create the measurement logs console at the bottom."""
        logs_frame = tk.Frame(self.root)
        logs_frame.pack(fill=tk.BOTH, expand=False, padx=5, pady=(0, 5))
        
        # Console label
        tk.Label(logs_frame, text="Measurement Logs:", font=("Arial", 9, "bold")).pack(anchor=tk.W)
        
        # Create text widget with scrollbar
        logs_container = tk.Frame(logs_frame)
        logs_container.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar for logs
        logs_scrollbar = tk.Scrollbar(logs_container)
        logs_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Text widget for logs
        self.logs_text = tk.Text(
            logs_container,
            height=6,
            wrap=tk.WORD,
            yscrollcommand=logs_scrollbar.set,
            font=("Consolas", 9),
            bg="#f8f9fa",
            fg="#333"
        )
        self.logs_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        logs_scrollbar.config(command=self.logs_text.yview)
        
        # Make logs read-only
        self.logs_text.config(state=tk.DISABLED)
        
    def create_status_bar(self):
        """Create the status bar at the bottom."""
        self.status_bar = tk.Label(
            self.root,
            text="Load an image to begin",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def update_status(self, message):
        """Update the status bar message."""
        self.status_bar.config(text=message)
        
    def on_unit_changed(self, event=None):
        """Handle unit selection change."""
        self.unit = self.unit_var.get()
        # Reset calibration when unit changes
        self.calibration_factor = None
        self.add_log(f"Unit changed to {self.unit}. Please recalibrate.")
        self.update_status(f"Unit changed to {self.unit}. Calibration reset - please recalibrate.")
        
    def on_zoom(self, event):
        """Handle Ctrl+scroll zoom."""
        if not self.image:
            return
            
        # Calculate zoom factor
        zoom_in = event.delta > 0
        zoom_factor = 1.1 if zoom_in else 0.9
        self.zoom_factor *= zoom_factor
        
        # Limit zoom range
        self.zoom_factor = max(0.1, min(5.0, self.zoom_factor))
        
        # Resize and redisplay image
        self.display_image()
        
    def on_vertical_scroll(self, event):
        """Handle vertical scrolling."""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        
    def on_horizontal_scroll(self, event):
        """Handle Shift+scroll horizontal scrolling."""
        self.canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")
        
    def add_log(self, message):
        """Add a message to the logs console."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.logs_text.config(state=tk.NORMAL)
        self.logs_text.insert(tk.END, log_entry)
        self.logs_text.see(tk.END)
        self.logs_text.config(state=tk.DISABLED)
        
        # Store in logs list
        self.measurement_logs.append({"timestamp": timestamp, "message": message})
        
    def clear_logs(self):
        """Clear the measurement logs."""
        self.logs_text.config(state=tk.NORMAL)
        self.logs_text.delete(1.0, tk.END)
        self.logs_text.config(state=tk.DISABLED)
        self.measurement_logs.clear()
        self.add_log("Logs cleared")
        
    def load_image(self):
        """Load an image file."""
        file_types = [
            ("All Supported Formats", "*.png *.jpg *.jpeg *.bmp *.gif"),
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg *.jpeg"),
            ("BMP files", "*.bmp"),
            ("GIF files", "*.gif"),
            ("All files", "*.*")
        ]
        
        file_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=file_types
        )
        
        if file_path:
            try:
                self.image = Image.open(file_path)
                self.zoom_factor = 1.0  # Reset zoom when loading new image
                self.display_image()
                self.reset_points()
                filename = file_path.split("/")[-1].split("\\")[-1]  # Get just filename
                self.add_log(f"Image loaded: {filename}")
                self.update_status(f"Image loaded: {file_path} | Mode: {self.mode.capitalize()}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
                
    def display_image(self):
        """Display the loaded image on the canvas with current zoom."""
        if self.image:
            # Calculate new size based on zoom
            original_size = self.image.size
            new_size = (
                int(original_size[0] * self.zoom_factor),
                int(original_size[1] * self.zoom_factor)
            )
            
            # Resize image for display
            display_image = self.image.resize(new_size, Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            self.photo = ImageTk.PhotoImage(display_image)
            
            # Clear canvas
            self.canvas.delete("all")
            
            # Display image
            self.canvas_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            
            # Configure scroll region
            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
            
    def set_calibration_mode(self):
        """Switch to calibration mode."""
        self.mode = "calibration"
        self.reset_points()
        self.add_log("Switched to Calibration mode")
        self.update_status(f"Calibration mode: Click two points on a known distance")
        
    def set_measurement_mode(self):
        """Switch to measurement mode."""
        if self.calibration_factor is None:
            messagebox.showwarning(
                "No Calibration",
                "Please calibrate the image first in Calibration mode."
            )
            self.set_calibration_mode()
            return
            
        self.mode = "measurement"
        self.reset_points()
        self.add_log("Switched to Measurement mode")
        self.update_status(f"Measurement mode: Click two points to measure distance")
        
    def reset_points(self):
        """Reset the selected points and visual markers."""
        self.points = []
        
        # Clear visual markers
        for marker in self.point_markers:
            self.canvas.delete(marker)
        self.point_markers = []
        
        for line in self.lines:
            self.canvas.delete(line)
        self.lines = []
        
    def on_canvas_click(self, event):
        """Handle canvas click events."""
        if not self.image:
            messagebox.showwarning("No Image", "Please load an image first.")
            return
            
        # Get canvas coordinates
        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)
        
        # Convert to original image coordinates (accounting for zoom)
        original_x = canvas_x / self.zoom_factor
        original_y = canvas_y / self.zoom_factor
        
        # Add point (store original coordinates for calculations)
        self.points.append((original_x, original_y))
        
        # Draw point marker at canvas coordinates
        marker = self.draw_point(canvas_x, canvas_y)
        self.point_markers.append(marker)
        
        # Update status
        if self.mode == "calibration":
            self.update_status(f"Calibration: Point {len(self.points)} of 2 selected")
        else:
            self.update_status(f"Measurement: Point {len(self.points)} of 2 selected")
        
        # Process when we have two points
        if len(self.points) == 2:
            # Draw line using canvas coordinates (zoomed)
            canvas_point1 = (self.points[0][0] * self.zoom_factor, self.points[0][1] * self.zoom_factor)
            canvas_point2 = (self.points[1][0] * self.zoom_factor, self.points[1][1] * self.zoom_factor)
            self.draw_line(canvas_point1, canvas_point2)
            
            if self.mode == "calibration":
                self.calibrate()
            else:
                self.measure()
                
    def draw_point(self, x, y, radius=5):
        """Draw a point marker on the canvas."""
        return self.canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            fill="red",
            outline="white",
            width=2
        )
        
    def draw_line(self, point1, point2):
        """Draw a line between two points."""
        line = self.canvas.create_line(
            point1[0], point1[1],
            point2[0], point2[1],
            fill="blue",
            width=2
        )
        self.lines.append(line)
        
    def calculate_distance(self, point1, point2):
        """Calculate pixel distance between two points."""
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        return math.sqrt(dx * dx + dy * dy)
        
    def calibrate(self):
        """Perform calibration using two selected points."""
        pixel_distance = self.calculate_distance(self.points[0], self.points[1])
        
        if pixel_distance < 1:
            messagebox.showerror("Error", "Points are too close together.")
            self.reset_points()
            return
            
        # Ask user for known distance
        known_distance = simpledialog.askfloat(
            "Calibration",
            f"Enter the actual distance between the two points (in {self.unit}):",
            minvalue=0.001
        )
        
        if known_distance is None or known_distance <= 0:
            messagebox.showerror("Error", "Invalid distance entered.")
            self.reset_points()
            return
            
        # Calculate calibration factor (units per pixel)
        self.calibration_factor = known_distance / pixel_distance
        
        # Log calibration
        self.add_log(f"Calibration: {pixel_distance:.2f}px = {known_distance:.2f} {self.unit} | Scale: {self.calibration_factor:.6f} {self.unit}/px")
        
        messagebox.showinfo(
            "Calibration Complete",
            f"Calibration successful!\n"
            f"Pixel distance: {pixel_distance:.2f} pixels\n"
            f"Known distance: {known_distance:.2f} {self.unit}\n"
            f"Scale: {self.calibration_factor:.6f} {self.unit}/pixel"
        )
        
        self.update_status(
            f"Calibration complete: {self.calibration_factor:.6f} {self.unit}/pixel | "
            f"Switch to Measurement mode to measure distances"
        )
        
        self.reset_points()
        
    def measure(self):
        """Measure distance between two selected points."""
        if self.calibration_factor is None:
            messagebox.showerror("Error", "Calibration required first.")
            self.reset_points()
            return
            
        pixel_distance = self.calculate_distance(self.points[0], self.points[1])
        real_distance = pixel_distance * self.calibration_factor
        
        # Log measurement
        self.add_log(f"Measured: {real_distance:.4f} {self.unit} ({pixel_distance:.2f}px)")
        
        messagebox.showinfo(
            "Measurement Result",
            f"Pixel distance: {pixel_distance:.2f} pixels\n"
            f"Real distance: {real_distance:.4f} {self.unit}"
        )
        
        self.update_status(
            f"Measured: {real_distance:.4f} {self.unit} ({pixel_distance:.2f} pixels)"
        )
        
        self.reset_points()
        
    def show_about(self):
        """Show about dialog."""
        messagebox.showinfo(
            "About Image Dimensioner",
            "Image Dimensioner v2.0\n\n"
            "A standalone application for measuring dimensions on diagrams.\n\n"
            "Features:\n"
            "- Load various image formats\n"
            "- Unit selection (mm, cm, m, inches, feet)\n"
            "- Zoom with Ctrl+scroll\n"
            "- Measurement logging\n"
            "- Calibrate using known distances\n"
            "- Measure real-world dimensions\n\n"
            "Built with Python, Tkinter, and Pillow"
        )
        
    def show_instructions(self):
        """Show instructions dialog."""
        instructions = (
            "How to Use Image Dimensioner:\n\n"
            "1. LOAD IMAGE:\n"
            "   - Use File > Open Image to select an image\n"
            "   - Supported formats: PNG, JPG, JPEG, BMP, GIF\n\n"
            "2. SELECT UNITS:\n"
            "   - Choose your preferred unit from the dropdown\n"
            "   - Default is mm (millimeters)\n\n"
            "3. CALIBRATION:\n"
            "   - Select Mode > Calibration\n"
            "   - Click two points on a known distance in the image\n"
            "   - Enter the actual physical distance when prompted\n"
            "   - The calibration factor will be calculated\n\n"
            "4. MEASUREMENT:\n"
            "   - Select Mode > Measurement\n"
            "   - Click two points to measure\n"
            "   - The real-world distance will be displayed\n"
            "   - All measurements are logged at the bottom\n\n"
            "Navigation:\n"
            "- Ctrl+scroll: Zoom in/out\n"
            "- Scroll: Move up/down\n"
            "- Shift+scroll: Move left/right\n\n"
            "Tips:\n"
            "- Calibrate with a longer reference distance for better accuracy\n"
            "- You can recalibrate at any time\n"
            "- Clear logs with the 'Clear Logs' button"
        )
        messagebox.showinfo("Instructions", instructions)


def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = ImageDimensioner(root)
    root.mainloop()


if __name__ == "__main__":
    main()