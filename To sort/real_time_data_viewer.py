import tkinter as tk
from tkinter import ttk
import random
from threading import Thread
import time

class RealTimeDataViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Data Viewer")

        # Graph area (mockup with text for simplicity)
        self.graph_label = tk.Label(self.root, text="Real-Time Graph Updates", font=("Arial", 16))
        self.graph_label.pack(pady=10)

        # Graph update (listbox for demo)
        self.data_list = tk.Listbox(self.root, width=50, height=15)
        self.data_list.pack(pady=10)

        # Start/Stop Buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_updates, bg="green", fg="white")
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_updates, bg="red", fg="white", state="disabled")
        self.stop_button.grid(row=0, column=1, padx=10)

        # Initialize threading
        self.updating = False

    def start_updates(self):
        self.updating = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.update_thread = Thread(target=self.update_data)
        self.update_thread.start()

    def stop_updates(self):
        self.updating = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def update_data(self):
        while self.updating:
            data_point = f"Data Point: {random.randint(1, 100)}"
            self.data_list.insert(tk.END, data_point)
            self.data_list.yview(tk.END)  # Auto-scroll
            time.sleep(1)

# Initialize
root = tk.Tk()
RealTimeDataViewer(root)
root.mainloop()
