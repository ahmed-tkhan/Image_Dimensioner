# Image Dimensioner

A precision measurement tool for digital images and technical diagrams. Transform pixel measurements into real-world dimensions with professional-grade accuracy.

## Overview

Image Dimensioner is a desktop application built for engineers, designers, and researchers who need to extract accurate measurements from digital images. Using a simple calibration process, the tool converts pixel distances to physical measurements in your preferred units.

## Key Features

**🎯 Precision Measurement**
- Sub-pixel accuracy using advanced coordinate interpolation
- Support for multiple measurement units (mm, cm, m, inches, feet)
- Real-time calculation with immediate visual feedback

**🔧 Professional Tools**
- Interactive zoom with mouse wheel control (Ctrl+scroll)
- Pan navigation (scroll: vertical, Shift+scroll: horizontal)
- Comprehensive measurement logging with timestamps
- Visual point markers and measurement lines

**📊 Data Management**
- Persistent measurement history
- Exportable measurement logs
- Session-based calibration settings

**💻 User Experience**
- Native desktop application (no browser required)
- Intuitive point-and-click interface
- Responsive canvas with smooth scrolling
- Professional visual design

## Technical Specifications

- **Language**: Python 3.6+
- **GUI Framework**: Tkinter (cross-platform)
- **Image Processing**: Pillow (PIL)
- **Supported Formats**: PNG, JPG, JPEG, BMP, GIF
- **Platforms**: Windows, macOS, Linux

## Quick Start

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python image_dimensioner.py
```

### Basic Workflow
1. **Load Image**: Import your technical drawing or photograph
2. **Calibrate**: Click two points on a known distance, enter the actual measurement
3. **Measure**: Click any two points to get real-world dimensions

## Application Architecture

The application follows a clean MVC pattern with separated concerns:

- **Model**: Calculation engine for coordinate geometry and unit conversion
- **View**: Tkinter-based responsive interface with custom widgets  
- **Controller**: Event handling for mouse interactions and menu operations

Key algorithmic components:
- Euclidean distance calculation with floating-point precision
- Scale factor calibration using linear transformation
- Zoom-aware coordinate mapping for accurate measurements

## Build & Distribution

The project includes automated build configuration for standalone distribution:

```bash
# Create executable
pyinstaller image_dimensioner.spec

# Output: dist/ImageDimensioner.exe
```

Features custom application icon and optimized packaging for professional deployment.

## Use Cases

- **Mechanical Engineering**: Measure component dimensions from technical drawings
- **Architecture**: Extract measurements from floor plans and blueprints  
- **Research**: Quantify specimen dimensions in microscopy images
- **Quality Control**: Verify product dimensions from photographs
- **Education**: Demonstrate measurement concepts in STEM curricula

## Development

Built with modern Python development practices:
- Modular code architecture
- Comprehensive error handling
- Unit test coverage for core calculations
- Professional documentation standards

---

*Developed by Ahmed Khan | [GitHub](https://github.com/ahmed-tkhan/Image_Dimensioner)*

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
