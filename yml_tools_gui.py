import os
import re
import json
import tkinter as tk
from tkinter import filedialog, messagebox
import codecs
import yaml

CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
    "encoding": "utf-8-sig",
    "split_lines": 500
}

PERSIAN_WORD_RE = re.compile(r'[\u0600-\u06FF]+')

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_CONFIG.copy()

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

config = load_config()

def split_yml_file():
    file_path = filedialog.askopenfilename(filetypes=[("YML files", "*.yml *.yaml")])
    if not file_path:
        return

    with codecs.open(file_path, 'r', encoding=config["encoding"]) as f:
        lines = f.readlines()

    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)

    os.makedirs("output", exist_ok=True)

    for i in range(0, len(lines), config["split_lines"]):
        part_lines = lines[i:i + config["split_lines"]]
        part_name = f"{name}_part{i // config['split_lines'] + 1}{ext}"
        part_path = os.path.join("output", part_name)
        with codecs.open(part_path, 'w', encoding=config["encoding"]) as pf:
            pf.writelines(part_lines)

    messagebox.showinfo("Done", "File successfully split.")

def join_yml_files():
    files = filedialog.askopenfilenames(filetypes=[("YML files", "*.yml *.yaml")])
    if not files:
        return

    sorted_files = sorted(files)
    all_lines = []

    for fpath in sorted_files:
        with codecs.open(fpath, 'r', encoding=config["encoding"]) as f:
            all_lines.extend(f.readlines())

    output_path = filedialog.asksaveasfilename(defaultextension=".yml", filetypes=[("YML files", "*.yml")])
    if output_path:
        with codecs.open(output_path, 'w', encoding=config["encoding"]) as outf:
            outf.writelines(all_lines)
        messagebox.showinfo("Done", "Files successfully joined.")

def traverse_and_count(obj):
    count = 0
    if isinstance(obj, str):
        tokens = re.split(r'\s+|[^\w\u0600-\u06FF]+', obj)
        for tok in tokens:
            if PERSIAN_WORD_RE.fullmatch(tok):
                count += 1
    elif isinstance(obj, dict):
        for v in obj.values():
            count += traverse_and_count(v)
    elif isinstance(obj, list) or isinstance(obj, tuple):
        for item in obj:
            count += traverse_and_count(item)
    return count

def count_lines_with_persian(filepath):
    count = 0
    with codecs.open(filepath, 'r', encoding=config["encoding"]) as f:
        for line in f:
            if PERSIAN_WORD_RE.search(line):
                count += 1
    return count

def count_persian_stats():
    folder = filedialog.askdirectory()
    if not folder:
        return

    total_words = 0
    total_lines = 0

    for fname in os.listdir(folder):
        if not (fname.endswith(".yml") or fname.endswith(".yaml")):
            continue
        path = os.path.join(folder, fname)

        total_lines += count_lines_with_persian(path)

        try:
            with codecs.open(path, 'r', encoding=config["encoding"]) as f:
                data = yaml.safe_load(f)
            total_words += traverse_and_count(data)
        except Exception:
            txt = codecs.open(path, 'r', encoding=config["encoding"]).read()
            total_words += traverse_and_count(txt)

    messagebox.showinfo("Count Result",
                        f"Total Persian words: {total_words}\nTotal translated lines: {total_lines}")

def open_settings():
    def save_and_close():
        config["encoding"] = encoding_var.get()
        config["split_lines"] = int(line_count_var.get())
        save_config(config)
        settings_window.destroy()

    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    tk.Label(settings_window, text="Encoding:").grid(row=0, column=0)
    encoding_var = tk.StringVar(value=config["encoding"])
    tk.OptionMenu(settings_window, encoding_var, "utf-8", "utf-8-sig").grid(row=0, column=1)

    tk.Label(settings_window, text="Lines per part:").grid(row=1, column=0)
    line_count_var = tk.StringVar(value=str(config["split_lines"]))
    tk.Entry(settings_window, textvariable=line_count_var).grid(row=1, column=1)

    tk.Button(settings_window, text="Save", command=save_and_close).grid(row=2, column=0, columnspan=2, pady=5)

# GUI Setup
root = tk.Tk()
root.title("YML Tools v2.0 by Hamed")
root.geometry("400x250")

tk.Button(root, text="Split YML File", width=30, command=split_yml_file).pack(pady=5)
tk.Button(root, text="Join YML Parts", width=30, command=join_yml_files).pack(pady=5)
tk.Button(root, text="Count Persian Words", width=30, command=count_persian_stats).pack(pady=5)
tk.Button(root, text="Settings", width=30, command=open_settings).pack(pady=5)

root.mainloop()