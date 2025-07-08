# 🔧 راهنمای ساخت EXE | Build Guide

## 🚀 ساخت سریع | Quick Build

### برای کاربران عادی:
```bash
# فقط دو کلیک!
build_exe.bat
```

### برای کاربران پیشرفته:
```bash
# ساخت ساده
build_simple.bat

# یا استفاده از spec files
pyinstaller PCPasokh_Internet_Repair.spec
```

## 📁 فایل‌های ساخت | Build Files

| فایل | توضیح |
|------|-------|
| `build_exe.bat` | ساخت کامل + بسته قابل حمل |
| `build_simple.bat` | ساخت ساده و سریع |
| `clean_build.bat` | پاک کردن فایل‌های اضافی |
| `PCPasokh_Internet_Repair.spec` | تنظیمات نسخه کامل |
| `PCPasokh_Simple.spec` | تنظیمات نسخه ساده |
| `version_info.py` | اطلاعات نسخه ویندوز |

## 📋 مراحل ساخت | Build Steps

### 1️⃣ آماده‌سازی:
```bash
# نصب وابستگی‌ها
pip install -r requirements.txt

# یا استفاده از fix_dependencies.bat
fix_dependencies.bat
```

### 2️⃣ ساخت:
```bash
# ساخت خودکار (توصیه می‌شود)
build_exe.bat

# یا ساخت ساده
build_simple.bat
```

### 3️⃣ تمیز کردن:
```bash
# پاک کردن فایل‌های اضافی
clean_build.bat
```

## 📦 نتایج | Output

### فایل‌های خروجی:
```
📁 PCPasokh_Internet_Repair_Portable/
├── PCPasokh_Internet_Repair.exe (نسخه کامل)
├── PCPasokh_Internet_Repair_Simple.exe (نسخه ساده)  
├── Run_Full_Version.bat
├── Run_Simple_Version.bat
└── Documentation files
```

### اندازه فایل‌ها:
- **نسخه کامل**: ~40-60 MB
- **نسخه ساده**: ~15-25 MB

## ⚡ نکات سریع | Quick Tips

✅ **برای ساخت سریع**: `build_exe.bat`
✅ **برای اندازه کمتر**: `build_simple.bat`  
✅ **برای کنترل بیشتر**: فایل‌های `.spec`
✅ **برای تمیز کردن**: `clean_build.bat`

❌ **اجرای مستقیم Python روی سیستم کاربر**
❌ **فراموش کردن تست فایل exe**
❌ **نادیده گرفتن مشکلات وابستگی**

## 🔍 عیب‌یابی | Troubleshooting

### مشکلات رایج:

**خطای ماژول:**
```bash
# اضافه کردن ماژول مفقود
pyinstaller --hidden-import missing_module main.py
```

**حجم زیاد:**
```bash
# بهینه‌سازی
pyinstaller --exclude-module unused_module main.py
```

**تست و دیباگ:**
```bash
# اجرا با console
pyinstaller --console main.py
```

## 📞 پشتیبانی | Support

### راهنمای کامل:
- 📄 `EXE_BUILD_GUIDE.md` - راهنمای جامع
- 📄 `QUICK_START.md` - راهنمای سریع

### تماس:
- 📧 support@pcpasokh.ir
- 🌐 www.pcpasokh.ir