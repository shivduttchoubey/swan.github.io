import tkinter as tk
from tkinter import messagebox

def configure_mqtt_and_db():
    config_window = tk.Toplevel(root)
    config_window.title("MQTT & Database Configuration")
    config_window.geometry("500x500")
    config_window.configure(bg="#f5f5f5")

    # Section Header
    def section_header(text):
        return tk.Label(
            config_window,
            text=text,
            font=("Helvetica", 14, "bold"),
            bg="#f5f5f5",
            fg="#333333",
        )

    # MQTT Broker Details
    section_header("MQTT Broker Details").pack(pady=10)
    mqtt_frame = tk.Frame(config_window, bg="#f5f5f5")
    mqtt_frame.pack(fill="x", padx=10, pady=5)

    mqtt_fields = {"Broker Host": "", "Broker Port": "", "Topic": ""}
    mqtt_entries = {}

    for field in mqtt_fields:
        frame = tk.Frame(mqtt_frame, bg="#f5f5f5")
        frame.pack(fill="x", pady=5)
        tk.Label(frame, text=field + ":", font=("Helvetica", 12), bg="#f5f5f5").pack(side="left")
        entry = tk.Entry(frame, font=("Helvetica", 12))
        entry.pack(side="right", fill="x", expand=True, padx=5)
        mqtt_entries[field] = entry

    # Database Details
    section_header("Database Details").pack(pady=10)
    db_frame = tk.Frame(config_window, bg="#f5f5f5")
    db_frame.pack(fill="x", padx=10, pady=5)

    db_fields = {"DB Host": "", "DB Port": "", "Database Name": "", "Username": "", "Password": ""}
    db_entries = {}

    for field in db_fields:
        frame = tk.Frame(db_frame, bg="#f5f5f5")
        frame.pack(fill="x", pady=5)
        tk.Label(frame, text=field + ":", font=("Helvetica", 12), bg="#f5f5f5").pack(side="left")
        entry = tk.Entry(frame, font=("Helvetica", 12), show="*" if field == "Password" else None)
        entry.pack(side="right", fill="x", expand=True, padx=5)
        db_entries[field] = entry

    # Submit Button
    def submit_details():
        mqtt_details = {field: entry.get() for field, entry in mqtt_entries.items()}
        db_details = {field: entry.get() for field, entry in db_entries.items()}

        if any(not value.strip() for value in mqtt_details.values()):
            messagebox.showerror("Error", "All MQTT Broker fields are required!")
            return
        if any(not value.strip() for value in db_details.values()):
            messagebox.showerror("Error", "All Database fields are required!")
            return

        # Simulated action: Print details or save them securely
        print("MQTT Details:", mqtt_details)
        print("Database Details:", db_details)
        messagebox.showinfo("Success", "Details saved successfully!")

    tk.Button(
        config_window,
        text="Submit",
        font=("Helvetica", 12),
        bg="#4285F4",
        fg="white",
        activebackground="#357ae8",
        activeforeground="white",
        command=submit_details,
    ).pack(pady=20)

# Main Tkinter Window
root = tk.Tk()
root.title("IoT Dashboard Configuration")
root.geometry("600x400")
root.configure(bg="#f5f5f5")

header = tk.Label(
    root,
    text="IoT Dashboard Configuration",
    font=("Helvetica", 24, "bold"),
    bg="#f5f5f5",
    fg="#333333",
)
header.pack(pady=20)

config_button = tk.Button(
    root,
    text="Configure MQTT & Database",
    font=("Helvetica", 14),
    bg="#34A853",
    fg="white",
    activebackground="#2c8c45",
    activeforeground="white",
    padx=20,
    pady=10,
    command=configure_mqtt_and_db,
)
config_button.pack(pady=20)

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
