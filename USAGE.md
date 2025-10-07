# User Guide

## Quick Start

### Launch Application
- **Desktop**: Double-click `ImageDimensioner.exe`
- **Python**: Run `python image_dimensioner.py`

### Workflow
1. **Load Image** → File → Open Image
2. **Select Units** → Choose preferred measurement units from dropdown
3. **Calibrate** → Mode → Calibration → Click two points on known distance → Enter actual measurement
4. **Measure** → Mode → Measurement → Click any two points for real-world distance

## Interface Controls

### Navigation
- **Zoom**: Ctrl + Mouse Wheel
- **Vertical Pan**: Mouse Wheel  
- **Horizontal Pan**: Shift + Mouse Wheel

### Measurement Units
- Millimeters (mm) - *default*
- Centimeters (cm)
- Meters (m)
- Inches (in)
- Feet (ft)

### Measurement Log
- Real-time measurement history
- Timestamp for each measurement
- Clear log function available

## Best Practices

### Calibration Tips
- Use the longest known distance available for better accuracy
- Ensure calibration points are clearly visible and well-defined
- Recalibrate when switching between different images or scales

### Measurement Accuracy
- Zoom in for precise point selection
- Use consistent point selection (e.g., center of features)
- Take multiple measurements for critical dimensions

### File Formats
Supported: PNG, JPG, JPEG, BMP, GIF

---

