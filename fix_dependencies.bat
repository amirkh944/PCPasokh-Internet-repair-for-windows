@echo off
title PCPasokh Internet Repair - Fix Dependencies
echo.
echo ================================================================
echo     Fixing Dependencies for PCPasokh Internet Repair
echo     رفع مشکل وابستگی‌ها برای نرم‌افزار پاسخگو رایانه
echo ================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo خطا: پایتون نصب نشده یا در PATH قرار ندارد
    echo.
    echo Please install Python from: https://python.org
    echo لطفا پایتون را از آدرس بالا نصب کنید
    pause
    exit /b 1
)

echo Step 1: Uninstalling problematic packages...
echo مرحله ۱: حذف پکیج‌های مشکل‌دار...
pip uninstall -y psutil speedtest-cli ping3 dnspython

echo.
echo Step 2: Clearing pip cache...
echo مرحله ۲: پاک کردن cache پیپ...
pip cache purge

echo.
echo Step 3: Upgrading pip...
echo مرحله ۳: به‌روزرسانی pip...
python -m pip install --upgrade pip

echo.
echo Step 4: Installing dependencies one by one...
echo مرحله ۴: نصب وابستگی‌ها یکی یکی...

echo Installing customtkinter...
pip install customtkinter==5.2.0

echo Installing requests...
pip install requests==2.31.0

echo Installing psutil (with force reinstall)...
pip install --force-reinstall --no-cache-dir psutil==5.9.5

echo Installing ping3...
pip install ping3==4.0.4

echo Installing speedtest-cli...
pip install speedtest-cli==2.1.3

echo Installing dnspython...
pip install dnspython==2.4.2

echo Installing Pillow...
pip install Pillow==10.0.1

echo.
echo Step 5: Verifying installation...
echo مرحله ۵: تایید نصب...

python -c "import psutil; print('✅ psutil:', psutil.__version__)"
python -c "import customtkinter; print('✅ customtkinter imported successfully')"
python -c "import requests; print('✅ requests:', requests.__version__)"

echo.
echo Dependencies fixed successfully!
echo وابستگی‌ها با موفقیت رفع شدند!
echo.
echo Now running the application...
echo اکنون برنامه اجرا می‌شود...
echo.

python main.py

pause