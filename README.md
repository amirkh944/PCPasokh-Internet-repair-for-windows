# PCPasokh Internet Repair / عیب یاب و ترمیم اینترنت پاسخگو رایانه

A comprehensive Windows application for diagnosing and fixing internet connection issues with a modern, beautiful interface. Developed by PCPasokh Computer Center.

یک برنامه جامع ویندوز برای عیب یابی و رفع مشکلات اتصال اینترنت با رابط کاربری مدرن و زیبا. توسعه یافته توسط مرکز پاسخگو رایانه.

## Features / ویژگی‌ها

### English
- **Comprehensive Network Diagnosis**: Advanced testing of internet connectivity, DNS servers, proxy settings, firewall status
- **Professional Repair Tools**: Complete network stack reset, adapter management, TCP/IP troubleshooting
- **Modern Bilingual Interface**: Beautiful, dark-themed interface with proper Persian text support
- **Unique System Identification**: Generates unique system ID for tracking and support
- **FTP Report Upload**: Automatically uploads diagnostic reports to PCPasokh server
- **Advanced System Information**: Collects detailed hardware, software, and network configuration data
- **Multiple DNS Testing**: Tests Iranian DNS servers (Shecan, 403) and international servers
- **Extensible Architecture**: Modular design for easy feature additions
- **Professional Branding**: PCPasokh Computer Center integration with contact information

### فارسی
- **عیب یابی جامع شبکه**: تست پیشرفته اتصال اینترنت، سرورهای DNS، تنظیمات پروکسی، وضعیت فایروال
- **ابزارهای ترمیم حرفه‌ای**: ریست کامل پشته شبکه، مدیریت آداپتور، عیب یابی TCP/IP
- **رابط کاربری مدرن دوزبانه**: رابط زیبا و تیره با پشتیبانی صحیح از متن فارسی
- **شناسایی منحصر بفرد سیستم**: تولید شناسه یکتا برای پیگیری و پشتیبانی
- **آپلود گزارش FTP**: آپلود خودکار گزارش‌های تشخیصی به سرور پاسخگو رایانه
- **اطلاعات پیشرفته سیستم**: جمع‌آوری اطلاعات دقیق سخت‌افزار، نرم‌افزار و پیکربندی شبکه
- **تست چندین DNS**: تست سرورهای DNS ایرانی (شکن، ۴۰۳) و بین‌المللی
- **معماری قابل توسعه**: طراحی ماژولار برای اضافه کردن آسان ویژگی‌ها
- **برندینگ حرفه‌ای**: یکپارچگی مرکز پاسخگو رایانه با اطلاعات تماس

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
3. **Repair Issues**: Click "Repair Issues" to fix detected network problems
4. **Save Reports**: Use "Save Report" to save diagnostic results to a text file
5. **Upload Reports**: Send reports directly to PCPasokh server via FTP

### فارسی
1. **شروع عیب یابی**: روی دکمه "شروع عیب یابی" کلیک کنید تا تست جامع شبکه آغاز شود
2. **نظارت بر پیشرفت**: پیشرفت و نتایج لحظه‌ای را در ناحیه متن مشاهده کنید
3. **ترمیم مشکلات**: روی "ترمیم مشکلات" کلیک کنید تا مشکلات شبکه برطرف شوند
4. **ذخیره گزارش‌ها**: از "ذخیره گزارش" برای ذخیره نتایج عیب یابی در فایل متنی استفاده کنید
5. **ارسال گزارش‌ها**: گزارش‌ها را مستقیماً به سرور پاسخگو رایانه ارسال کنید

## Diagnostic Tests / تست‌های عیب یابی

The application performs the following tests:

- DNS Resolution Testing (Multiple servers including Iranian DNS)
- HTTP Connectivity Testing
- Ping Tests to Multiple Servers (Google DNS, Cloudflare, Shecan, 403)
- Network Adapter Status Check
- Internet Speed Testing
- Proxy Configuration Check
- Windows Firewall Status
- Network Driver Information

## Automatic Fixes / رفع خودکار مشکلات

When issues are detected, the app attempts these fixes:

- DNS Cache Flush (`ipconfig /flushdns`)
- IP Address Renewal (`ipconfig /release` & `/renew`)
- TCP/IP Stack Reset (`netsh int ip reset`)
- Winsock Reset (`netsh winsock reset`)
- Network Adapter Reset
- ARP Cache Clear
- Internet Explorer Settings Reset

## FTP Configuration / تنظیمات FTP

The application uploads reports to PCPasokh server:

1. Click "Settings" to configure FTP server details
2. Default server: ftp.pcpasokh.ir
3. Test connection before saving
4. Reports are automatically uploaded with unique system ID

## File Structure / ساختار فایل‌ها

```
pcpasokh-internet-repair/
├── main.py                 # Main application file
├── network_diagnostics.py  # Network diagnostic functions
├── ftp_uploader.py         # FTP upload functionality
├── system_info.py          # System information collector
├── requirements.txt        # Python dependencies
├── run.bat                # Windows batch file to run app
├── README.md              # This file
├── CHANGELOG.md           # Version history
├── INSTALL_GUIDE.md       # Detailed installation guide
└── ftp_config.json        # FTP configuration (auto-generated)
```

## Dependencies / وابستگی‌ها

- `customtkinter` - Modern GUI framework
- `requests` - HTTP requests
- `psutil` - System and network monitoring
- `ping3` - Ping functionality
- `speedtest-cli` - Internet speed testing
- `dnspython` - Advanced DNS testing
- `Pillow` - Image support for future enhancements

## Troubleshooting / عیب یابی

### Common Issues / مشکلات رایج

1. **"Python not found"**: Install Python from python.org and add to PATH
2. **Permission errors**: Run as Administrator for network fixes
3. **FTP upload fails**: Check server settings and internet connectivity
4. **GUI doesn't appear**: Ensure all dependencies are installed correctly
5. **Persian text issues**: Application automatically handles proper font rendering

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

## Contact Information / اطلاعات تماس

**PCPasokh Computer Center / مرکز پاسخگو رایانه**
- 📞 Phone: 021-88888888
- 📧 Email: support@pcpasokh.ir
- 🌐 Website: www.pcpasokh.ir

## License / مجوز

This project is developed by PCPasokh Computer Center for professional use.

## Support / پشتیبانی

For technical support and questions:
- Contact PCPasokh Computer Center using the information above
- Ensure you're running as Administrator when needed
- Verify all dependencies are installed correctly
- Use the built-in report upload feature to send diagnostic data

---

**Note**: This application is designed specifically for Windows and requires administrator privileges for some network repair functions.

**توجه**: این برنامه مخصوص ویندوز طراحی شده و برای برخی عملکردهای تعمیر شبکه نیاز به دسترسی مدیر دارد.
