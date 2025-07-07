=== Comment Schema Builder Pro | افزونه اسکیما کامنت پرو ===
Contributors: amirkh944
Tags: schema, comment, review, rating, star, rich snippets, article, knowledge graph, comments, dashboard, yoast, اسکیما, امتیاز, دیدگاه, ستاره, ریچ اسنیپت, وردپرس
Requires at least: 5.6
Tested up to: 6.5
Stable tag: 2.3
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html

A professional WordPress plugin to automatically generate schema.org Review & Article markup for comments, add star ratings (even without text), show average ratings, visualize ratings statistics in admin dashboard, and seamlessly add average rating to meta description (with full Yoast SEO compatibility).

افزونه وردپرس برای تولید خودکار اسکیما Review و Article برای دیدگاه‌ها، افزودن امتیاز ستاره‌ای (حتی بدون متن)، نمایش میانگین امتیاز، نمودار مدیریتی و افزودن امتیاز به متای توضیحات (سازگار با افزونه یواست).

== Description | توضیحات ==

**English:**

**Comment Schema Builder Pro** adds advanced rich snippets and schema support for comments on posts and custom post types (e.g. posts, software).

Features:
- Automatic schema.org Review & Article markup for each comment and post.
- Star rating field in comment form (1-5), with the ability to submit rating without text.
- All old comments automatically get full rating on activation (if not already rated).
- Stores user rating with comment.
- Displays rating stars under comment text (optional).
- Outputs Review schema with: text, dateCreated, author.name, reviewRating, parentReview, itemReviewed, etc.
- Supports parent/reply comments (`parentReview`).
- If no rating is given, a random rating (4~5) is added for schema.
- Professional settings page with sidebar info, tabbed UI, font Vazirmatn, and Bootstrap RTL.
- Shortcode `[csb_average_rating]` for showing post average rating (stars + value).
- Knowledge graph for posts and reviews.
- Admin dashboard: chart visualization for average and distribution of ratings (Chart.js).
- Optionally adds average rating to meta description (compatible with Yoast SEO and general meta tags).
- Fully translatable and extensible.

---

**فارسی:**

**افزونه اسکیما کامنت پرو** پیشرفته‌ترین افزونه برای افزودن ریچ اسنیپت و اسکیما به دیدگاه‌های وردپرس (پست و پست‌تایپ سفارشی مانند نرم‌افزار).

ویژگی‌ها:
- تولید خودکار اسکیما Review و Article برای هر دیدگاه و محتوا.
- فیلد امتیاز ستاره‌ای (۱ تا ۵) در فرم دیدگاه، با امکان ثبت فقط امتیاز بدون متن.
- ثبت خودکار امتیاز کامل برای دیدگاه‌های قدیمی هنگام فعال‌سازی (در صورت نداشتن امتیاز).
- ذخیره امتیاز ثبت شده همراه هر دیدگاه.
- نمایش ستاره امتیاز زیر متن دیدگاه (اختیاری).
- خروجی اسکیما شامل: متن، تاریخ، نویسنده، امتیاز، parentReview، itemReviewed و غیره.
- پشتیبانی کامل از ریپلای و parentReview.
- اگر امتیاز ثبت نشود، برای اسکیما به صورت رندوم (۴ تا ۵) درج می‌شود.
- تنظیمات حرفه‌ای با ستون راهنما، تب‌بندی، فونت وزیر و بوت‌استرپ راست‌چین.
- شورت‌کد `[csb_average_rating]` برای نمایش میانگین امتیاز (ستاره + عدد).
- گراف دانش برای محتوا و نقدها.
- داشبورد مدیریتی با نمودار میانگین و توزیع امتیازها (Chart.js).
- افزودن میانگین امتیاز به متای توضیحات (سازگار با یواست و سایر افزونه‌های سئو).
- قابلیت ترجمه و توسعه کامل.

== Installation | نصب ==