*For technical support, visit the [GitHub repository](https://github.com/ahmed-tkhan/Image_Dimensioner)*

**Supported Formats**: PNG, JPG, JPEG, BMP, GIF

**Steps**:
1. Click **File** in the menu bar
2. Select **Open Image**
3. Navigate to your image file
4. Click **Open**

The image will be displayed on the canvas with scrollbars if needed.

### 2. Calibration Mode

Calibration establishes the scale by relating pixel distances to real-world measurements.

**Steps**:
1. Select **Mode** → **Calibration** from the menu
2. The status bar will show: "Calibration mode: Click two points on a known distance"
3. Click the **first point** on your reference distance
   - A red circle will mark the point
4. Click the **second point** on your reference distance
   - Another red circle will mark the point
   - A blue line will connect the two points
5. A dialog will appear asking for the actual distance
6. Enter the real-world distance (e.g., 10 for 10cm)
7. Click **OK**

**Result**: The calibration factor is calculated and displayed. You can now switch to Measurement mode.

#### Calibration Examples

**Example 1: Using a Ruler**
- Click on the 0cm mark
- Click on the 10cm mark
- Enter "10" as the distance

**Example 2: Using a Scale Bar**
- Click at one end of the scale bar
- Click at the other end
- Enter the distance shown on the scale bar

**Example 3: Using Known Object**
- If you know an object in the image is 5 inches wide
- Click on the left edge
- Click on the right edge
- Enter "5" as the distance

### 3. Measurement Mode

Once calibrated, you can measure any distance on the image.

**Steps**:
1. Select **Mode** → **Measurement** from the menu
2. The status bar will show: "Measurement mode: Click two points to measure distance"
3. Click the **first point** of your measurement
4. Click the **second point** of your measurement
5. A dialog will display:
   - Pixel distance
   - Real-world distance in your calibrated units

**Result**: The measurement is displayed, and you can immediately measure again by clicking two new points.

#### Measurement Examples

**Example 1: Measuring a Rectangle Width**
- Click on the left edge
- Click on the right edge
- Read the displayed distance

**Example 2: Measuring a Diagonal**
- Click on one corner
- Click on the opposite corner
- Read the displayed distance

**Example 3: Measuring Multiple Features**
- Measure first feature (points 1 & 2)
- After viewing result, click OK
- Measure second feature (points 3 & 4)
- Repeat as needed

## Tips and Best Practices

### For Better Accuracy

1. **Use Longer Reference Distances**
   - Longer calibration distances provide better accuracy
   - Example: Use 50cm instead of 5cm if possible

2. **Choose Clear Reference Points**
   - Select distinct, easily identifiable points
   - Avoid blurry or ambiguous edges

3. **Calibrate at the Same Scale**
   - If measuring different parts of an image, use a reference at a similar location
   - This accounts for any perspective distortion

4. **Zoom Features** (Future Enhancement)
   - For precise point selection on small features
   - Currently use scrollbars to navigate

### Workflow Tips

1. **Recalibrate When Needed**
   - Switch back to Calibration mode at any time
   - Useful when working with different images or units

2. **Check Status Bar**
   - The status bar shows:
     - Current mode
     - Number of points selected
     - Last measurement result

3. **Visual Feedback**
   - Red circles: Your selected points
   - Blue lines: The measured distance
   - Points reset after each measurement

4. **Multiple Measurements**
   - Stay in Measurement mode to take multiple readings
   - No need to switch modes between measurements

### Working with Different Image Types

**Engineering Drawings**:
- Use scale bars or dimension lines for calibration
- Typically very accurate due to precise scale information

**Floor Plans**:
- Use provided scale (e.g., "1 inch = 10 feet")
- Convert to consistent units (e.g., measure 1 inch on image, enter 120 for 120 inches or 10 for 10 feet)

**Maps**:
- Use map scale bar for calibration
- Account for map projection distortions

**Photographs**:
- Use objects of known size (credit card, ruler, etc.)
- Less accurate due to perspective and angle variations

**Microscopy Images**:
- Use scale bar provided by microscope software
- Critical for scientific accuracy

## Troubleshooting

### Common Issues

**Problem**: "No Calibration" warning when switching to Measurement mode
- **Solution**: Complete calibration first in Calibration mode

**Problem**: Points are not visible
- **Solution**: Ensure image is loaded and you're clicking on the canvas (not outside it)

**Problem**: Measurements seem inaccurate
- **Solution**: 
  - Recalibrate with a longer reference distance
  - Ensure reference points were selected accurately
  - Check that known distance was entered correctly

**Problem**: Can't see the entire image
- **Solution**: Use the scrollbars to navigate. Zoom feature is planned for future releases.

**Problem**: Dialog boxes not appearing
- **Solution**: Check if dialogs are appearing behind the main window

**Problem**: Image won't load
- **Solution**: 
  - Verify file format is supported (PNG, JPG, JPEG, BMP, GIF)
  - Check file is not corrupted
  - Ensure you have read permissions

### Error Messages

**"Failed to load image"**
- File format not supported or file is corrupted
- Try converting to PNG or JPG

**"Invalid distance entered"**
- Distance must be a positive number
- Don't include unit symbols (just enter the number)

**"Points are too close together"**
- Select points farther apart
- Minimum recommended distance: 10 pixels

## Advanced Usage

### Unit Conversions

The application uses a unit-agnostic approach. You can work in any unit:

**Centimeters (cm)**:
- Calibrate: Enter distance in cm
- Measurements: Results in cm

**Inches (in)**:
- Calibrate: Enter distance in inches
- Measurements: Results in inches

**Meters (m)**:
- Calibrate: Enter distance in meters
- Measurements: Results in meters

**Custom Units**:
- You can use any unit system
- Just be consistent between calibration and measurement

### Accuracy Considerations

**Factors Affecting Accuracy**:
1. Image resolution (higher is better)
2. Calibration reference length (longer is better)
3. Point selection precision (click accuracy)
4. Image quality (sharp vs. blurry)
5. Perspective distortion in photographs

**Expected Accuracy**:
- Engineering drawings: ±1-2%
- Maps with scale bars: ±2-5%
- Photographs: ±5-10% (varies with perspective)

### Keyboard Shortcuts

Currently, the application uses menu-based interaction. Future enhancements may include:
- Ctrl+O: Open image
- Ctrl+C: Calibration mode
- Ctrl+M: Measurement mode
- Ctrl+R: Reset points

## Examples by Use Case

### Use Case 1: Measuring a Technical Drawing

**Scenario**: You have a mechanical drawing with a scale bar showing 100mm.

1. Load the drawing image
2. Enter Calibration mode
3. Click at the start of the 100mm scale bar
4. Click at the end of the 100mm scale bar
5. Enter "100" (for 100mm)
6. Enter Measurement mode
7. Click on the two points of the feature you want to measure
8. Record the measurement result

### Use Case 2: Measuring Room Dimensions from a Floor Plan

**Scenario**: Floor plan states "Scale: 1/4 inch = 1 foot"

1. Load the floor plan image
2. Enter Calibration mode
3. Measure 1 inch on the image (4 times the scale unit)
4. Click at start and end of this 1-inch section
5. Enter "48" (1 inch = 4 feet = 48 inches, using the 1/4 inch scale)
6. Enter Measurement mode
7. Measure room dimensions
8. Results will be in inches (divide by 12 for feet)

### Use Case 3: Measuring Features in a Microscopy Image

**Scenario**: Microscopy image with a 10µm scale bar.

1. Load the microscopy image
2. Enter Calibration mode
3. Click at both ends of the 10µm scale bar
4. Enter "10" (for 10 micrometers)
5. Enter Measurement mode
6. Measure cell features
7. Results will be in micrometers

## Keyboard and Mouse Controls

### Mouse Controls
- **Left Click**: Select point
- **Scroll Wheel**: Scroll canvas (if image is larger than window)

### Menu Controls
- **File → Open Image**: Load new image
- **File → Exit**: Close application
- **Mode → Calibration**: Switch to calibration mode
- **Mode → Measurement**: Switch to measurement mode
- **Help → Instructions**: Show brief instructions
- **Help → About**: Show application information

## Future Enhancements

Planned features for future versions:
- Measurement history and logging
- Export measurements to CSV
- Multiple unit support with conversion
- Zoom and pan controls
- Angle measurements
- Multi-point measurements (perimeter, area)
- Undo/redo functionality
- Enhanced UI with measurement list

## Getting Help

If you encounter issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the [Tips and Best Practices](#tips-and-best-practices)
3. Ensure you've followed the [Detailed Instructions](#detailed-instructions)
4. Check that dependencies are installed correctly
5. Open an issue on the project repository

## Additional Resources

- **README.md**: Quick overview and installation
- **test_image_dimensioner.py**: Unit tests demonstrating calculations
- **Project Repository**: [github.com/ahmed-tkhan/Image_Dimensioner](https://github.com/ahmed-tkhan/Image_Dimensioner)
