#!/usr/bin/env python3
"""
Quick Start Guide for Image Dimensioner

This script provides instructions for testing the Image Dimensioner application.
"""

print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                    IMAGE DIMENSIONER - QUICK START                        ║
╚═══════════════════════════════════════════════════════════════════════════╝

INSTALLATION:
1. pip install -r requirements.txt

RUN APPLICATION:
2. python image_dimensioner.py

TESTING WITH TEST IMAGE:
3. Create a test image (optional):
   python -c "from PIL import Image, ImageDraw; import math; 
   w,h=800,600; img=Image.new('RGB',(w,h),'white'); d=ImageDraw.Draw(img);
   d.rectangle([(150,80),(650,120)],'lightgray','black',2);
   [d.line([(150+i,85),(150+i,115)],'black',2) for i in range(0,501,100)];
   img.save('test_image.png'); print('Test image created!')"

4. In the application:
   a) File → Open Image → Select test_image.png (or your own image)
   b) Mode → Calibration
   c) Click at pixel 150 (left edge of ruler)
   d) Click at pixel 250 (100 pixels to the right)
   e) Enter "10" (representing 10 cm for this 100-pixel distance)
   f) Mode → Measurement
   g) Click any two points to measure their distance

EXAMPLE WORKFLOW:
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. LOAD IMAGE                                                           │
│    • File → Open Image                                                  │
│    • Select your diagram/drawing/map                                    │
├─────────────────────────────────────────────────────────────────────────┤
│ 2. CALIBRATE                                                            │
│    • Mode → Calibration                                                 │
│    • Click on start of known distance (e.g., 0cm on ruler)            │
│    • Click on end of known distance (e.g., 10cm on ruler)             │
│    • Enter actual distance: 10                                          │
├─────────────────────────────────────────────────────────────────────────┤
│ 3. MEASURE                                                              │
│    • Mode → Measurement                                                 │
│    • Click start point of feature to measure                           │
│    • Click end point of feature to measure                             │
│    • Read result in dialog box                                          │
└─────────────────────────────────────────────────────────────────────────┘

TIPS FOR ACCURACY:
✓ Use longer calibration distances (e.g., 50cm rather than 5cm)
✓ Click precisely on clear, distinct points
✓ Ensure your reference measurement is accurate
✓ Recalibrate if switching between different images

COMMON USE CASES:
• Engineering drawings with scale bars
• Floor plans with dimension markers
• Maps with distance scales
• Microscopy images with scale bars
• Technical diagrams with known dimensions

TROUBLESHOOTING:
? Can't switch to Measurement mode
  → Complete calibration first

? Measurements seem wrong
  → Recalibrate with accurate reference
  → Use a longer calibration distance
  → Verify you entered the correct reference distance

? Image is too large
  → Use scrollbars to navigate
  → Future version will include zoom

DOCUMENTATION:
• README.md - Overview and installation
• USAGE.md - Detailed instructions and examples
• test_image_dimensioner.py - Unit tests

SUPPORT:
For issues or questions, please visit:
https://github.com/ahmed-tkhan/Image_Dimensioner

═══════════════════════════════════════════════════════════════════════════

Ready to start? Run: python image_dimensioner.py

""")