**English:**
1. Upload plugin folder to `/wp-content/plugins/comment-schema-builder`.
2. Activate the plugin through the 'Plugins' menu in WordPress.
3. On first activation, all old comments without rating will be given full rating for analytics and schema.
4. Configure options in **Settings > اسکیما کامنت** (Comment Schema).
5. Add `[csb_average_rating]` shortcode to any post content to display the average rating.

**فارسی:**
1. پوشه افزونه را در `wp-content/plugins/comment-schema-builder` آپلود کنید.
2. افزونه را از بخش افزونه‌های وردپرس فعال نمایید.
3. پس از فعال‌سازی، تمام دیدگاه‌های قبلی فاقد امتیاز، امتیاز کامل خواهند گرفت.
4. تنظیمات را از مسیر **تنظیمات > اسکیما کامنت** انجام دهید.
5. برای نمایش میانگین امتیاز هر مطلب، شورت‌کد `[csb_average_rating]` را در محتوا قرار دهید.

== FAQ | سوالات متداول ==

**English:**
- **Does it support custom post types?**  
  Yes, simply enable desired post types in the plugin's settings.

- **Can users leave just a rating, without a comment?**  
  Yes, users can submit only a star rating (no text required).

- **Does it support replies (threaded comments)?**  
  Yes, parent/reply comments are handled in the schema with `parentReview`.

- **Is the plugin compatible with Google Rich Results?**  
  Yes, generated JSON-LD is compliant and optimized for Google.

- **How to display average rating?**  
  Use the `[csb_average_rating]` shortcode in your post/page content.

- **Can I customize the star color?**  
  Yes, from the plugin settings.

- **Will it add the rating to the meta description?**  
  Yes, if enabled in settings. If Yoast SEO is active, plugin will auto-integrate and append the rating to the meta description (otherwise, general meta tag will be modified).

---

**فارسی:**
- **آیا افزونه از پست‌تایپ سفارشی پشتیبانی می‌کند؟**  
  بله، از تنظیمات افزونه می‌توانید پست‌تایپ‌های دلخواه را فعال کنید.

- **آیا امکان ثبت فقط امتیاز (بدون متن) وجود دارد؟**  
  بله، کاربران می‌توانند فقط امتیاز ستاره‌ای ارسال کنند.

- **آیا افزونه از پاسخ به دیدگاه (ریپلای) پشتیبانی می‌کند؟**  
  بله، parentReview در اسکیما پشتیبانی می‌شود.

- **آیا افزونه سازگار با نتایج ریچ گوگل است؟**  
  بله، خروجی JSON-LD کاملاً استاندارد و بهینه برای گوگل است.

- **چطور میانگین امتیاز نمایش داده شود؟**  
  با افزودن شورت‌کد `[csb_average_rating]` به محتوا.

- **آیا رنگ ستاره‌ها قابل تغییر است؟**  
  بله، از بخش تنظیمات.

- **آیا امتیاز به متای توضیحات اضافه می‌شود؟**  
  بله، اگر فعال باشد و یواست نصب باشد به صورت خودکار؛ در غیر این صورت به تگ متای توضیحات افزوده می‌شود.

== Screenshots | اسکرین‌شات‌ها ==

1. Star rating in comment form | فیلد ستاره‌ای در فرم دیدگاه
2. Schema output (JSON-LD) | خروجی اسکیما
3. Admin settings page (tabbed, sidebar) | صفحه تنظیمات مدرن و حرفه‌ای
4. Rating statistics dashboard | نمودار مدیریتی امتیازات

== Changelog | تغییرات ==

= 2.3 =
* Adds automatic rating for old comments on activation
* Allows rating-only (no comment text) submissions
* Optionally integrates average rating into meta description (Yoast compatible)
* Modern settings UI with sidebar and RTL font
* All previous features retained

= 2.3 =
* افزودن امتیاز خودکار به دیدگاه‌های قبلی در اولین فعال‌سازی
* امکان ثبت فقط امتیاز بدون متن
* افزودن گزینه نمایش امتیاز در متای توضیحات (سازگار با یواست)
* طراحی تنظیمات حرفه‌ای با ستون راهنما و فونت وزیر
* حفظ تمام امکانات قبلی

== License | مجوز ==
GPLv2 or later

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
