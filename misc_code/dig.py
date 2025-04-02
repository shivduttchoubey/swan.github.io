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
root.geometry("1000x700")

# Add frames for parameter selection and graph display
selection_frame = tk.Frame(root)
selection_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

graph_container = tk.Frame(root)
graph_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Variables for graph management
graphs = []  # List to store graph details

# Selection fields in selection_frame
tk.Label(selection_frame, text="Select Location").grid(row=0, column=0, padx=10, pady=5)
location_var = tk.StringVar(value=locations[0])
ttk.Combobox(selection_frame, textvariable=location_var, values=locations).grid(row=0, column=1, padx=10, pady=5)

tk.Label(selection_frame, text="Select Database").grid(row=1, column=0, padx=10, pady=5)
database_var = tk.StringVar(value=databases[0])
ttk.Combobox(selection_frame, textvariable=database_var, values=databases).grid(row=1, column=1, padx=10, pady=5)

tk.Label(selection_frame, text="Select Table").grid(row=2, column=0, padx=10, pady=5)
table_var = tk.StringVar(value=tables[0])
ttk.Combobox(selection_frame, textvariable=table_var, values=tables).grid(row=2, column=1, padx=10, pady=5)

tk.Label(selection_frame, text="Select Sensor").grid(row=3, column=0, padx=10, pady=5)
sensor_var = tk.StringVar(value=sensors[0])
ttk.Combobox(selection_frame, textvariable=sensor_var, values=sensors).grid(row=3, column=1, padx=10, pady=5)

tk.Label(selection_frame, text="Choose Unit").grid(row=4, column=0, padx=10, pady=5)
unit_var = tk.StringVar(value=units[0])
ttk.Combobox(selection_frame, textvariable=unit_var, values=units).grid(row=4, column=1, padx=10, pady=5)

# Function to create a new graph and add it to the container
def create_graph():
    # Fetch data based on selected parameters
    data = fetch_data(location_var.get(), database_var.get(), table_var.get(), sensor_var.get(), unit_var.get())
    
    # Create Matplotlib figure for the new graph
    fig = Figure(figsize=(5, 3), dpi=100)
    ax = fig.add_subplot(111)
    
    x_values = [item['x_value'] for item in data]
    y_values = [item['y_value'] for item in data]
    
    ax.plot(x_values, y_values, marker='o', label="Y Values")
    ax.set_title(f"Graph ({location_var.get()}, {sensor_var.get()})")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.legend()
    
    # Create a frame for the graph and place it in the grid layout
    graph_frame = tk.Frame(graph_container, relief=tk.RAISED, borderwidth=1)
    graph_frame.grid(row=len(graphs)//2, column=len(graphs)%2, sticky="nsew", padx=5, pady=5)
    
    # Add resizable canvas for the graph
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    # Add buttons for graph editing inside graph frame
    edit_frame = tk.Frame(graph_frame)
    edit_frame.pack(side=tk.BOTTOM, fill=tk.X)
    
    tk.Button(edit_frame, text="Edit Graph Name", command=lambda: edit_graph_name(fig, canvas)).pack(side=tk.LEFT, padx=5)
    tk.Button(edit_frame, text="Edit Scale/Unit", command=lambda: edit_scale_and_unit(fig, canvas)).pack(side=tk.LEFT, padx=5)
    tk.Button(edit_frame, text="Edit Graph Type", command=lambda: edit_graph_type(fig, canvas, data)).pack(side=tk.LEFT, padx=5)
    tk.Button(edit_frame, text="Label Axis", command=lambda: label_axis(fig, canvas)).pack(side=tk.LEFT, padx=5)
    tk.Button(edit_frame, text="Delete Graph", command=lambda: delete_graph(graph_frame)).pack(side=tk.LEFT, padx=5)
    
    # Store graph information for further manipulation
    graphs.append({
        'fig': fig,
        'canvas': canvas,
        'frame': graph_frame
    })

# Graph editing functions
def edit_graph_name(fig, canvas):
    new_name = simpledialog.askstring("Edit Graph Name", "Enter new graph name:")
    if new_name:
        fig.suptitle(new_name)
        canvas.draw()

def edit_scale_and_unit(fig, canvas):
    new_y_label = simpledialog.askstring("Edit Y-axis Unit", "Enter new Y-axis unit:")
    new_x_label = simpledialog.askstring("Edit X-axis Unit", "Enter new X-axis unit:")
    if new_y_label and new_x_label:
        ax = fig.gca()
        ax.set_ylabel(new_y_label)
        ax.set_xlabel(new_x_label)
        canvas.draw()

def edit_graph_type(fig, canvas, data):
    graph_type = simpledialog.askstring("Edit Graph Type", "Enter graph type (line, bar):")
    if graph_type:
        x_values = [item['x_value'] for item in data]
        y_values = [item['y_value'] for item in data]
        
        fig.clear()
        ax = fig.add_subplot(111)
        
        if graph_type == "line":
            ax.plot(x_values, y_values, marker='o', label="Y Values")
        elif graph_type == "bar":
            ax.bar(x_values, y_values, label="Y Values")
        
        ax.legend()
        canvas.draw()

def label_axis(fig, canvas):
    new_x_label = simpledialog.askstring("Label X Axis", "Enter new label for X Axis:")
    new_y_label = simpledialog.askstring("Label Y Axis", "Enter new label for Y Axis:")
    if new_x_label and new_y_label:
        ax = fig.gca()
        ax.set_xlabel(new_x_label)
        ax.set_ylabel(new_y_label)
        canvas.draw()

def delete_graph(graph_frame):
    graph_frame.destroy()
    graphs.remove(next((graph for graph in graphs if graph['frame'] == graph_frame), None))

# Submit button to add a new graph
submit_button = tk.Button(selection_frame, text="Add Graph", command=create_graph)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Configure grid layout for resizable frames
graph_container.columnconfigure(0, weight=1)
graph_container.columnconfigure(1, weight=1)
graph_container.rowconfigure(0, weight=1)
graph_container.rowconfigure(1, weight=1)

# Run the Tkinter main loop
root.mainloop()
