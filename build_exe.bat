@echo off
title PCPasokh Internet Repair - Build EXE
echo.
echo ================================================================
echo     Building PCPasokh Internet Repair EXE File
echo     ساخت فایل EXE برای نرم‌افزار پاسخگو رایانه
echo ================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo خطا: پایتون نصب نشده یا در PATH قرار ندارد
    pause
    exit /b 1
)

echo Step 1: Installing PyInstaller...
echo مرحله ۱: نصب PyInstaller...
pip install pyinstaller

echo.
echo Step 2: Creating icon file...
echo مرحله ۲: ایجاد فایل آیکون...
REM Create a simple batch script to generate icon (if you have an icon file)
if exist "icon.ico" (
    echo Icon file found: icon.ico
    set ICON_PARAM=--icon=icon.ico
) else (
    echo No icon file found, building without icon
    set ICON_PARAM=
)

echo.
echo Step 3: Building main application EXE...
echo مرحله ۳: ساخت EXE نسخه کامل...

pyinstaller --onefile ^
    --windowed ^
    --name "PCPasokh_Internet_Repair" ^
    %ICON_PARAM% ^
    --add-data "requirements.txt;." ^
    --hidden-import "customtkinter" ^
    --hidden-import "tkinter" ^
    --hidden-import "psutil" ^
    --hidden-import "requests" ^
    --hidden-import "ping3" ^
    --hidden-import "speedtest" ^
    --hidden-import "dns.resolver" ^
    --hidden-import "PIL" ^
    --distpath "dist/full_version" ^
    main.py

echo.
echo Step 4: Building simple version EXE...
echo مرحله ۴: ساخت EXE نسخه ساده...

pyinstaller --onefile ^
    --windowed ^
    --name "PCPasokh_Internet_Repair_Simple" ^
    %ICON_PARAM% ^
    --hidden-import "tkinter" ^
    --distpath "dist/simple_version" ^
    main_simple.py

echo.
echo Step 5: Creating portable package...
echo مرحله ۵: ایجاد بسته قابل حمل...

REM Create portable folder structure
mkdir "PCPasokh_Internet_Repair_Portable" 2>nul
copy "dist\full_version\PCPasokh_Internet_Repair.exe" "PCPasokh_Internet_Repair_Portable\" 2>nul
copy "dist\simple_version\PCPasokh_Internet_Repair_Simple.exe" "PCPasokh_Internet_Repair_Portable\" 2>nul
copy "README.md" "PCPasokh_Internet_Repair_Portable\" 2>nul
copy "QUICK_START.md" "PCPasokh_Internet_Repair_Portable\" 2>nul
copy "CHANGELOG.md" "PCPasokh_Internet_Repair_Portable\" 2>nul

REM Create run scripts
echo @echo off > "PCPasokh_Internet_Repair_Portable\Run_Full_Version.bat"
echo title PCPasokh Internet Repair - Full Version >> "PCPasokh_Internet_Repair_Portable\Run_Full_Version.bat"
echo echo Starting PCPasokh Internet Repair Full Version... >> "PCPasokh_Internet_Repair_Portable\Run_Full_Version.bat"
echo echo شروع نسخه کامل پاسخگو رایانه... >> "PCPasokh_Internet_Repair_Portable\Run_Full_Version.bat"
echo start PCPasokh_Internet_Repair.exe >> "PCPasokh_Internet_Repair_Portable\Run_Full_Version.bat"

echo @echo off > "PCPasokh_Internet_Repair_Portable\Run_Simple_Version.bat"
echo title PCPasokh Internet Repair - Simple Version >> "PCPasokh_Internet_Repair_Portable\Run_Simple_Version.bat"
echo echo Starting PCPasokh Internet Repair Simple Version... >> "PCPasokh_Internet_Repair_Portable\Run_Simple_Version.bat"
echo echo شروع نسخه ساده پاسخگو رایانه... >> "PCPasokh_Internet_Repair_Portable\Run_Simple_Version.bat"
echo start PCPasokh_Internet_Repair_Simple.exe >> "PCPasokh_Internet_Repair_Portable\Run_Simple_Version.bat"

echo.
echo ================================================================
echo     Build completed successfully!
echo     ساخت فایل با موفقیت تکمیل شد!
echo ================================================================
echo.
echo Files created / فایل‌های ایجاد شده:
echo 📁 PCPasokh_Internet_Repair_Portable\
echo    ├── PCPasokh_Internet_Repair.exe (Full Version)
echo    ├── PCPasokh_Internet_Repair_Simple.exe (Simple Version)
echo    ├── Run_Full_Version.bat
echo    ├── Run_Simple_Version.bat
echo    └── Documentation files
echo.
echo You can now distribute the PCPasokh_Internet_Repair_Portable folder
echo اکنون می‌توانید پوشه PCPasokh_Internet_Repair_Portable را توزیع کنید
echo.
pause