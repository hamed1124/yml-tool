
# YML Splitter & Merger Tool | ابزار تقسیم و ادغام فایل YML

This tool helps you split and merge `.yml` files into smaller parts (e.g., every 500 lines) while preserving structure and encoding (UTF-8 with BOM). It supports both command-line and graphical interface (GUI).

این ابزار به شما کمک می‌کند فایل‌های `.yml` را به بخش‌های کوچکتر (مثلاً هر ۵۰۰ خط) تقسیم کرده و مجدد به یکدیگر متصل کنید، در حالی که ساختار و رمزگذاری (`UTF-8 with BOM`) فایل حفظ می‌شود. این ابزار هم نسخه ترمینال دارد و هم رابط گرافیکی (GUI).

---

## 🔧 Features | امکانات

- ✅ Split `.yml` files into parts (e.g., 500 lines each)  
- ✅ Merge parts back into the original file  
- ✅ Preserves `utf-8-sig` encoding and newline structure  
- ✅ Command-line version and GUI version (using `tkinter`)  
- ✅ مناسب برای فایل‌های ترجمه بازی یا پروژه‌های چندزبانه

---

## 🖥️ How to Use (Terminal Version) | نحوه استفاده (نسخه ترمینالی)

```bash
# 1 = Split, 2 = Join
python yml_tool.py
```

Place the original file in the `input` folder. The output files will be saved to the `output` folder.

فایل اصلی را در پوشه `input` قرار دهید. فایل‌های خروجی در پوشه `output` ذخیره می‌شوند.

---

## 🖱️ GUI Version | نسخه گرافیکی

Run the following:

```bash
python yml_gui_tool.py
```

Two buttons will appear:
- **Split YML File**: Choose a file to split into parts
- **Join YML Parts**: Select one of the part files to merge all parts into one

دو دکمه نمایش داده می‌شود:
- **Split YML File**: انتخاب فایل برای تقسیم
- **Join YML Parts**: انتخاب یکی از پارت‌ها برای ادغام کل فایل

---

## 🛠️ How to Build .exe | ساخت فایل اجرایی ویندوز

Make sure Python and [PyInstaller](https://pyinstaller.org/) are installed.

```bash
pip install pyinstaller

# For terminal version:
pyinstaller --onefile yml_tool.py

# For GUI version (no console window):
pyinstaller --onefile --noconsole yml_gui_tool.py
```

The `.exe` file will be created in the `dist/` folder.

فایل اجرایی در پوشه `dist/` قرار خواهد گرفت.

---

## 📁 File Structure | ساختار پوشه‌ها

```
project/
│
├── input/           # Original file location
├── output/          # Result after split or join
├── yml_tool.py      # Terminal version
├── yml_gui_tool.py  # GUI version
├── dist/            # Compiled .exe files (after building)
└── README.md        # This file
```

---

## 📌 Notes | نکات

- This tool supports **UTF-8 with BOM** (`utf-8-sig`) encoding.  
- Handles newline preservation (`newline=''`) to ensure file structure stays intact.
- Only `.yml` files are officially supported (but others may work too).

- این ابزار از کدگذاری `UTF-8 with BOM` پشتیبانی می‌کند.
- ساختار خط‌ها حفظ می‌شود.
- فقط فایل‌های `.yml` رسماً پشتیبانی می‌شوند.

---

## 🧑‍💻 Author

Made by **hamed**  
Created with ❤️ using Python and Tkinter  
ساخته شده با عشق با پایتون و Tkinter

---
