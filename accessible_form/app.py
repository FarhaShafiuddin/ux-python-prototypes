#UX prototyping · Accessibility-focused design · Python UI

## This project is a desktop form prototype built using Python and Tkinter to
## explore how small interface decisions affect usability and accessibility.
## Rather than focusing on visual polish, the goal was to design a form that reduces
## user frustration, provides clear feedback, and supports error recovery — especially
## for users who are easily overwhelmed by poorly designed forms.

BG_COLOR = "#367691"
TEXT_COLOR = "#111827"
SUBTEXT_COLOR = "#374151"
ACCENT_COLOR = "#2563eb"
ERROR_COLOR = "#b91c1c"
SUCCESS_COLOR = "#15803d"



import tkinter as tk
from tkinter import messagebox
import re

# ---------- Validation helpers ----------
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

# ---------- Submit action ----------
def submit_form():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    message = message_text.get("1.0", tk.END).strip()

    if not name:
        status_label.config(text="Please enter your name.", fg="red")
        name_entry.focus()
        return

    if not email:
        status_label.config(text="Please enter your email.", fg="red")
        email_entry.focus()
        return

    if not is_valid_email(email):
        status_label.config(text="Please enter a valid email address.", fg="red")
        email_entry.focus()
        return

    # Success
    status_label.config(
        text="Thank you! Your information was submitted successfully.",
        fg="green"
    )

    # Clear fields (optional UX choice)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)

# ---------- Main window ----------
root = tk.Tk()
root.title("Accessible Form Prototype")
root.geometry("420x380")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# ---------- Layout ----------
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)
frame.configure(bg=BG_COLOR)


title_label = tk.Label(
    frame,
    text="Accessible Form Prototype",
    font=("Segoe UI", 16, "bold")
)
title_label.pack(pady=(0, 15))

# Name
tk.Label(frame, text="Name (required):").pack(anchor="w")
name_entry = tk.Entry(frame, width=40)
name_entry.pack(pady=(0, 10))

# Email
tk.Label(frame, text="Email (required):").pack(anchor="w")
email_entry = tk.Entry(frame, width=40)
email_entry.pack(pady=(0, 10))

# Message
tk.Label(frame, text="Message (optional):").pack(anchor="w")
message_text = tk.Text(frame, height=5, width=40)
message_text.pack(pady=(0, 15))

# Submit button
submit_button = tk.Button(
    frame,
    text="Submit",
    command=submit_form,
    width=15
)
submit_button.pack()

# Status message
status_label = tk.Label(frame, text="", font=("Arial", 10))
status_label.pack(pady=(15, 0))

# ---------- Accessibility touches ----------
name_entry.focus()
root.bind("<Return>", lambda event: submit_form())

# ---------- Start app ----------
root.mainloop()
