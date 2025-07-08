@echo off
title PCPasokh Internet Repair - Clean Build Files
echo.
echo ========================================
echo   Cleaning Build Files
echo   پاک کردن فایل‌های ساخت
echo ========================================
echo.

echo Removing build directories...
echo حذف پوشه‌های ساخت...

if exist "build" (
    rmdir /s /q "build"
    echo ✓ Removed 'build' directory
    echo ✓ پوشه 'build' حذف شد
)

if exist "dist" (
    rmdir /s /q "dist"
    echo ✓ Removed 'dist' directory
    echo ✓ پوشه 'dist' حذف شد
)

if exist "__pycache__" (
    rmdir /s /q "__pycache__"
    echo ✓ Removed '__pycache__' directory
    echo ✓ پوشه '__pycache__' حذف شد
)

echo.
echo Removing spec files...
echo حذف فایل‌های spec...

if exist "*.spec" (
    del "*.spec" /q
    echo ✓ Removed spec files
    echo ✓ فایل‌های spec حذف شدند
)

echo.
echo Removing portable package...
echo حذف بسته قابل حمل...

if exist "PCPasokh_Internet_Repair_Portable" (
    rmdir /s /q "PCPasokh_Internet_Repair_Portable"
    echo ✓ Removed portable package
    echo ✓ بسته قابل حمل حذف شد
)

echo.
echo ========================================
echo Cleanup completed!
echo پاک‌سازی تکمیل شد!
echo ========================================
echo.
echo All build files have been removed.
echo تمام فایل‌های ساخت حذف شدند.
echo.
pause