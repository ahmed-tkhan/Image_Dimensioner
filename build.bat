@echo off
echo Building Image Dimensioner executable...
echo.

echo Step 1: Creating application icon...
python create_icon.py
if %errorlevel% neq 0 (
    echo ERROR: Failed to create icon
    pause
    exit /b 1
)

echo Step 2: Building executable with PyInstaller...
pyinstaller --clean image_dimensioner.spec
if %errorlevel% neq 0 (
    echo ERROR: Failed to build executable
    pause
    exit /b 1
)

echo.
echo SUCCESS: Build completed!
echo Executable location: dist\ImageDimensioner.exe
echo.
pause