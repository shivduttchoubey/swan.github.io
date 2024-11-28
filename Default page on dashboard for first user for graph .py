import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class ResizableGraphFrame(ttk.Frame):
   def __init__(self, parent, figure, *args, **kwargs):
       super().__init__(parent, *args, **kwargs)
      
       # Canvas to embed the matplotlib figure
       self.canvas = FigureCanvasTkAgg(figure, self)
       self.canvas_widget = self.canvas.get_tk_widget()
       self.canvas_widget.pack(fill=tk.BOTH, expand=True)


       # Resize handle at the bottom-right corner
       self.resizer = ttk.Sizegrip(self)
       self.resizer.place(relx=1.0, rely=1.0, anchor='se')


       # Bind the resize event
       self.bind("<Configure>", self.on_resize)
      
   def on_resize(self, event):
       width = self.winfo_width()
       height = self.winfo_height()
       self.canvas_widget.config(width=width, height=height)
       self.canvas.draw()


class GraphPanelApp:
   def __init__(self, root):
       self.root = root
       self.root.title("Resizable Graphs")


       # Main container for graphs
       self.graphs_frame = ttk.Frame(root)
       self.graphs_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


       # Create and display the graphs
       self.create_graphs()


   def create_graphs(self):
       for i in range(4):  # Number of graphs (4)
           fig = plt.Figure(figsize=(5, 4))
           ax = fig.add_subplot(111)
           x = np.linspace(0, 10, 100)
           y = np.sin(x) * (i + 1)
           ax.plot(x, y)
           ax.set_title(f"Graph {i + 1}")


           # Create resizable frame for each graph
           resizable_frame = ResizableGraphFrame(self.graphs_frame, fig)
           resizable_frame.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="nsew")


           # Configure this frame to be resizable independently
           resizable_frame.grid_rowconfigure(0, weight=1)
           resizable_frame.grid_columnconfigure(0, weight=1)


           # Make the main frame rows and columns resizable
           self.graphs_frame.grid_rowconfigure(i//2, weight=1)
           self.graphs_frame.grid_columnconfigure(i%2, weight=1)


if __name__ == "__main__":
   root = tk.Tk()
   root.geometry("800x600")
   app = GraphPanelApp(root)
   root.mainloop()




