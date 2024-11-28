import tkinter as tk
from tkinter import ttk, simpledialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import random
import os
import subprocess
import time


class Graph(ttk.Frame):
   def __init__(self, master, title, graph_type, update_callback):
       super().__init__(master)
       self.title = title
       self.graph_type = graph_type
       self.update_callback = update_callback
       self.create_widgets()


   def create_widgets(self):
       self.header = ttk.Frame(self)
       self.header.pack(fill=tk.X)


       ttk.Label(self.header, text=self.title).pack(side=tk.LEFT)
       ttk.Button(self.header, text="Edit", command=self.edit_graph).pack(side=tk.RIGHT)


       self.fig = Figure(figsize=(5, 4), dpi=100)
       self.ax = self.fig.add_subplot(111)
       self.canvas = FigureCanvasTkAgg(self.fig, master=self)
       self.canvas.draw()
       self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


       ttk.Button(self, text="Resize", command=self.resize_graph).pack(side=tk.RIGHT, anchor=tk.SE)


       self.plot_default()


   def plot_default(self):
       self.ax.clear()
       if self.graph_type == "Line Plot":
           x = np.linspace(0, 10, 100)
           y = np.sin(x)
           self.ax.plot(x, y)
       elif self.graph_type == "Bar Chart":
           x = ['A', 'B', 'C', 'D']
           y = [3, 7, 2, 5]
           self.ax.bar(x, y)
       elif self.graph_type == "Scatter Plot":
           x = np.random.rand(50)
           y = np.random.rand(50)
           self.ax.scatter(x, y)
       self.ax.set_title(self.title)
       self.canvas.draw()


   def edit_graph(self):
       new_title = simpledialog.askstring("Edit Graph", "Enter new title:", initialvalue=self.title)
       if new_title:
           self.title = new_title
           self.ax.set_title(self.title)
           self.canvas.draw()
           self.update_callback()


   def resize_graph(self):
       new_size = simpledialog.askstring("Resize Graph", "Enter new size (width,height):")
       if new_size:
           width, height = map(int, new_size.split(','))
           self.fig.set_size_inches(width/100, height/100)
           self.canvas.draw()


   def update_data(self):
       if self.graph_type == "Line Plot":
           x = np.linspace(0, 10, 100)
           y = np.sin(x + random.random())
           self.ax.clear()
           self.ax.plot(x, y)
       elif self.graph_type == "Bar Chart":
           x = ['A', 'B', 'C', 'D']
           y = [random.randint(1, 10) for _ in range(4)]
           self.ax.clear()
           self.ax.bar(x, y)
       elif self.graph_type == "Scatter Plot":
           x = np.random.rand(50)
           y = np.random.rand(50)
           self.ax.clear()
           self.ax.scatter(x, y)
       self.ax.set_title(self.title)
       self.canvas.draw()


class Dashboard(tk.Tk):
   def __init__(self):
       super().__init__()
       self.title("Dashboard")
       self.geometry("1000x800")
       self.create_widgets()


   def create_widgets(self):
       self.grid_columnconfigure(1, weight=1)
       self.grid_rowconfigure(1, weight=1)


       # Header
       header = ttk.Frame(self)
       header.grid(row=0, column=0, columnspan=2, sticky="ew")
       ttk.Label(header, text="Dashboard", font=("Arial", 20)).pack(side=tk.LEFT, padx=10)
       ttk.Button(header, text="Account Control", command=self.account_control).pack(side=tk.RIGHT, padx=10)


       # Left Column for dynamic graphs
       self.left_column = ttk.Frame(self, width=200)
       self.left_column.grid(row=1, column=0, sticky="ns")
       self.dynamic_graphs = self.create_dynamic_graphs()


       # Main graph area
       self.graph_area = ttk.Frame(self)
       self.graph_area.grid(row=1, column=1, sticky="nsew")
       self.graphs = []
       for i, graph_type in enumerate(["Line Plot", "Bar Chart", "Scatter Plot"]):
           graph = Graph(self.graph_area, f"Graph {i+1}", graph_type, self.update_dynamic_graphs)
           graph.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="nsew")
           self.graphs.append(graph)


       # Add graph button
       ttk.Button(self, text="+", command=self.add_graph).grid(row=2, column=1, sticky="se", padx=10, pady=10)


       # Update button
       ttk.Button(self, text="Update All", command=self.update_all_graphs).grid(row=2, column=1, sticky="sw", padx=10, pady=10)


   def create_dynamic_graphs(self):
       dynamic_graphs = []
       for i in range(5):  # Creating 5 dynamic graphs
           fig = Figure(figsize=(2, 1), dpi=100)
           ax = fig.add_subplot(111)
           canvas = FigureCanvasTkAgg(fig, master=self.left_column)
           canvas.draw()
           canvas.get_tk_widget().pack(pady=5)


           x = np.linspace(0, 10, 100)
           y = np.sin(x + i)
           ax.plot(x, y)
           ax.set_title(f"Dynamic Graph {i+1}")
           fig.tight_layout()
           dynamic_graphs.append((fig, ax, canvas))
       return dynamic_graphs


   def add_graph(self):
       graph_types = ["Line Plot", "Bar Chart", "Scatter Plot"]
       choice = simpledialog.askstring("Add Graph", "Select graph type:", initialvalue=graph_types[0])
       if choice in graph_types:
           new_graph = Graph(self.graph_area, f"New {choice}", choice, self.update_dynamic_graphs)
           row = len(self.graphs) // 2
           col = len(self.graphs) % 2
           new_graph.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
           self.graphs.append(new_graph)


   def update_dynamic_graphs(self):
       for fig, ax, canvas in self.dynamic_graphs:
           ax.clear()
           x = np.linspace(0, 10, 100)
           y = np.sin(x + random.random())
           ax.plot(x, y)
           canvas.draw()


   def update_all_graphs(self):
       for graph in self.graphs:
           graph.update_data()
       self.update_dynamic_graphs()


   def account_control(self):
       # Placeholder for account control functionality
       print("Account Control clicked")


def run_with_xvfb():
   try:
       # Try to create the Tk root window
       root = tk.Tk()
       root.destroy()  # If successful, destroy it and proceed normally
       print("Display available. Running normally.")
       app = Dashboard()
       app.mainloop()
   except tk.TclError:
       print("No display found. Attempting to run with Xvfb.")
       try:
           # Start Xvfb
           xvfb_process = subprocess.Popen(['Xvfb', ':99'])
           os.environ['DISPLAY'] = ':99'
           time.sleep(1)  # Give Xvfb a moment to start


           # Now try to run the dashboard
           app = Dashboard()
           app.mainloop()
       finally:
           # Clean up Xvfb process
           if 'xvfb_process' in locals():
               xvfb_process.terminate()
               xvfb_process.wait()


if __name__ == "__main__":
   run_with_xvfb()

