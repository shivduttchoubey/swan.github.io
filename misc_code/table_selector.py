# # script for single sensor selection for graph visualization

# import tkinter as tk
# from tkinter import ttk

# # Sample data for selections
# locations = ["Location 1", "Location 2", "Location 3"]
# databases = ["Database A", "Database B", "Database C"]
# tables = ["Table X", "Table Y", "Table Z"]
# sensors = ["Sensor 1", "Sensor 2", "Sensor 3"]
# units = ["Unit A", "Unit B", "Unit C"]

# # Function to handle submission
# def submit():
#     print("Selected Location:", location_var.get())
#     print("Selected Database:", database_var.get())
#     print("Selected Table:", table_var.get())
#     print("Selected Sensor:", sensor_var.get())
#     print("Selected Unit:", unit_var.get())
#     root.destroy()  # Close the window after submission

# # Create main window
# root = tk.Tk()
# root.title("Selection Dialog")

# # Selection fields with labels and dropdowns
# tk.Label(root, text="Select the Location").grid(row=0, column=0, padx=10, pady=5)
# location_var = tk.StringVar(value=locations[0])
# ttk.Combobox(root, textvariable=location_var, values=locations).grid(row=0, column=1, padx=10, pady=5)

# tk.Label(root, text="Select the Database").grid(row=1, column=0, padx=10, pady=5)
# database_var = tk.StringVar(value=databases[0])
# ttk.Combobox(root, textvariable=database_var, values=databases).grid(row=1, column=1, padx=10, pady=5)

# tk.Label(root, text="Select the Table").grid(row=2, column=0, padx=10, pady=5)
# table_var = tk.StringVar(value=tables[0])
# ttk.Combobox(root, textvariable=table_var, values=tables).grid(row=2, column=1, padx=10, pady=5)

# tk.Label(root, text="Select the Sensor").grid(row=3, column=0, padx=10, pady=5)
# sensor_var = tk.StringVar(value=sensors[0])
# ttk.Combobox(root, textvariable=sensor_var, values=sensors).grid(row=3, column=1, padx=10, pady=5)

# tk.Label(root, text="Choose the Unit").grid(row=4, column=0, padx=10, pady=5)
# unit_var = tk.StringVar(value=units[0])
# ttk.Combobox(root, textvariable=unit_var, values=units).grid(row=4, column=1, padx=10, pady=5)

# # Submit button
# submit_button = tk.Button(root, text="Submit", command=submit)
# submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# root.mainloop()


import tkinter as tk
from tkinter import ttk

# Sample data for selections
locations = ["Location 1", "Location 2", "Location 3"]
databases = ["Database A", "Database B", "Database C"]
tables = ["Table X", "Table Y", "Table Z"]
sensors = ["Sensor 1", "Sensor 2", "Sensor 3"]
units = ["Unit A", "Unit B", "Unit C"]

# Function to handle submission
def submit():
    print("X-Axis Selections:")
    print("  Location:", location_var_x.get())
    print("  Database:", database_var_x.get())
    print("  Table:", table_var_x.get())
    print("  Sensor:", sensor_var_x.get())
    print("  Unit:", unit_var_x.get())
    
    print("Y-Axis Selections:")
    print("  Location:", location_var_y.get())
    print("  Database:", database_var_y.get())
    print("  Table:", table_var_y.get())
    print("  Sensor:", sensor_var_y.get())
    print("  Unit:", unit_var_y.get())
    
    root.destroy()  # Close the window after submission

# Create main window
root = tk.Tk()
root.title("Graph Parameter Selection")

# Section for X-axis selection
tk.Label(root, text="X-Axis Selections", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
tk.Label(root, text="Select Location").grid(row=1, column=0, padx=10, pady=5)
location_var_x = tk.StringVar(value=locations[0])
ttk.Combobox(root, textvariable=location_var_x, values=locations).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Select Database").grid(row=2, column=0, padx=10, pady=5)
database_var_x = tk.StringVar(value=databases[0])
ttk.Combobox(root, textvariable=database_var_x, values=databases).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Select Table").grid(row=3, column=0, padx=10, pady=5)
table_var_x = tk.StringVar(value=tables[0])
ttk.Combobox(root, textvariable=table_var_x, values=tables).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Select Sensor").grid(row=4, column=0, padx=10, pady=5)
sensor_var_x = tk.StringVar(value=sensors[0])
ttk.Combobox(root, textvariable=sensor_var_x, values=sensors).grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Choose Unit").grid(row=5, column=0, padx=10, pady=5)
unit_var_x = tk.StringVar(value=units[0])
ttk.Combobox(root, textvariable=unit_var_x, values=units).grid(row=5, column=1, padx=10, pady=5)

# Section for Y-axis selection
tk.Label(root, text="Y-Axis Selections", font=("Arial", 12, "bold")).grid(row=6, column=0, columnspan=2, pady=5)
tk.Label(root, text="Select Location").grid(row=7, column=0, padx=10, pady=5)
location_var_y = tk.StringVar(value=locations[0])
ttk.Combobox(root, textvariable=location_var_y, values=locations).grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="Select Database").grid(row=8, column=0, padx=10, pady=5)
database_var_y = tk.StringVar(value=databases[0])
ttk.Combobox(root, textvariable=database_var_y, values=databases).grid(row=8, column=1, padx=10, pady=5)

tk.Label(root, text="Select Table").grid(row=9, column=0, padx=10, pady=5)
table_var_y = tk.StringVar(value=tables[0])
ttk.Combobox(root, textvariable=table_var_y, values=tables).grid(row=9, column=1, padx=10, pady=5)

tk.Label(root, text="Select Sensor").grid(row=10, column=0, padx=10, pady=5)
sensor_var_y = tk.StringVar(value=sensors[0])
ttk.Combobox(root, textvariable=sensor_var_y, values=sensors).grid(row=10, column=1, padx=10, pady=5)

tk.Label(root, text="Choose Unit").grid(row=11, column=0, padx=10, pady=5)
unit_var_y = tk.StringVar(value=units[0])
ttk.Combobox(root, textvariable=unit_var_y, values=units).grid(row=11, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=12, column=0, columnspan=2, pady=10)

root.mainloop()
