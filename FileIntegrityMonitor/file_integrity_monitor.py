import hashlib
import threading
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox


monitoring = False


# Generate SHA-256 Hash
def generate_hash(file_path):

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


# Save Logs
def save_log(message):

    with open("log.txt", "a") as log_file:
        log_file.write(message + "\n")


# Browse File
def browse_file():

    global selected_file

    selected_file = filedialog.askopenfilename()

    file_label.config(
        text=f"Selected File:\n{selected_file}"
    )


# Start Monitoring
def start_monitoring():

    global monitoring

    if not selected_file:
        messagebox.showerror(
            "Error",
            "Please select a file first."
        )
        return

    monitoring = True

    status_label.config(
        text="Monitoring Started...",
        fg="lightgreen"
    )

    thread = threading.Thread(
        target=monitor_file
    )

    thread.start()


# Stop Monitoring
def stop_monitoring():

    global monitoring

    monitoring = False

    status_label.config(
        text="Monitoring Stopped",
        fg="red"
    )


# Monitor File
def monitor_file():

    global monitoring

    original_hash = generate_hash(selected_file)

    while monitoring:

        current_hash = generate_hash(selected_file)

        if current_hash != original_hash:

            current_time = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            warning_message = (
                f"[{current_time}] WARNING: File Modified!"
            )

            save_log(warning_message)

            messagebox.showwarning(
                "Security Alert",
                warning_message
            )

            hash_label.config(
                text=(
                    f"Old Hash:\n{original_hash}\n\n"
                    f"New Hash:\n{current_hash}"
                )
            )

            original_hash = current_hash

        time.sleep(2)


# GUI Window
root = tk.Tk()

root.title("File Integrity Monitor")

root.geometry("750x620")

root.config(bg="#1e1e2f")

root.resizable(False, False)


selected_file = ""


# Heading
heading = tk.Label(
    root,
    text="File Integrity Monitor",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)

heading.pack(pady=20)


# Select File Button
browse_button = tk.Button(
    root,
    text="Select File",
    command=browse_file,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    cursor="hand2",
    width=18,
    pady=8
)

browse_button.pack(pady=10)


# File Label
file_label = tk.Label(
    root,
    text="No file selected",
    font=("Arial", 11),
    bg="#1e1e2f",
    fg="white",
    wraplength=650
)

file_label.pack(pady=10)


# Start Button
start_button = tk.Button(
    root,
    text="Start Monitoring",
    command=start_monitoring,
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    activebackground="#1976D2",
    cursor="hand2",
    width=18,
    pady=8
)

start_button.pack(pady=10)


# Stop Button
stop_button = tk.Button(
    root,
    text="Stop Monitoring",
    command=stop_monitoring,
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    activebackground="#d32f2f",
    cursor="hand2",
    width=18,
    pady=8
)

stop_button.pack(pady=10)


# Status Label
status_label = tk.Label(
    root,
    text="Monitoring Not Started",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f",
    fg="yellow"
)

status_label.pack(pady=20)


# Hash Label
hash_label = tk.Label(
    root,
    text="Hash details will appear here",
    font=("Consolas", 10),
    bg="#2b2b3d",
    fg="white",
    wraplength=680,
    justify="left",
    padx=15,
    pady=15
)

hash_label.pack(pady=20)


# Run GUI
footer_label = tk.Label(
    root,
    text="File Integrity Monitoring System | Python Security Tool",
    font=("Arial", 9),
    bg="#1e1e2f",
    fg="#888888"
)

footer_label.pack(side="bottom", pady=10)
root.mainloop()