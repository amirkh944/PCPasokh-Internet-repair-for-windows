# Network Troubleshooter / عیب یاب اتصال اینترنت

A comprehensive Windows application for diagnosing and fixing internet connection issues with a modern, beautiful interface.

یک برنامه جامع ویندوز برای عیب یابی و رفع مشکلات اتصال اینترنت با رابط کاربری مدرن و زیبا.

## Features / ویژگی‌ها

### English
- **Automatic Network Diagnosis**: Comprehensive testing of internet connectivity
- **Automatic Issue Resolution**: Attempts to fix common network problems
- **Modern GUI**: Beautiful, dark-themed interface built with CustomTkinter
- **Detailed Reporting**: Generates comprehensive diagnostic reports
- **Email Integration**: Automatically sends reports via email when internet is available
- **Speed Testing**: Measures download/upload speeds and ping
- **Network Adapter Monitoring**: Checks status of network adapters
- **DNS and Network Stack Fixes**: Automatic DNS flush, IP renewal, and network stack reset

### فارسی
- **عیب یابی خودکار شبکه**: تست جامع اتصال اینترنت
- **رفع خودکار مشکلات**: تلاش برای رفع مشکلات رایج شبکه
- **رابط کاربری مدرن**: رابط زیبا و تیره ساخته شده با CustomTkinter
- **گزارش دهی دقیق**: تولید گزارش‌های جامع عیب یابی
- **یکپارچگی ایمیل**: ارسال خودکار گزارش‌ها از طریق ایمیل هنگام دسترسی به اینترنت
- **تست سرعت**: اندازه‌گیری سرعت دانلود/آپلود و پینگ
- **نظارت بر آداپتور شبکه**: بررسی وضعیت آداپتورهای شبکه
- **رفع مشکلات DNS و پشته شبکه**: پاک کردن خودکار DNS، تجدید IP و ریست پشته شبکه

## Requirements / پیش‌نیازها

- Windows 10/11
- Python 3.8 or higher / پایتون ۳.۸ یا بالاتر
- Administrator privileges for some network fixes / دسترسی مدیر برای برخی رفع مشکلات شبکه

## Installation / نصب

### Method 1: Using Batch File / روش ۱: استفاده از فایل بچ

1. Double-click `run.bat` - this will automatically:
   - Create a virtual environment
   - Install all dependencies
   - Run the application

### Method 2: Manual Installation / روش ۲: نصب دستی

```bash
# Create virtual environment / ایجاد محیط مجازی
python -m venv venv

# Activate virtual environment / فعال‌سازی محیط مجازی
venv\Scripts\activate.bat

# Install dependencies / نصب وابستگی‌ها
pip install -r requirements.txt

# Run application / اجرای برنامه
python main.py
```

## How to Use / نحوه استفاده

### English
1. **Start Diagnosis**: Click the "Start Diagnosis" button to begin comprehensive network testing
2. **Monitor Progress**: Watch real-time progress and results in the text area
3. **Email Configuration**: Click "Email Config" to set up email reporting
4. **Save Reports**: Use "Save Report" to save diagnostic results to a text file
5. **Automatic Fixes**: The app will automatically attempt to fix detected issues

### فارسی
1. **شروع عیب یابی**: روی دکمه "شروع عیب یابی" کلیک کنید تا تست جامع شبکه آغاز شود
2. **نظارت بر پیشرفت**: پیشرفت و نتایج لحظه‌ای را در ناحیه متن مشاهده کنید
3. **تنظیم ایمیل**: روی "Email Config" کلیک کنید تا گزارش‌دهی ایمیل را تنظیم کنید
4. **ذخیره گزارش‌ها**: از "Save Report" برای ذخیره نتایج عیب یابی در فایل متنی استفاده کنید
5. **رفع خودکار**: برنامه به طور خودکار سعی می‌کند مشکلات شناسایی شده را رفع کند

## Diagnostic Tests / تست‌های عیب یابی

The application performs the following tests:

- DNS Resolution Testing
- HTTP Connectivity Testing
- Ping Tests to Multiple Servers (Google DNS, Cloudflare, Google)
- Network Adapter Status Check
- Internet Speed Testing
- Network Configuration Analysis

## Automatic Fixes / رفع خودکار مشکلات

When issues are detected, the app attempts these fixes:

- DNS Cache Flush (`ipconfig /flushdns`)
- IP Address Renewal (`ipconfig /release` & `/renew`)
- Network Stack Reset (`netsh winsock reset`, `netsh int ip reset`)

## Email Configuration / تنظیمات ایمیل

To enable email reporting:

1. Click "Email Config" button
2. Enter SMTP server details (default: Gmail)
3. Enter your email credentials
4. Enter recipient email address
5. Test connection and save

**Note**: For Gmail, you may need to use an "App Password" instead of your regular password.

## File Structure / ساختار فایل‌ها

```
network-troubleshooter/
├── main.py                 # Main application file
├── network_diagnostics.py  # Network diagnostic functions
├── email_sender.py         # Email functionality
├── requirements.txt        # Python dependencies
├── run.bat                # Windows batch file to run app
├── README.md              # This file
└── email_config.json      # Email configuration (auto-generated)
```

## Dependencies / وابستگی‌ها

- `customtkinter` - Modern GUI framework
- `requests` - HTTP requests
- `psutil` - System and network monitoring
- `ping3` - Ping functionality
- `speedtest-cli` - Internet speed testing
- Standard Python libraries for email, networking, etc.

## Troubleshooting / عیب یابی

### Common Issues / مشکلات رایج

1. **"Python not found"**: Install Python from python.org and add to PATH
2. **Permission errors**: Run as Administrator for network fixes
3. **Email sending fails**: Check firewall settings and use app passwords for Gmail
4. **GUI doesn't appear**: Ensure all dependencies are installed correctly

## Screenshots / تصاویر

The application features:
- Dark, modern theme
- Bilingual interface (English/Persian)
- Real-time progress monitoring
- Comprehensive diagnostic results
- Easy email configuration

## License / مجوز

This project is open source and available under the MIT License.

## Support / پشتیبانی

For issues and questions:
- Check the troubleshooting section above
- Ensure you're running as Administrator when needed
- Verify all dependencies are installed correctly

---

**Note**: This application is designed specifically for Windows and requires administrator privileges for some network repair functions.

**توجه**: این برنامه مخصوص ویندوز طراحی شده و برای برخی عملکردهای تعمیر شبکه نیاز به دسترسی مدیر دارد.
