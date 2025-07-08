@echo off
title PCPasokh Internet Repair - Simple Build
echo.
echo ========================================
echo   Simple EXE Builder
echo   سازنده ساده فایل EXE  
echo ========================================
echo.

REM Install PyInstaller
echo Installing PyInstaller...
echo نصب PyInstaller...
pip install pyinstaller

echo.
echo Building main application...
echo ساخت نرم‌افزار اصلی...
pyinstaller --onefile --windowed --name "PCPasokh_Internet_Repair" main.py

echo.
echo Building simple version...
echo ساخت نسخه ساده...
pyinstaller --onefile --windowed --name "PCPasokh_Internet_Repair_Simple" main_simple.py

echo.
echo ========================================
echo Build completed!
echo ساخت تکمیل شد!
echo ========================================
echo.
echo Files are in 'dist' folder:
echo فایل‌ها در پوشه 'dist' هستند:
echo - dist\PCPasokh_Internet_Repair.exe
echo - dist\PCPasokh_Internet_Repair_Simple.exe
echo.
pause