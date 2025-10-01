#!/usr/bin/env python3
"""
Example demonstrating the Image Dimensioner calculation functions.

This shows how the core mathematical functions work without the GUI.
Useful for understanding the underlying logic or for integration into other applications.
"""

import math


def calculate_pixel_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in pixels.
    
    Args:
        point1 (tuple): First point as (x, y)
        point2 (tuple): Second point as (x, y)
        
    Returns:
        float: Distance in pixels
    """
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return math.sqrt(dx * dx + dy * dy)


def calculate_calibration_factor(pixel_distance, known_distance):
    """
    Calculate the calibration factor (units per pixel).
    
    Args:
        pixel_distance (float): Distance in pixels
        known_distance (float): Known real-world distance in any unit
        
    Returns:
        float: Calibration factor (units per pixel)
        
    Raises:
        ValueError: If pixel_distance is zero or negative
    """
    if pixel_distance <= 0:
        raise ValueError("Pixel distance must be positive")
    return known_distance / pixel_distance


def calculate_real_distance(pixel_distance, calibration_factor):
    """
    Convert pixel distance to real-world distance using calibration factor.
    
    Args:
        pixel_distance (float): Distance in pixels
        calibration_factor (float): Calibration factor (units per pixel)
        
    Returns:
        float: Real-world distance in calibrated units
    """
    return pixel_distance * calibration_factor


def demo_calibration_and_measurement():
    """Demonstrate a complete calibration and measurement workflow."""
    print("=" * 70)
    print("IMAGE DIMENSIONER - Calculation Example")
    print("=" * 70)
    print()
    
    # Example 1: Calibration
    print("EXAMPLE 1: Calibration")
    print("-" * 70)
    print("Scenario: We have a ruler in the image showing 10cm")
    print()
    
    # Points on the ruler (0cm to 10cm marks)
    ruler_start = (100, 50)
    ruler_end = (300, 50)
    
    print(f"Ruler start point: {ruler_start}")
    print(f"Ruler end point:   {ruler_end}")
    
    # Calculate pixel distance
    pixel_dist = calculate_pixel_distance(ruler_start, ruler_end)
    print(f"Pixel distance:    {pixel_dist:.2f} pixels")
    
    # Known distance (what the ruler shows)
    known_dist = 10.0  # 10 cm
    print(f"Known distance:    {known_dist} cm")
    
    # Calculate calibration factor
    cal_factor = calculate_calibration_factor(pixel_dist, known_dist)
    print(f"Calibration factor: {cal_factor:.6f} cm/pixel")
    print()
    
    # Example 2: Measurement using calibration
    print("EXAMPLE 2: Measurement")
    print("-" * 70)
    print("Scenario: Measure the width of a rectangle in the image")
    print()
    
    # Points on the rectangle
    rect_left = (150, 200)
    rect_right = (250, 200)
    
    print(f"Rectangle left edge:  {rect_left}")
    print(f"Rectangle right edge: {rect_right}")
    
    # Calculate pixel distance
    pixel_dist_rect = calculate_pixel_distance(rect_left, rect_right)
    print(f"Pixel distance:       {pixel_dist_rect:.2f} pixels")
    
    # Convert to real distance
    real_dist = calculate_real_distance(pixel_dist_rect, cal_factor)
    print(f"Real distance:        {real_dist:.4f} cm")
    print()
    
    # Example 3: Diagonal measurement
    print("EXAMPLE 3: Diagonal Measurement")
    print("-" * 70)
    print("Scenario: Measure diagonal distance between two points")
    print()
    
    point_a = (100, 100)
    point_b = (200, 300)
    
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    
    pixel_dist_diag = calculate_pixel_distance(point_a, point_b)
    print(f"Pixel distance: {pixel_dist_diag:.2f} pixels")
    
    real_dist_diag = calculate_real_distance(pixel_dist_diag, cal_factor)
    print(f"Real distance:  {real_dist_diag:.4f} cm")
    print()
    
    # Example 4: Different units
    print("EXAMPLE 4: Using Different Units (Inches)")
    print("-" * 70)
    print("Scenario: Calibrate using inches instead of centimeters")
    print()
    
    # Same pixel measurements but different known distance
    known_dist_inches = 4.0  # 10cm ≈ 3.94 inches, using 4 for simplicity
    cal_factor_inches = calculate_calibration_factor(pixel_dist, known_dist_inches)
    
    print(f"Pixel distance:     {pixel_dist:.2f} pixels")
    print(f"Known distance:     {known_dist_inches} inches")
    print(f"Calibration factor: {cal_factor_inches:.6f} inches/pixel")
    print()
    
    # Measure rectangle in inches
    real_dist_inches = calculate_real_distance(pixel_dist_rect, cal_factor_inches)
    print(f"Rectangle width:    {real_dist_inches:.4f} inches")
    print()
    
    # Example 5: Verification
    print("EXAMPLE 5: Verification")
    print("-" * 70)
    print("Verify: A 100-pixel distance should measure as 5cm with our calibration")
    print()
    
    verification_pixels = 100.0
    verification_real = calculate_real_distance(verification_pixels, cal_factor)
    
    print(f"Pixel distance:      {verification_pixels} pixels")
    print(f"Calculated distance: {verification_real:.4f} cm")
    print(f"Expected:            5.0000 cm")
    print(f"Match: {'✓ YES' if abs(verification_real - 5.0) < 0.0001 else '✗ NO'}")
    print()
    
    print("=" * 70)
    print("Note: These calculations are exactly what the GUI application uses!")
    print("=" * 70)


def demo_accuracy_comparison():
    """Demonstrate how calibration distance affects accuracy."""
    print()
    print("=" * 70)
    print("ACCURACY COMPARISON")
    print("=" * 70)
    print()
    print("Demonstrating why longer calibration distances are more accurate")
    print()
    
    # Simulate a measurement error of ±1 pixel in calibration
    true_calibration = 0.05  # True value: 0.05 cm/pixel
    
    scenarios = [
        ("Short calibration", 20, 1.0),   # 20 pixels = 1 cm
        ("Medium calibration", 100, 5.0),  # 100 pixels = 5 cm
        ("Long calibration", 500, 25.0),   # 500 pixels = 25 cm
    ]
    
    print(f"{'Scenario':<20} {'Pixels':<10} {'Error Impact':<20}")
    print("-" * 70)
    
    for name, pixels, known_cm in scenarios:
        # Calculate with ±1 pixel error
        cal_low = calculate_calibration_factor(pixels - 1, known_cm)
        cal_high = calculate_calibration_factor(pixels + 1, known_cm)
        
        # Measure a 100-pixel distance
        measure_pixels = 100
        dist_low = calculate_real_distance(measure_pixels, cal_low)
        dist_high = calculate_real_distance(measure_pixels, cal_high)
        
        error_range = dist_high - dist_low
        error_percent = (error_range / dist_low) * 100
        
        print(f"{name:<20} {pixels:<10} ±{error_range:.4f} cm ({error_percent:.2f}%)")
    
    print()
    print("Conclusion: Longer calibration distances reduce the impact of")
    print("            pixel selection errors, improving measurement accuracy.")
    print()


if __name__ == "__main__":
    demo_calibration_and_measurement()
    demo_accuracy_comparison()
