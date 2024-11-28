import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class DataFilterTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Filter and Query Tool")

        # Filter Form
        tk.Label(self.root, text="Filter Data", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Start Date:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.start_date = tk.Entry(self.root)
        self.start_date.grid(row=1, column=1, pady=5)

        tk.Label(self.root, text="End Date:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.end_date = tk.Entry(self.root)
        self.end_date.grid(row=2, column=1, pady=5)

        tk.Label(self.root, text="Data Type:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.data_type = ttk.Combobox(self.root, values=["Temperature", "Humidity", "Pressure"], state="readonly")
        self.data_type.grid(row=3, column=1, pady=5)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Apply Filter", command=self.apply_filter, bg="blue", fg="white")
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Filtered Data View
        self.result_text = tk.Text(self.root, wrap="word", height=10, width=50)
        self.result_text.grid(row=5, column=0, columnspan=2, pady=10)

    def apply_filter(self):
        # Placeholder for filtering logic
        start_date = self.start_date.get()
        end_date = self.end_date.get()
        data_type = self.data_type.get()

        if not (start_date and end_date and data_type):
            messagebox.showwarning("Incomplete Information", "Please fill all fields.")
            return

        # Simulate fetching filtered data
        self.result_text.delete(1.0, "end")
        self.result_text.insert("end", f"Filtered Data for {data_type}:\n")
        self.result_text.insert("end", f"From {start_date} to {end_date}\n")
        self.result_text.insert("end", "Sample Data:\n - Data1: 45\n - Data2: 50\n - Data3: 60\n")

# Initialize
root = tk.Tk()
DataFilterTool(root)
root.mainloop()
