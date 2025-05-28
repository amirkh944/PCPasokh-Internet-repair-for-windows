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
  Yes, simply enable desired post types in the plugin’s settings.

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
