import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # For Google Sign-In button image (optional)

class UserAuthenticationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Authentication")
        self.root.geometry("400x300")

        # Title
        tk.Label(self.root, text="Welcome to the Dashboard", font=("Arial", 16)).pack(pady=10)

        # Google Sign-In Button
        self.google_button = tk.Button(
            self.root, 
            text="Sign In with Google", 
            bg="#4285F4", fg="white", 
            font=("Arial", 12), 
            command=self.google_sign_in
        )
        self.google_button.pack(pady=10)

        # Divider
        ttk.Separator(self.root, orient="horizontal").pack(fill="x", pady=10)

        # Personalized Settings Area (hidden initially)
        self.settings_frame = tk.Frame(self.root)
        self.settings_frame.pack(pady=10, fill="x")

        tk.Label(self.settings_frame, text="Personalized Settings", font=("Arial", 14)).pack(pady=5)

        self.user_name_label = tk.Label(self.settings_frame, text="Name: ", font=("Arial", 12))
        self.user_name_label.pack(pady=2)

        self.user_email_label = tk.Label(self.settings_frame, text="Email: ", font=("Arial", 12))
        self.user_email_label.pack(pady=2)

        self.logout_button = tk.Button(
            self.settings_frame, 
            text="Logout", 
            bg="red", fg="white", 
            font=("Arial", 12), 
            command=self.logout
        )
        self.logout_button.pack(pady=10)

        # Hide settings frame initially
        self.settings_frame.pack_forget()

    def google_sign_in(self):
        # Simulated Google Sign-In (replace with actual OAuth flow in production)
        user_name = "Shiv Dutt Choubey"
        user_email = "shiv.dutt.choubey@example.com"

        # Simulate success
        messagebox.showinfo("Sign-In Successful", f"Welcome, {user_name}!")
        self.display_settings(user_name, user_email)

    def display_settings(self, name, email):
        # Show personalized settings
        self.settings_frame.pack(pady=10, fill="x")
        self.google_button.pack_forget()  # Hide the sign-in button

        self.user_name_label.config(text=f"Name: {name}")
        self.user_email_label.config(text=f"Email: {email}")

    def logout(self):
        # Simulate logout
        self.settings_frame.pack_forget()  # Hide settings
        self.google_button.pack(pady=10)  # Show sign-in button again
        messagebox.showinfo("Logged Out", "You have been logged out successfully.")

# Initialize
root = tk.Tk()
UserAuthenticationApp(root)
root.mainloop()
