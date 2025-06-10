import tkinter as tk
from tkinter import messagebox, ttk
import paho.mqtt.client as mqtt
import json
from datetime import datetime
import threading
import os

class MQTTLogger:
    def __init__(self, master):
        self.master = master
        master.title("MQTT Data Logger")
        master.geometry("800x600")

        # Broker Input
        tk.Label(master, text="MQTT Broker Address:").pack()
        self.broker_entry = tk.Entry(master, width=50)
        self.broker_entry.pack()
        self.broker_entry.insert(0, "localhost")

        # Port Input
        tk.Label(master, text="Port:").pack()
        self.port_entry = tk.Entry(master, width=50)
        self.port_entry.pack()
        self.port_entry.insert(0, "1883")

        # Topic Input
        tk.Label(master, text="Topic to Subscribe:").pack()
        self.topic_entry = tk.Entry(master, width=50)
        self.topic_entry.pack()

        # File Name Input
        tk.Label(master, text="JSON File Name:").pack()
        self.file_entry = tk.Entry(master, width=50)
        self.file_entry.pack()
        self.file_entry.insert(0, "mqtt_data")

        # Buttons Frame
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        # Connect Button
        self.connect_btn = tk.Button(button_frame, text="Connect & Subscribe", command=self.start_mqtt)
        self.connect_btn.pack(side=tk.LEFT, padx=5)

        # Show Data Button
        self.show_data_btn = tk.Button(button_frame, text="Show Stored Data", command=self.show_stored_data)
        self.show_data_btn.pack(side=tk.LEFT, padx=5)

        # Data Display
        self.tree = ttk.Treeview(master, columns=('Time', 'Message'), show='headings')
        self.tree.heading('Time', text='Time')
        self.tree.heading('Message', text='Message')
        self.tree.column('Time', width=200)
        self.tree.column('Message', width=500)
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

        # Scrollbar for Treeview
        scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscroll=scrollbar.set)

        # Text widget for logging
        self.log_text = tk.Text(master, height=5, width=80)
        self.log_text.pack(padx=10, pady=10)

        # MQTT Client
        self.client = None
        self.data_lock = threading.Lock()

    def log(self, message):
        # Log messages to the text widget
        self.log_text.insert(tk.END, str(message) + "\n")
        self.log_text.see(tk.END)

    def save_to_json(self, timestamp, message):
        # Get file name
        filename = f"{self.file_entry.get()}_data.json"
        
        # Ensure thread-safe file writing
        with self.data_lock:
            # Try to read existing data
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                data = []
            
            # Append new message
            data.append({
                'timestamp': timestamp,
                'message': message
            })
            
            # Write back to file
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)

    def start_mqtt(self):
        # Get input values
        broker = self.broker_entry.get()
        port = int(self.port_entry.get())
        topic = self.topic_entry.get()

        # Validate inputs
        if not (broker and topic):
            messagebox.showerror("Error", "Please fill all fields")
            return

        try:
            # Setup MQTT Client
            self.client = mqtt.Client()
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message

            # Connect to broker
            self.client.connect(broker, port, 60)

            # Start MQTT loop in a thread
            mqtt_thread = threading.Thread(target=self.client.loop_start)
            mqtt_thread.daemon = True
            mqtt_thread.start()

            self.log(f"Connected to broker {broker} on port {port}")
            self.log(f"Subscribed to topic: {topic}")
            messagebox.showinfo("Success", "Connected to MQTT Broker!")

        except Exception as e:
            self.log(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))

    def on_connect(self, client, userdata, flags, rc):
        topic = self.topic_entry.get()
        client.subscribe(topic)
        self.log(f"Connected with result code {rc}")
        self.log(f"Subscribed to {topic}")

    def on_message(self, client, userdata, msg):
        # Get current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Decode message
        try:
            # Try to parse as JSON first
            message = msg.payload.decode('utf-8')
        except Exception as e:
            # If decoding fails, use raw payload
            message = str(msg.payload)

        self.log(f"Received message: {message}")
        
        # Save to JSON
        self.save_to_json(timestamp, message)

        # Update treeview in main thread
        self.master.after(0, self.update_treeview, timestamp, message)

    def update_treeview(self, timestamp, message):
        # Update treeview with new message
        self.tree.insert('', 'end', values=(timestamp, message))

    def show_stored_data(self):
        # Clear existing items
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Get filename
        filename = f"{self.file_entry.get()}_data.json"

        try:
            # Read JSON file
            with open(filename, 'r') as f:
                data = json.load(f)

            self.log(f"Retrieved {len(data)} records from JSON")

            # Populate treeview
            for item in data:
                self.tree.insert('', 'end', 
                                 values=(item['timestamp'], item['message']))

        except FileNotFoundError:
            self.log("No data file found")
        except Exception as e:
            self.log(f"Error retrieving data: {str(e)}")
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = MQTTLogger(root)
    root.mainloop()

if __name__ == "__main__":
    main()