import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Sample data for selections
locations = ["Location 1", "Location 2", "Location 3"]
databases = ["Database A", "Database B", "Database C"]
tables = ["Table X", "Table Y", "Table Z"]
sensors = ["Sensor 1", "Sensor 2", "Sensor 3"]
units = ["Unit A", "Unit B", "Unit C"]


# Function to simulate data fetching based on selected parameters
def fetch_data(location, database, table, sensor, unit):
    # Simulated data as a list of x, y pairs
    return [{'x_value': i, 'y_value': random.uniform(0, 10)} for i in range(10)]


# Tkinter GUI setup
root = tk.Tk()
root.title("Graph Parameter Selection")
root.geometry("800x600")


# Selection fields
tk.Label(root, text="Select Location").grid(row=0, column=0, padx=10, pady=5)
location_var = tk.StringVar(value=locations[0])
ttk.Combobox(root, textvariable=location_var, values=locations).grid(row=0, column=1, padx=10, pady=5)


tk.Label(root, text="Select Database").grid(row=1, column=0, padx=10, pady=5)
database_var = tk.StringVar(value=databases[0])
ttk.Combobox(root, textvariable=database_var, values=databases).grid(row=1, column=1, padx=10, pady=5)


tk.Label(root, text="Select Table").grid(row=2, column=0, padx=10, pady=5)
table_var = tk.StringVar(value=tables[0])
ttk.Combobox(root, textvariable=table_var, values=tables).grid(row=2, column=1, padx=10, pady=5)


tk.Label(root, text="Select Sensor").grid(row=3, column=0, padx=10, pady=5)
sensor_var = tk.StringVar(value=sensors[0])
ttk.Combobox(root, textvariable=sensor_var, values=sensors).grid(row=3, column=1, padx=10, pady=5)


tk.Label(root, text="Choose Unit").grid(row=4, column=0, padx=10, pady=5)
unit_var = tk.StringVar(value=units[0])
ttk.Combobox(root, textvariable=unit_var, values=units).grid(row=4, column=1, padx=10, pady=5)


# Global variables to store graph and figure references
fig = None
canvas = None


# Function to create a graph based on the fetched data
def create_graph():
    global fig, canvas
    # Fetch data based on selected parameters
    data = fetch_data(location_var.get(), database_var.get(), table_var.get(), sensor_var.get(), unit_var.get())
   
    # Prepare X and Y values
    x_values = [item['x_value'] for item in data]
    y_values = [item['y_value'] for item in data]
   
    # Create or update figure
    if fig is not None:
        fig.clear()  # Clear previous figure
   
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(x_values, y_values, marker='o', label="Y Values")
    ax.set_title("Graph")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.legend()
   
    # Display on Tkinter canvas
    if canvas is not None:
        canvas.get_tk_widget().destroy()
   
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    fig.tight_layout()
   
    # Update toolbar with edit options
    toolbar_frame = tk.Frame(root)
    toolbar_frame.grid(row=7, column=0, columnspan=2, pady=5)
   
    tk.Button(toolbar_frame, text="Edit Graph Name", command=edit_graph_name).grid(row=0, column=0, padx=5)
    tk.Button(toolbar_frame, text="Edit Scale and Unit", command=edit_scale_and_unit).grid(row=0, column=1, padx=5)
    tk.Button(toolbar_frame, text="Edit X/Y Params", command=create_graph).grid(row=0, column=2, padx=5)  # Re-fetch data
    tk.Button(toolbar_frame, text="Edit Graph Type", command=edit_graph_type).grid(row=0, column=3, padx=5)
    tk.Button(toolbar_frame, text="Label the Axis", command=label_axis).grid(row=0, column=4, padx=5)
    tk.Button(toolbar_frame, text="Delete Graph", command=delete_graph).grid(row=0, column=5, padx=5)


# Graph editing functions
def edit_graph_name():
    new_name = simpledialog.askstring("Edit Graph Name", "Enter new graph name:")
    if new_name and fig:
        fig.suptitle(new_name)
        canvas.draw()


def edit_scale_and_unit():
    new_y_label = simpledialog.askstring("Edit Y-axis Unit", "Enter new Y-axis unit:")
    new_x_label = simpledialog.askstring("Edit X-axis Unit", "Enter new X-axis unit:")
    if new_y_label and new_x_label and fig:
        ax = fig.gca()
        ax.set_ylabel(new_y_label)
        ax.set_xlabel(new_x_label)
        canvas.draw()


def edit_graph_type():
    graph_type = simpledialog.askstring("Edit Graph Type", "Enter graph type (line, bar):")
    if graph_type and fig:
        x_values = [item['x_value'] for item in fetch_data(location_var.get(), database_var.get(), table_var.get(), sensor_var.get(), unit_var.get())]
        y_values = [item['y_value'] for item in fetch_data(location_var.get(), database_var.get(), table_var.get(), sensor_var.get(), unit_var.get())]
       
        fig.clear()
        ax = fig.add_subplot(111)
       
        if graph_type == "line":
            ax.plot(x_values, y_values, marker='o', label="Y Values")
        elif graph_type == "bar":
            ax.bar(x_values, y_values, label="Y Values")
       
        ax.legend()
        canvas.draw()


def label_axis():
    new_x_label = simpledialog.askstring("Label X Axis", "Enter new label for X Axis:")
    new_y_label = simpledialog.askstring("Label Y Axis", "Enter new label for Y Axis:")
    if new_x_label and new_y_label and fig:
        ax = fig.gca()
        ax.set_xlabel(new_x_label)
        ax.set_ylabel(new_y_label)
        canvas.draw()


def delete_graph():
    global fig, canvas
    if canvas:
        canvas.get_tk_widget().destroy()
        fig = None
        canvas = None
        messagebox.showinfo("Delete Graph", "Graph deleted.")


# Submit button to create graph
submit_button = tk.Button(root, text="Submit", command=create_graph)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)


root.mainloop()



