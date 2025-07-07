# راه‌حل سریع مشکل psutil / Quick Fix for psutil Error

## 🚨 مشکل / Problem
اگر این خطا را دریافت می‌کنید:
```
ImportError: cannot import name '_pswindows' from partially initialized module 'psutil'
```

## 🛠️ راه‌حل‌های سریع / Quick Solutions

### گزینه ۱: اجرای فایل رفع مشکل (توصیه می‌شود)
```bash
# Run the dependency fix file
fix_dependencies.bat
```

### گزینه ۲: استفاده از نسخه ساده
```bash
# Run the simplified version (no external dependencies)
python main_simple.py
```

### گزینه ۳: رفع دستی مشکل
```bash
# Step 1: Uninstall problematic packages
pip uninstall -y psutil speedtest-cli ping3 dnspython

# Step 2: Clear cache
pip cache purge

# Step 3: Reinstall with force
pip install --force-reinstall --no-cache-dir psutil==5.9.5
pip install customtkinter==5.2.0
pip install requests==2.31.0

# Step 4: Run main app
python main.py
```

## 📁 فایل‌های موجود / Available Files

### 🎯 فایل‌های اصلی / Main Files
- **`main.py`** - نسخه کامل با تمام ویژگی‌ها (نیاز به dependencies)
- **`main_simple.py`** - نسخه ساده فقط با کتابخانه‌های داخلی Python
- **`fix_dependencies.bat`** - فایل رفع مشکل وابستگی‌ها

### 🔧 فایل‌های کمکی / Helper Files
- **`run.bat`** - اجرای خودکار نسخه کامل
- **`requirements.txt`** - لیست وابستگی‌ها
- **`network_diagnostics.py`** - ماژول عیب یابی شبکه
- **`ftp_uploader.py`** - ماژول آپلود FTP
- **`system_info.py`** - ماژول اطلاعات سیستم

## 🎨 مقایسه نسخه‌ها / Version Comparison

### نسخه کامل (main.py)
✅ رابط کاربری مدرن با CustomTkinter  
✅ عیب یابی پیشرفته و جامع  
✅ آپلود گزارش به سرور FTP  
✅ اطلاعات سیستم کامل  
❌ نیاز به نصب dependencies  

### نسخه ساده (main_simple.py)  
✅ بدون نیاز به external dependencies  
✅ عیب یابی اساسی شبکه  
✅ رابط کاربری ساده اما کارآمد  
✅ اجرای فوری بدون نصب  
❌ ویژگی‌های محدودتر  

## 🚀 توصیه نهایی / Final Recommendation

1. **ابتدا امتحان کنید**: `fix_dependencies.bat`
2. **اگر مشکل ادامه داشت**: `python main_simple.py`
3. **برای استفاده حرفه‌ای**: مشکل dependencies را حل کرده و از `main.py` استفاده کنید

## 📞 پشتیبانی / Support
- 📧 Email: support@pcpasokh.ir
- 📞 Phone: 021-88888888
- 🌐 Website: www.pcpasokh.ir

---

**نکته**: نسخه ساده (`main_simple.py`) تمام عملکردهای اصلی عیب یابی و ترمیم شبکه را دارد، فقط رابط کاربری ساده‌تر و بدون وابستگی‌های خارجی است.