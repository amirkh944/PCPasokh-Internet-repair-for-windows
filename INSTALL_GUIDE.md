# Windows Installation Guide / راهنمای نصب ویندوز

## Quick Start / شروع سریع

### For beginners / برای مبتدیان:
1. Download and extract all files to a folder
2. Double-click `run.bat`
3. Wait for installation to complete
4. The application will start automatically

### برای کاربران مبتدی:
1. تمام فایل‌ها را دانلود کرده و در یک پوشه استخراج کنید
2. روی `run.bat` دابل کلیک کنید
3. منتظر تکمیل نصب باشید
4. برنامه به طور خودکار اجرا خواهد شد

---

## Detailed Installation / نصب تفصیلی

### Step 1: Install Python / مرحله ۱: نصب پایتون

1. **Download Python**: Go to [python.org](https://python.org) and download Python 3.8 or newer
2. **Install Python**: 
   - ✅ Check "Add Python to PATH" during installation
   - ✅ Check "Install for all users" (recommended)
3. **Verify installation**: Open Command Prompt and type `python --version`

### مرحله ۱: نصب پایتون
1. **دانلود پایتون**: به [python.org](https://python.org) بروید و پایتون ۳.۸ یا جدیدتر را دانلود کنید
2. **نصب پایتون**:
   - ✅ گزینه "Add Python to PATH" را در هنگام نصب انتخاب کنید
   - ✅ گزینه "Install for all users" را انتخاب کنید (توصیه می‌شود)
3. **تایید نصب**: Command Prompt را باز کرده و `python --version` را تایپ کنید

### Step 2: Download Application / مرحله ۲: دانلود برنامه

1. Download all these files to a folder:
   - `main.py`
   - `network_diagnostics.py`
   - `email_sender.py`
   - `requirements.txt`
   - `run.bat`
   - `README.md`

### Step 3: Run Application / مرحله ۳: اجرای برنامه

**Method A: Using Batch File (Recommended)**
1. Double-click `run.bat`
2. The script will automatically:
   - Create a virtual environment
   - Install all dependencies
   - Start the application

**Method B: Manual Installation**
1. Open Command Prompt as Administrator
2. Navigate to the application folder: `cd path\to\your\folder`
3. Create virtual environment: `python -m venv venv`
4. Activate virtual environment: `venv\Scripts\activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run application: `python main.py`

---

## Usage Guide / راهنمای استفاده

### Main Interface / رابط اصلی

1. **Start Diagnosis Button** / دکمه شروع عیب یابی
   - Begins comprehensive network testing
   - شروع تست جامع شبکه

2. **Email Config Button** / دکمه تنظیم ایمیل
   - Configure email settings for automatic reporting
   - تنظیم ایمیل برای گزارش‌دهی خودکار

3. **Save Report Button** / دکمه ذخیره گزارش
   - Save diagnostic results to text file
   - ذخیره نتایج عیب یابی در فایل متنی

### Diagnostic Process / فرآیند عیب یابی

The application will automatically:
1. Test DNS resolution
2. Check HTTP connectivity
3. Test ping to multiple servers
4. Check network adapter status
5. Measure internet speed (if connected)
6. Attempt automatic fixes if issues found

### فرآیند عیب یابی
برنامه به طور خودکار:
1. DNS را تست می‌کند
2. اتصال HTTP را بررسی می‌کند
3. پینگ به چندین سرور تست می‌کند
4. وضعیت آداپتور شبکه را بررسی می‌کند
5. سرعت اینترنت را اندازه‌گیری می‌کند (در صورت اتصال)
6. در صورت یافتن مشکل، سعی در رفع خودکار می‌کند

### Automatic Fixes / رفع خودکار مشکلات

If problems are detected, the app will try:
1. **DNS Cache Flush** - Clear DNS cache
2. **IP Address Renewal** - Release and renew IP
3. **Network Stack Reset** - Reset Windows network components

### Email Configuration / تنظیم ایمیل

To set up email reporting:
1. Click "Email Config"
2. Enter your email settings:
   - **SMTP Server**: smtp.gmail.com (for Gmail)
   - **SMTP Port**: 587
   - **Your Email**: your-email@gmail.com
   - **Password**: Your email password or app password
   - **Recipient**: where to send reports

**For Gmail users**: You may need to create an "App Password":
1. Go to your Google Account settings
2. Enable 2-Step Verification
3. Generate an App Password
4. Use the App Password instead of your regular password

---

## Troubleshooting / عیب یابی

### Common Issues / مشکلات رایج

#### "Python is not recognized"
**Problem**: Python not found in PATH
**Solution**: Reinstall Python and check "Add Python to PATH"

#### "Permission denied" errors
**Problem**: Administrator privileges needed
**Solution**: Right-click `run.bat` → "Run as administrator"

#### GUI doesn't appear
**Problem**: Display or dependency issues
**Solution**: 
1. Ensure all files are in the same folder
2. Try running: `pip install --upgrade customtkinter`
3. Restart your computer

#### Email sending fails
**Problem**: SMTP authentication or firewall
**Solutions**:
1. Use App Password for Gmail
2. Check firewall settings
3. Try different SMTP server

### Error Messages / پیام‌های خطا

- **"ModuleNotFoundError"**: Dependencies not installed → Run `pip install -r requirements.txt`
- **"Access denied"**: Need administrator privileges → Run as administrator
- **"Connection timeout"**: Network issues → Check internet connection
- **"SMTP authentication failed"**: Wrong email credentials → Check email settings

---

## System Requirements / سیستم مورد نیاز

### Minimum Requirements / حداقل سیستم مورد نیاز
- **OS**: Windows 10 or newer / ویندوز ۱۰ یا جدیدتر
- **Python**: 3.8 or newer / پایتون ۳.۸ یا جدیدتر
- **RAM**: 256 MB free memory / ۲۵۶ مگابایت حافظه آزاد
- **Storage**: 50 MB free space / ۵۰ مگابایت فضای آزاد
- **Network**: Any network adapter / هر آداپتور شبکه‌ای

### Recommended Requirements / سیستم توصیه شده
- **OS**: Windows 11 / ویندوز ۱۱
- **Python**: 3.10 or newer / پایتون ۳.۱۰ یا جدیدتر
- **RAM**: 512 MB free memory / ۵۱۲ مگابایت حافظه آزاد
- **Administrator privileges** for network fixes / دسترسی مدیر برای رفع مشکلات شبکه

---

## Features Overview / نمای کلی ویژگی‌ها

### Diagnostic Tests / تست‌های تشخیصی
- ✅ DNS Resolution Testing
- ✅ HTTP Connectivity Testing  
- ✅ Ping Tests (Google DNS, Cloudflare, Google)
- ✅ Network Adapter Status Check
- ✅ Internet Speed Testing
- ✅ Network Configuration Analysis

### Automatic Repairs / تعمیرات خودکار
- 🔧 DNS Cache Flush (`ipconfig /flushdns`)
- 🔧 IP Address Renewal (`ipconfig /release` & `/renew`)
- 🔧 Winsock Reset (`netsh winsock reset`)
- 🔧 TCP/IP Stack Reset (`netsh int ip reset`)

### Reporting Features / ویژگی‌های گزارش‌دهی
- 📄 Detailed text reports
- 💾 Save reports to file
- 📧 Email reports automatically
- 🕒 Timestamped results
- 📊 Performance metrics

---

## Support / پشتیبانی

### Getting Help / دریافت کمک

If you encounter issues:
1. Check this troubleshooting guide
2. Ensure you're running as Administrator
3. Verify all dependencies are installed
4. Check the README.md file

### اگر با مشکل مواجه شدید:
1. این راهنمای عیب یابی را بررسی کنید
2. اطمینان حاصل کنید که برنامه را با دسترسی مدیر اجرا می‌کنید
3. نصب تمام وابستگی‌ها را تایید کنید
4. فایل README.md را بررسی کنید

### Contact Information / اطلاعات تماس
- Check the main README.md file for more information
- برای اطلاعات بیشتر فایل README.md اصلی را بررسی کنید

---

**Note**: This application requires administrator privileges for some network repair functions. Always run as administrator for best results.

**توجه**: این برنامه برای برخی عملکردهای تعمیر شبکه نیاز به دسترسی مدیر دارد. همیشه با دسترسی مدیر اجرا کنید تا بهترین نتایج را بگیرید.