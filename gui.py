#gui.py
import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
import time
import threading
import json

LOG_FILE = "firewall_log.txt"
RULES_FILE = "rules.json"

root = tk.Tk()
root.title("🔥 Personal Firewall - Log Monitor")
root.geometry("700x600")  # taller for rules display
root.resizable(False, False)

# Log display
log_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 10))
log_display.pack(padx=10, pady=(10, 0), fill=tk.BOTH, expand=True)

# Clear logs button
def clear_logs():
    if os.path.exists(LOG_FILE):
        if messagebox.askyesno("Clear Logs", "Are you sure you want to clear all logs?"):
            with open(LOG_FILE, "w") as f:
                f.truncate(0)
            log_display.delete("1.0", tk.END)
            log_display.insert(tk.END, "[Logs cleared]\n")

clear_btn = tk.Button(root, text="Clear Logs", command=clear_logs, bg="#d9534f", fg="white", font=("Arial", 11, "bold"))
clear_btn.pack(pady=10)

# Function to load logs
def load_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = f.read()
            log_display.delete("1.0", tk.END)
            log_display.insert(tk.END, data)

# Display rules label and text widget
rules_label = tk.Label(root, text="Current Firewall Rules:", font=("Arial", 12, "bold"))
rules_label.pack(pady=(10, 0))

rules_display = tk.Text(root, height=10, width=80, font=("Courier", 10))
rules_display.pack(padx=10, pady=(0, 10))

def load_rules():
    if os.path.exists(RULES_FILE):
        with open(RULES_FILE, "r") as f:
            rules = json.load(f)
        rules_text = json.dumps(rules, indent=4)
    else:
        rules_text = "No rules.json found."
    return rules_text

def show_rules():
    rules_display.delete("1.0", tk.END)
    rules_display.insert(tk.END, load_rules())

show_rules()

# Auto-refresh logs every 2 seconds without freezing UI
def auto_refresh():
    while True:
        load_logs()
        time.sleep(2)

t = threading.Thread(target=auto_refresh, daemon=True)
t.start()

root.mainloop()
