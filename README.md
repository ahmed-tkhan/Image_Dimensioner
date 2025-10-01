# Image Dimensioner

A standalone Python application for measuring dimensions on diagrams and images. This tool enables users to calibrate images using a known distance and then accurately measure any distance by converting pixel values into real-world units.

## Features

- **Load Images**: Support for multiple image formats (PNG, JPG, JPEG, BMP, GIF)
- **Calibration Mode**: Set a scale reference by clicking two points on a known distance
- **Measurement Mode**: Measure any distance on the calibrated image
- **Interactive Canvas**: Visual feedback with point markers and lines
- **Scrollable View**: Navigate large images with scrollbars
- **User-Friendly Interface**: Simple menu-driven interface with clear instructions

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install -r requirements.txt
```

The only external dependency is Pillow (PIL) for image processing. Tkinter comes bundled with Python.

## Usage

### Running the Application

```bash
python image_dimensioner.py
```

Or make it executable (Linux/Mac):

```bash
chmod +x image_dimensioner.py
./image_dimensioner.py
```

### Step-by-Step Guide

#### 1. Load an Image

1. Click **File** → **Open Image**
2. Select an image file (PNG, JPG, JPEG, BMP, or GIF)
3. The image will be displayed on the canvas

#### 2. Calibration

1. Select **Mode** → **Calibration**
2. Click two points on the image that represent a known distance
   - For example, a ruler, a scale bar, or any object with known dimensions
3. Enter the actual physical distance between these points when prompted
4. The application will calculate and store the calibration factor

**Tip**: Use a longer reference distance for better accuracy.

#### 3. Measurement

1. Select **Mode** → **Measurement**
2. Click two points on the image to measure the distance between them
3. The real-world distance will be displayed in a dialog box
4. Repeat as needed - the calibration remains active

#### 4. Tips

- You can recalibrate at any time by switching back to Calibration mode
- The status bar at the bottom shows the current mode and recent measurements
- Use the scrollbars to navigate large images
- Red circles mark your selected points
- Blue lines show the measured distance

## Menu Reference

### File Menu
- **Open Image**: Load an image file
- **Exit**: Close the application

### Mode Menu
- **Calibration**: Switch to calibration mode to set the scale reference
- **Measurement**: Switch to measurement mode to measure distances

### Help Menu
- **Instructions**: Display usage instructions
- **About**: Display application information

## Example Use Cases

- **Engineering Diagrams**: Measure dimensions from technical drawings
- **Floor Plans**: Determine distances and room sizes from architectural plans
- **Maps**: Calculate real-world distances from map images
- **Scientific Images**: Measure features in microscopy or other scientific imaging
- **Construction**: Verify measurements from photos or sketches

## Technical Details

- **Language**: Python 3
- **GUI Framework**: Tkinter (standard library)
- **Image Processing**: Pillow (PIL)
- **Distance Calculation**: Euclidean distance formula
- **Calibration**: Linear scaling factor (units per pixel)

## Future Enhancements

- Measurement history and logging
- Multiple unit support (cm, inches, meters, etc.)
- Zoom and pan functionality
- Export measurements to CSV or text file
- Multi-point and angle measurements
- Enhanced UI with PyQt or Kivy

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
