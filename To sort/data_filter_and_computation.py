import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataFilterAndComputationTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Filter, Computation, and Visualization Tool")

        # Filter Form
        tk.Label(self.root, text="Filter Data", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Start Date:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.start_date = tk.Entry(self.root)
        self.start_date.grid(row=1, column=1, pady=5)

        tk.Label(self.root, text="End Date:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.end_date = tk.Entry(self.root)
        self.end_date.grid(row=2, column=1, pady=5)

        tk.Label(self.root, text="Data Type:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.data_type = ttk.Combobox(self.root, values=["Distance", "Speed"], state="readonly")
        self.data_type.grid(row=3, column=1, pady=5)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Apply Filter", command=self.apply_filter, bg="blue", fg="white")
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Computation Section
        tk.Label(self.root, text="Computation Tool", font=("Arial", 16)).grid(row=5, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Derived Metric:").grid(row=6, column=0, sticky="e", padx=5, pady=5)
        self.derived_metric = ttk.Combobox(self.root, values=["Acceleration"], state="readonly")
        self.derived_metric.grid(row=6, column=1, pady=5)

        self.compute_button = tk.Button(self.root, text="Compute", command=self.compute_metric, bg="green", fg="white")
        self.compute_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Visualization Section
        tk.Label(self.root, text="Visualization", font=("Arial", 16)).grid(row=8, column=0, columnspan=2, pady=10)

        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.grid(row=9, column=0, columnspan=2, pady=10)

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.graph_axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas.get_tk_widget().pack()

    def apply_filter(self):
        # Simulate fetching data
        start_date = self.start_date.get()
        end_date = self.end_date.get()
        data_type = self.data_type.get()

        if not (start_date and end_date and data_type):
            messagebox.showwarning("Incomplete Information", "Please fill all fields.")
            return

        self.data = {
            "Distance": [0, 10, 20, 30, 40, 50],
            "Speed": [0, 5, 10, 15, 20, 25]
        }

        messagebox.showinfo("Filter Applied", f"Data for {data_type} fetched successfully!")

    def compute_metric(self):
        derived_metric = self.derived_metric.get()

        if derived_metric == "Acceleration":
            # Simulate computing acceleration from distance and speed
            distance = self.data.get("Distance", [])
            speed = self.data.get("Speed", [])

            if not distance or not speed:
                messagebox.showerror("Error", "No data available for computation. Apply filter first.")
                return

            # Compute acceleration (mock computation: ΔSpeed/ΔTime)
            acceleration = [(speed[i] - speed[i - 1]) for i in range(1, len(speed))]
            time = list(range(len(acceleration)))

            # Plotting the derived metric
            self.graph_axes.clear()
            self.graph_axes.plot(time, acceleration, label="Acceleration (m/s²)", marker="o")
            self.graph_axes.set_title("Acceleration Over Time")
            self.graph_axes.set_xlabel("Time (s)")
            self.graph_axes.set_ylabel("Acceleration (m/s²)")
            self.graph_axes.legend()
            self.canvas.draw()

            messagebox.showinfo("Computation Complete", "Acceleration has been computed and plotted.")

        else:
            messagebox.showwarning("Invalid Metric", "Please select a valid derived metric.")

# Initialize
root = tk.Tk()
DataFilterAndComputationTool(root)
root.mainloop()
