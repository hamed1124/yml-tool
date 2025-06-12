
# YML Tools by Hamed | ابزار مدیریت فایل‌های YML

A graphical utility for splitting, joining, and analyzing YML translation files.  
یک ابزار گرافیکی برای تقسیم، اتصال و تحلیل فایل‌های ترجمه YML.

---

## 🔧 Features | ویژگی‌ها

### 🧩 Split YML File | تقسیم فایل YML
- Split large `.yml` files into smaller parts based on a specified number of lines.
- تقسیم فایل‌های بزرگ YML به بخش‌های کوچکتر با تعداد خط مشخص (پیش‌فرض: ۵۰۰ خط).

### 🔗 Join YML Parts | اتصال فایل‌های جداشده
- Merge multiple `*_partX.yml` files back into the original structure.
- اتصال فایل‌های جداشده با پسوند `part` به یک فایل واحد با حفظ ساختار اصلی.

### 📝 Count Persian Words | شمارش کلمات فارسی
- Automatically count the number of Persian (Farsi) words and translated lines in `.yml` files.
- شمارش خودکار کلمات فارسی و خطوط ترجمه‌شده در فایل‌های YML.

### ⚙ Settings Panel | تنظیمات
- Choose between encoding formats: `utf-8`, `utf-8-sig (BOM)`
- انتخاب فرمت کدگذاری فایل‌ها مانند UTF-8 و UTF-8-BOM
- Set custom line count for splitting.
- تعیین تعداد خطوط دلخواه برای تقسیم فایل‌ها.

---

## 📂 How to Use | نحوه استفاده

1. Run the program (`.exe` or Python file).  
   برنامه را اجرا کنید (فایل exe یا اسکریپت پایتون).
2. Use buttons to:
   - Split a file
   - Join part files
   - Count Persian words
   - Adjust settings
   از دکمه‌ها برای عملیات تقسیم، اتصال، شمارش کلمات و تنظیمات استفاده کنید.
3. Input files can be selected manually.
   فایل‌های ورودی را می‌توانید از طریق پنجره انتخاب فایل انتخاب کنید.
4. Output files will be saved to an `output` folder.
   فایل‌های خروجی در پوشه `output` ذخیره می‌شوند.

---

## ✅ Requirements | پیش‌نیازها

- Python 3.x  
- Libraries used: `tkinter`, `codecs`, `json`, `re`

---

## 💻 Build Executable | ساخت فایل اجرایی

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole yml_tools_gui.py
```

---

## 👤 Author | نویسنده

Developed by **Hamed**  

---

## 📃 License

MIT License
