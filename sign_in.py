import tkinter as tk
from tkinter import messagebox

def google_sign_in():
    # Placeholder function for Google Sign-In
    messagebox.showinfo("Google Sign-In", "Redirecting to Google Sign-In...")

def about_project():
    # Function to show project details
    messagebox.showinfo(
        "About Project",
        "This project provides customizable dashboards for IoT data visualization with real-time updates and various graphing options.",
    )

# Initialize Tkinter Window
root = tk.Tk()
root.title("IoT Dashboard Landing Page")
root.geometry("800x500")  # Width x Height
root.configure(bg="#f5f5f5")

# Header Section
header = tk.Label(
    root,
    text="Welcome to the IoT Dashboard",
    font=("Helvetica", 24, "bold"),
    bg="#f5f5f5",
    fg="#333333",
)
header.pack(pady=20)

# Description Section
description = tk.Label(
    root,
    text=(
        "Monitor and visualize your IoT data in real-time.\n"
        "Customize your dashboard with flexible graphs and layouts."
    ),
    font=("Helvetica", 14),
    bg="#f5f5f5",
    fg="#555555",
    justify="center",
)
description.pack(pady=10)

# Buttons Section
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=40)

google_button = tk.Button(
    button_frame,
    text="Sign in with Google",
    font=("Helvetica", 14),
    bg="#4285F4",
    fg="white",
    activebackground="#357ae8",
    activeforeground="white",
    padx=20,
    pady=10,
    command=google_sign_in,
)
google_button.grid(row=0, column=0, padx=20)

about_button = tk.Button(
    button_frame,
    text="About the Project",
    font=("Helvetica", 14),
    bg="#34A853",
    fg="white",
    activebackground="#2c8c45",
    activeforeground="white",
    padx=20,
    pady=10,
    command=about_project,
)
about_button.grid(row=0, column=1, padx=20)

# Footer Section
footer = tk.Label(
    root,
    text="© 2024 IoT Dashboard Project",
    font=("Helvetica", 10),
    bg="#f5f5f5",
    fg="#777777",
)
footer.pack(side="bottom", pady=20)

# Run the Tkinter Main Loop
root.mainloop()
