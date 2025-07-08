# راهنمای ساخت فایل EXE / EXE Build Guide

## 🚀 روش سریع / Quick Method

### برای کاربران عادی / For Regular Users:
```bash
# فقط این دستور را اجرا کنید / Just run this command:
build_exe.bat
```

## 📋 روش‌های مختلف / Different Methods

### 🔧 روش ۱: ساخت خودکار (توصیه می‌شود)
```bash
# اجرای فایل ساخت خودکار
build_exe.bat
```

**این روش شامل:**
- نصب PyInstaller
- ساخت نسخه کامل
- ساخت نسخه ساده  
- ایجاد بسته قابل حمل
- کپی فایل‌های مستندات

### 🛠️ روش ۲: ساخت دستی

#### نصب PyInstaller:
```bash
pip install pyinstaller
```

#### ساخت نسخه کامل:
```bash
pyinstaller --onefile --windowed --name "PCPasokh_Internet_Repair" main.py
```

#### ساخت نسخه ساده:
```bash
pyinstaller --onefile --windowed --name "PCPasokh_Internet_Repair_Simple" main_simple.py
```

### 🎯 روش ۳: استفاده از فایل‌های Spec

#### برای نسخه کامل:
```bash
pyinstaller PCPasokh_Internet_Repair.spec
```

#### برای نسخه ساده:
```bash
pyinstaller PCPasokh_Simple.spec
```

## 📱 آیکون سفارشی / Custom Icon

### افزودن آیکون:
1. فایل آیکون `.ico` را در پوشه پروژه قرار دهید
2. نام آن را `icon.ico` بگذارید
3. فایل build مجدداً اجرا کنید

### ساخت فایل آیکون:
- از سایت‌هایی مثل [ICO Convert](https://icoconvert.com/) استفاده کنید
- تصویر PNG یا JPG را به ICO تبدیل کنید
- سایز توصیه شده: 256x256 پیکسل

## ⚙️ تنظیمات پیشرفته / Advanced Settings

### کاهش حجم فایل:
```bash
pyinstaller --onefile --windowed --strip --upx-dir="path/to/upx" main.py
```

### حذف کتابخانه‌های غیرضروری:
```bash
pyinstaller --onefile --windowed --exclude-module matplotlib --exclude-module numpy main.py
```

### ساخت با console برای دیباگ:
```bash
pyinstaller --onefile --console main.py
```

## 📁 ساختار فایل‌های خروجی / Output File Structure

```
📁 PCPasokh_Internet_Repair_Portable/
├── 🔧 PCPasokh_Internet_Repair.exe (نسخه کامل - 40-60 MB)
├── 🔧 PCPasokh_Internet_Repair_Simple.exe (نسخه ساده - 15-25 MB)
├── 📄 Run_Full_Version.bat
├── 📄 Run_Simple_Version.bat
├── 📄 README.md
├── 📄 QUICK_START.md
└── 📄 CHANGELOG.md
```

## 🎛️ پارامترهای PyInstaller

### پارامترهای اصلی:
| پارامتر | توضیح |
|---------|-------|
| `--onefile` | تک فایل exe |
| `--windowed` | بدون console |
| `--console` | با console |
| `--name` | نام فایل خروجی |
| `--icon` | آیکون exe |
| `--add-data` | افزودن فایل‌های داده |
| `--hidden-import` | وارد کردن ماژول‌های پنهان |
| `--exclude-module` | حذف ماژول‌های غیرضروری |
| `--upx` | فشرده‌سازی با UPX |
| `--strip` | حذف debug symbols |

### پارامترهای ویندوز:
| پارامتر | توضیح |
|---------|-------|
| `--version-file` | فایل اطلاعات نسخه |
| `--manifest` | فایل manifest |
| `--uac-admin` | نیاز به دسترسی مدیر |

## 🔍 عیب یابی مشکلات / Troubleshooting

### مشکلات رایج:

#### ۱. خطای "Module not found":
```bash
# اضافه کردن ماژول به hidden imports
pyinstaller --hidden-import module_name main.py
```

#### ۲. حجم فایل زیاد:
```bash
# حذف کتابخانه‌های غیرضروری
pyinstaller --exclude-module matplotlib --exclude-module numpy main.py
```

#### ۳. خطای "Failed to execute script":
```bash
# اجرا با console برای دیدن خطا
pyinstaller --console main.py
```

#### ۴. مشکل با tkinter:
```bash
# اضافه کردن ماژول‌های tkinter
pyinstaller --hidden-import tkinter --hidden-import tkinter.ttk main.py
```

### بررسی وابستگی‌ها:
```bash
# نمایش وابستگی‌های یک فایل Python
pipdeptree

# یا برای فایل خاص
python -m modulefinder main.py
```

## 📊 مقایسه روش‌های مختلف

| روش | حجم نهایی | سرعت ساخت | سهولت استفاده |
|-----|-----------|------------|----------------|
| ساخت خودکار | متوسط | سریع | ⭐⭐⭐⭐⭐ |
| ساخت دستی | متوسط | متوسط | ⭐⭐⭐ |
| Spec Files | کم | سریع | ⭐⭐⭐⭐ |

## 🎯 توصیه‌های بهینه‌سازی

### کاهش حجم فایل:
1. **حذف ماژول‌های غیرضروری** در فایل spec
2. **استفاده از UPX** برای فشرده‌سازی
3. **حذف debug symbols** با `--strip`
4. **استفاده از virtual environment** تمیز

### بهبود سرعت اجرا:
1. **استفاده از --onefile** برای سادگی
2. **تست با --console** ابتدا
3. **بهینه‌سازی imports** در کد

### امنیت:
1. **اسکن ویروس** فایل نهایی
2. **تست روی سیستم‌های مختلف**
3. **استفاده از کد امضای دیجیتال**

## 🔐 امضای دیجیتال / Digital Signing

### برای توزیع حرفه‌ای:
```bash
# استفاده از signtool (نیاز به certificate)
signtool sign /f certificate.p12 /p password /t http://timestamp.server PCPasokh_Internet_Repair.exe
```

## 📦 توزیع / Distribution

### ایجاد Installer:
- **NSIS** برای installer ویندوز
- **Inno Setup** برای installer پیشرفته
- **WiX Toolset** برای MSI

### بسته‌بندی:
```bash
# ایجاد ZIP
7z a PCPasokh_Internet_Repair_v2.0.zip PCPasokh_Internet_Repair_Portable/

# یا RAR
rar a PCPasokh_Internet_Repair_v2.0.rar PCPasokh_Internet_Repair_Portable/
```

## 📋 چک‌لیست تست / Testing Checklist

### قبل از توزیع:
- [ ] تست روی ویندوز 10
- [ ] تست روی ویندوز 11  
- [ ] تست با/بدون دسترسی مدیر
- [ ] تست تمام ویژگی‌ها
- [ ] تست اتصال اینترنت
- [ ] تست ذخیره/بارگذاری گزارش
- [ ] اسکن ویروس
- [ ] بررسی اندازه فایل
- [ ] تست روی سیستم تمیز

## 🆘 پشتیبانی / Support

### در صورت مشکل:
1. **فایل log** PyInstaller را بررسی کنید
2. **تست با --console** انجام دهید  
3. **وابستگی‌ها** را بررسی کنید
4. **با پاسخگو رایانه** تماس بگیرید

### اطلاعات تماس:
- 📧 support@pcpasokh.ir
- 📞 021-88888888
- 🌐 www.pcpasokh.ir

---

**نکته مهم**: همیشه فایل exe را روی سیستم‌های مختلف تست کنید قبل از توزیع نهایی!