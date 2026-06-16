# Alhoseini.com

A multilingual content management platform built with Django, designed for global content publishing with a focus on educational and informational content.

## Overview

Alhosseini.com is a production-ready CMS that demonstrates the implementation of a multilingual blog platform with rich content editing capabilities. Built with Django 6.0, it features automatic content processing, media management, and a modern administrative interface. The project serves as a comprehensive example of internationalized web applications, incorporating best practices for content moderation, user management, and scalable architecture.

**Key Engineering Decisions:**
- Modular Django architecture with separate apps for user management, content, and categories
- Internationalization (i18n) using Django's LocaleMiddleware and Rosetta for translation management
- Automatic content processing (slug generation, summary extraction)
- Rich text editing with CKEditor, complete with image upload handling
- Modern admin interface using Unfold for enhanced user experience

## Key Features

- **Multilingual Content Management**: Serve content in English, French, Arabic, and German with easy translation management
- **Rich Text Editor Integration**: Full CKEditor integration with file upload support and custom toolbars
- **Automatic Content Processing**: Auto-generate slugs and summaries from post content
- **Media Management**: Custom image models with automatic thumbnail generation
- **Content Lifecycle Control**: Publish/unpublish content with scheduled dating
- **Category-based Organization**: Hierarchical content categorization
- **Modern Admin Interface**: Unfold-powered admin dashboard with enhanced UX
- **Extensible Architecture**: Ready for comments, courses, and additional feature modules
- **Custom User Model**: Extended Django user model for future customization

## Tech Stack

### Backend
- **Django 6.0.5** - High-level Python web framework
- **django-modeltranslation** - Content translation management
- **django-render-partial** - Component-based partial rendering
- **Rosetta** - Translation interface for Django

### Frontend
- **Django Templates** - Server-side HTML templating
- **CKEditor** - WYSIWYG rich text editor
- **Unfold** - Modern Django admin theme

### Media Processing
- **ImageKit** - Image processing and thumbnail generation
- **django-ckeditor-uploader** - Image upload handling for CKEditor

### Database
- **SQLite3** - Development database
- **PostgreSQL** - Production-ready (configured but commented)

---

# Alhoseini.com

یک پلتفرم مدیریت محتوای چندزبانه ساخته شده با جنگو، طراحی شده برای انتشار محتوای آموزشی و اطلاعاتی در سطح جهانی.

## نمای کلی

Alhosseini.com یک سیستم مدیریت محتوای آماده تولید است که پیاده‌سازی یک پلتفرم وبلاگ چندزبانه با قابلیت‌های ویرایش محتوای غنی را به نمایش می‌گذارد. این پروژه با جنگو ۶.۰ ساخته شده و شامل پردازش خودکار محتوا، مدیریت رسانه و رابط مدیریت مدرن است.

**تصمیمات کلیدی مهندسی:**
- معماری ماژولار جنگو با اپلیکیشن‌های مجزا برای مدیریت کاربران، محتوا و دسته‌بندی‌ها
- بین‌المللی‌سازی (i18n) با استفاده از LocaleMiddleware جنگو و روزتا برای مدیریت ترجمه
- پردازش خودکار محتوا (ایجاد اسلاگ، استخراج خلاصه)
- ویرایش متن غنی با CKEditor به همراه قابلیت آپلود تصویر
- رابط مدیریت مدرن با استفاده از Unfold برای تجربه کاربری بهتر

## ویژگی‌های کلیدی

- **مدیریت محتوای چندزبانه**: ارائه محتوا به زبان‌های انگلیسی، فرانسوی، عربی و آلمانی با مدیریت آسان ترجمه
- **یکپارچگی ویرایشگر متن غنی**: یکپارچگی کامل CKEditor با پشتیبانی از آپلود فایل و نوار ابزار سفارشی
- **پردازش خودکار محتوا**: تولید خودکار اسلاگ و خلاصه از محتوای پست
- **مدیریت رسانه**: مدل‌های تصویر سفارشی با تولید خودکار تصاویر کوچک
- **کنترل چرخه حیات محتوا**: انتشار/عدم انتشار محتوا با تاریخ‌گذاری برنامه‌ریزی شده
- **سازمان‌دهی بر اساس دسته‌بندی**: دسته‌بندی سلسله‌مراتبی محتوا
- **رابط مدیریت مدرن**: داشبورد مدیریت با قابلیت Unfold با UX بهبود یافته
- **معماری قابل توسعه**: آماده برای نظرات، دوره‌ها و ماژول‌های ویژگی اضافی
- **مدل کاربر سفارشی**: مدل کاربر توسعه‌یافته جنگو برای سفارشی‌سازی آینده

## پشته فناوری

### بک‌اند
- **جنگو ۶.۰.۵** - فریم‌ورک وب سطح بالای پایتون
- **django-modeltranslation** - مدیریت ترجمه محتوا
- **django-render-partial** - رندرینگ جزئی مبتنی بر کامپوننت
- **روزتا** - رابط ترجمه برای جنگو

### فرانت‌اند
- **تمپلیت‌های جنگو** - قالب‌بندی HTML سمت سرور
- **CKEditor** - ویرایشگر متن غنی WYSIWYG
- **Unfold** - تم مدیریت مدرن جنگو

### پردازش رسانه
- **ImageKit** - پردازش تصویر و تولید تصاویر کوچک
- **django-ckeditor-uploader** - مدیریت آپلود تصویر برای CKEditor

### پایگاه داده
- **SQLite3** - پایگاه داده توسعه
- **PostgreSQL** - آماده تولید (پیکربندی شده اما کامنت شده)
