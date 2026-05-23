import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to check password strength
def check_password():

    password = password_entry.get()

    strength = 0
    remarks = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("At least 8 characters")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add uppercase letter")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add lowercase letter")

    # Number Check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Add number")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add special character")

    # Update Progress Bar
    progress["value"] = strength * 20
    # Display Result
    if strength == 5:
        result_label.config(text="Strong Password", fg="green")
    elif strength >= 3:
        result_label.config(text="Medium Password", fg="orange")
    else:
        result_label.config(text="Weak Password", fg="red")

    # Suggestions
    suggestion_text = "\n".join(remarks)

    suggestion_label.config(text=suggestion_text)

# Main Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x500")
root.config(bg="#1e1e2f")

# Heading
heading = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
heading.pack(pady=10)

# Password Entry
password_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 14),
    show="*",
    bd=3
)
# Function to show/hide password
def toggle_password():

    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")
password_entry.pack(pady=10)
# Show Password Checkbox
show_var = tk.BooleanVar()

show_password = tk.Checkbutton(
    root,
    text="Show Password",
    variable=show_var,
    command=toggle_password,
    bg="#1e1e2f",
    fg="white",
    activebackground="#1e1e2f",
    activeforeground="white",
    selectcolor="#1e1e2f",
    font=("Arial", 10)
)

show_password.pack()

# Check Button
check_button = tk.Button(
    root,
    text="Check Strength",
    font=("Arial", 12, "bold"),
    command=check_password,
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5
)

check_button.pack(pady=15)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
)

result_label.pack(pady=10)
# Progress Bar
progress = ttk.Progressbar(
    root,
    length=250,
    mode='determinate'
)

progress.pack(pady=15)

# Suggestion Label
suggestion_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    bg="#1e1e2f",
    fg="white",
    justify="left"
)
suggestion_label.pack(pady=10)

# Run Window
# Center Window
window_width = 500
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.mainloop()