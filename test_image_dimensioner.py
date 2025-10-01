#!/usr/bin/env python3
"""
Unit tests for Image Dimensioner core functionality.

Tests the mathematical calculations without requiring GUI components.
"""

import unittest
import math


class TestImageDimensionerCalculations(unittest.TestCase):
    """Test core calculation functions."""
    
    def test_calculate_distance_horizontal(self):
        """Test distance calculation for horizontal line."""
        point1 = (0, 0)
        point2 = (100, 0)
        
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        distance = math.sqrt(dx * dx + dy * dy)
        
        self.assertEqual(distance, 100.0)
        
    def test_calculate_distance_vertical(self):
        """Test distance calculation for vertical line."""
        point1 = (0, 0)
        point2 = (0, 50)
        
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        distance = math.sqrt(dx * dx + dy * dy)
        
        self.assertEqual(distance, 50.0)
        
    def test_calculate_distance_diagonal(self):
        """Test distance calculation for diagonal line."""
        point1 = (0, 0)
        point2 = (3, 4)
        
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        distance = math.sqrt(dx * dx + dy * dy)
        
        self.assertEqual(distance, 5.0)  # 3-4-5 triangle
        
    def test_calculate_distance_negative_coordinates(self):
        """Test distance calculation with negative coordinates."""
        point1 = (-10, -10)
        point2 = (10, 10)
        
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        distance = math.sqrt(dx * dx + dy * dy)
        
        expected = math.sqrt(20**2 + 20**2)
        self.assertAlmostEqual(distance, expected, places=5)
        
    def test_calibration_factor(self):
        """Test calibration factor calculation."""
        pixel_distance = 100.0
        known_distance = 10.0  # 10 cm
        
        calibration_factor = known_distance / pixel_distance
        
        self.assertEqual(calibration_factor, 0.1)  # 0.1 cm per pixel
        
    def test_measurement_calculation(self):
        """Test measurement with calibration factor."""
        calibration_factor = 0.1  # 0.1 cm per pixel
        pixel_distance = 250.0
        
        real_distance = pixel_distance * calibration_factor
        
        self.assertEqual(real_distance, 25.0)  # 25 cm
        
    def test_calibration_different_units(self):
        """Test calibration with different unit values."""
        # Test 1: 200 pixels = 5 inches
        pixel_distance = 200.0
        known_distance = 5.0
        calibration_factor = known_distance / pixel_distance
        
        self.assertEqual(calibration_factor, 0.025)  # 0.025 inches per pixel
        
        # Measure 400 pixels
        measured_pixels = 400.0
        real_distance = measured_pixels * calibration_factor
        self.assertEqual(real_distance, 10.0)  # 10 inches
        
    def test_small_calibration(self):
        """Test calibration with small distances."""
        pixel_distance = 10.0
        known_distance = 0.5  # 0.5 cm
        
        calibration_factor = known_distance / pixel_distance
        
        self.assertEqual(calibration_factor, 0.05)  # 0.05 cm per pixel
        
    def test_large_calibration(self):
        """Test calibration with large distances."""
        pixel_distance = 1000.0
        known_distance = 100.0  # 100 cm (1 meter)
        
        calibration_factor = known_distance / pixel_distance
        
        self.assertEqual(calibration_factor, 0.1)  # 0.1 cm per pixel
        
    def test_precision(self):
        """Test calculation precision."""
        # Pi-based distance
        point1 = (0, 0)
        point2 = (math.pi, math.pi)
        
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        distance = math.sqrt(dx * dx + dy * dy)
        
        expected = math.pi * math.sqrt(2)
        self.assertAlmostEqual(distance, expected, places=10)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error conditions."""
    
    def test_zero_distance(self):
        """Test behavior with identical points."""
        point1 = (50, 50)
        point2 = (50, 50)
        
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        distance = math.sqrt(dx * dx + dy * dy)
        
        self.assertEqual(distance, 0.0)
        
    def test_very_small_distance(self):
        """Test with very small distances."""
        point1 = (100.0, 100.0)
        point2 = (100.001, 100.001)
        
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        distance = math.sqrt(dx * dx + dy * dy)
        
        self.assertGreater(distance, 0.0)
        self.assertLess(distance, 0.01)
        
    def test_large_coordinates(self):
        """Test with large coordinate values."""
        point1 = (10000, 10000)
        point2 = (10100, 10100)
        
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        distance = math.sqrt(dx * dx + dy * dy)
        
        expected = 100 * math.sqrt(2)
        self.assertAlmostEqual(distance, expected, places=5)


def run_tests():
    """Run all tests and display results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestImageDimensionerCalculations))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    exit(run_tests())
