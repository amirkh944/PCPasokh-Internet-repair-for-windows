@echo off
title PCPasokh Internet Repair - عیب یاب و ترمیم اینترنت پاسخگو رایانه
echo.
echo ================================================================
echo     PCPasokh Internet Repair Starting...
echo     عیب یاب و ترمیم اینترنت پاسخگو رایانه در حال اجرا...
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

REM Install requirements if they don't exist
if not exist "venv\" (
    echo Creating virtual environment...
    echo ایجاد محیط مجازی...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install requirements
echo Installing requirements...
echo نصب وابستگی ها...
pip install -r requirements.txt

REM Run the application
echo.
echo Starting PCPasokh Internet Repair...
echo شروع عیب یاب و ترمیم اینترنت پاسخگو رایانه...
echo.
python main.py

REM Deactivate virtual environment
deactivate

echo.
echo Application closed. Press any key to exit...
echo برنامه بسته شد. برای خروج کلیدی را فشار دهید...
pause