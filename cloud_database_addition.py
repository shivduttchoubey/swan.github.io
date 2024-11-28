import tkinter as tk
from tkinter import simpledialog, messagebox

def fetch_db_credentials():
    # Function to collect credentials
    db_window = tk.Toplevel(root)
    db_window.title("Database Credentials")
    db_window.geometry("400x300")
    db_window.configure(bg="#f5f5f5")

    # Title
    tk.Label(
        db_window,
        text="Enter Database Credentials",
        font=("Helvetica", 14, "bold"),
        bg="#f5f5f5",
        fg="#333333",
    ).pack(pady=10)

    # Input fields
    fields = ["Host", "Port", "Database Name","Table Name", "Platform(AWS/AZURE/GCP)","Username", "Password"]
    entries = {}

    for field in fields:
        frame = tk.Frame(db_window, bg="#f5f5f5")
        frame.pack(fill="x", padx=10, pady=5)
        tk.Label(frame, text=field + ":", font=("Helvetica", 12), bg="#f5f5f5").pack(side="left")
        entry = tk.Entry(frame, show="*" if field == "Password" else None, font=("Helvetica", 12))
        entry.pack(side="right", fill="x", expand=True, padx=5)
        entries[field] = entry

    # Submit button
    def submit_credentials():
        credentials = {field: entry.get() for field, entry in entries.items()}
        if any(not value.strip() for value in credentials.values()):
            messagebox.showerror("Error", "All fields are required!")
            return
        db_window.destroy()
        # You can connect to the database here using the collected credentials
        messagebox.showinfo(
            "Success",
            f"Database credentials saved successfully!\nHost: {credentials['Host']}",
        )
        print(credentials)  # For debugging

    tk.Button(
        db_window,
        text="Submit",
        font=("Helvetica", 12),
        bg="#4285F4",
        fg="white",
        activebackground="#357ae8",
        activeforeground="white",
        command=submit_credentials,
    ).pack(pady=20)

# Main Tkinter Window
root = tk.Tk()
root.title("IoT Dashboard")
root.geometry("600x400")
root.configure(bg="#f5f5f5")

# Landing Page Content
header = tk.Label(
    root,
    text="IoT Dashboard",
    font=("Helvetica", 24, "bold"),
    bg="#f5f5f5",
    fg="#333333",
)
header.pack(pady=20)

db_button = tk.Button(
    root,
    text="Configure Database",
    font=("Helvetica", 14),
    bg="#34A853",
    fg="white",
    activebackground="#2c8c45",
    activeforeground="white",
    padx=20,
    pady=10,
    command=fetch_db_credentials,
)
db_button.pack(pady=20)

# Footer
footer = tk.Label(
    root,
    text="© 2024 IoT Dashboard Project",
    font=("Helvetica", 10),
    bg="#f5f5f5",
    fg="#777777",
)
footer.pack(side="bottom", pady=20)

# Run Tkinter Main Loop
root.mainloop()
