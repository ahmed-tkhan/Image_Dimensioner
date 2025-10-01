#!/bin/bash
# Verification script for Image Dimensioner installation

echo "=========================================="
echo "Image Dimensioner - Installation Verification"
echo "=========================================="
echo ""

# Check Python version
echo "1. Checking Python version..."
python_version=$(python3 --version 2>&1)
if [ $? -eq 0 ]; then
    echo "   ✓ $python_version"
else
    echo "   ✗ Python 3 not found"
    exit 1
fi
echo ""

# Check dependencies
echo "2. Checking dependencies..."
if python3 -c "from PIL import Image" 2>/dev/null; then
    echo "   ✓ Pillow is installed"
else
    echo "   ✗ Pillow not found. Run: pip install -r requirements.txt"
    exit 1
fi
echo ""

# Check main application file
echo "3. Checking application files..."
if [ -f "image_dimensioner.py" ]; then
    echo "   ✓ image_dimensioner.py found"
else
    echo "   ✗ image_dimensioner.py not found"
    exit 1
fi
echo ""

# Check syntax
echo "4. Checking Python syntax..."
if python3 -m py_compile image_dimensioner.py 2>/dev/null; then
    echo "   ✓ No syntax errors"
else
    echo "   ✗ Syntax errors found"
    exit 1
fi
echo ""

# Run tests
echo "5. Running unit tests..."
if python3 test_image_dimensioner.py > /dev/null 2>&1; then
    echo "   ✓ All tests passed"
else
    echo "   ✗ Tests failed"
    exit 1
fi
echo ""

# Check documentation
echo "6. Checking documentation..."
docs=("README.md" "USAGE.md" "requirements.txt")
for doc in "${docs[@]}"; do
    if [ -f "$doc" ]; then
        echo "   ✓ $doc found"
    else
        echo "   ✗ $doc not found"
        exit 1
    fi
done
echo ""

echo "=========================================="
echo "✓ All checks passed!"
echo "=========================================="
echo ""
echo "To run the application:"
echo "  python3 image_dimensioner.py"
echo ""
echo "For help:"
echo "  python3 QUICKSTART.py"
echo ""

