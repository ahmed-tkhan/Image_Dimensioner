#!/usr/bin/env python3
"""
Create a simple icon for the Image Dimensioner application.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    """Create a simple ruler/measurement icon."""
    # Create a 256x256 image with transparent background
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Colors
    ruler_color = (52, 152, 219)  # Blue
    mark_color = (255, 255, 255)  # White
    number_color = (44, 62, 80)   # Dark blue
    
    # Draw ruler body
    ruler_width = 40
    ruler_height = 200
    ruler_x = (size - ruler_width) // 2
    ruler_y = (size - ruler_height) // 2
    
    # Main ruler rectangle
    draw.rectangle([ruler_x, ruler_y, ruler_x + ruler_width, ruler_y + ruler_height], 
                  fill=ruler_color, outline=number_color, width=3)
    
    # Draw measurement marks
    for i in range(0, 21):  # 20 marks
        y_pos = ruler_y + (i * ruler_height // 20)
        if i % 5 == 0:  # Major marks
            mark_width = ruler_width - 10
            mark_thickness = 3
        else:  # Minor marks
            mark_width = ruler_width - 20
            mark_thickness = 2
            
        mark_x = ruler_x + (ruler_width - mark_width) // 2
        draw.rectangle([mark_x, y_pos, mark_x + mark_width, y_pos + mark_thickness],
                      fill=mark_color)
    
    # Add numbers at major marks
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    for i in range(0, 5):  # Numbers 0, 5, 10, 15, 20
        number = str(i * 5)
        y_pos = ruler_y + (i * 4 * ruler_height // 20)
        
        # Get text size
        bbox = draw.textbbox((0, 0), number, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        text_x = ruler_x - text_width - 5
        text_y = y_pos - text_height // 2
        
        draw.text((text_x, text_y), number, fill=number_color, font=font)
    
    # Add "mm" label
    try:
        font_small = ImageFont.truetype("arial.ttf", 12)
    except:
        font_small = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), "mm", font=font_small)
    text_width = bbox[2] - bbox[0]
    draw.text((ruler_x + ruler_width + 5, ruler_y + ruler_height - 20), "mm", 
              fill=number_color, font=font_small)
    
    return img

def main():
    """Create and save the icon in multiple sizes."""
    # Create the main icon
    icon = create_icon()
    
    # Save in different sizes for ICO format
    sizes = [16, 32, 48, 64, 128, 256]
    icon_images = []
    
    for size in sizes:
        resized = icon.resize((size, size), Image.Resampling.LANCZOS)
        icon_images.append(resized)
    
    # Save as ICO file (multi-size)
    icon.save('app_icon.ico', format='ICO', sizes=[(size, size) for size in sizes])
    
    # Also save as PNG for other uses
    icon.save('app_icon.png', format='PNG')
    
    print("Icon files created:")
    print("- app_icon.ico (multi-size for executable)")
    print("- app_icon.png (PNG version)")

if __name__ == "__main__":
    main()