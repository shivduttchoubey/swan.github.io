import tkinter as tk
from tkinter import ttk

class ErrorLogViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Error and Logging View")

        # Error log title
        self.title_label = tk.Label(self.root, text="System Logs and Errors", font=("Arial", 16), fg="red")
        self.title_label.pack(pady=10)

        # Log area (scrollable)
        self.log_frame = tk.Frame(self.root)
        self.log_frame.pack(pady=10, fill="both", expand=True)

        self.log_text = tk.Text(self.log_frame, wrap="word", height=20, width=60)
        self.scrollbar = tk.Scrollbar(self.log_frame, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=self.scrollbar.set)

        self.log_text.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Simulate adding logs
        self.add_dummy_logs()

    def add_dummy_logs(self):
        logs = [
            "[INFO] MQTT broker connected successfully.",
            "[INFO] Data received on topic 'sensor/data'.",
            "[ERROR] Database connection failed: Timeout occurred.",
            "[WARNING] High latency detected in message processing.",
            "[INFO] System is running smoothly."
        ]
        for log in logs:
            self.log_text.insert("end", f"{log}\n")
        self.log_text.insert("end", "\n--- End of Logs ---\n")

# Initialize
root = tk.Tk()
ErrorLogViewer(root)
root.mainloop()
