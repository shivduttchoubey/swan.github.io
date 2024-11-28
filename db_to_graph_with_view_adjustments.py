# Creating Graph from Database


import sqlite3
import os
from datetime import datetime
import random
import pandas as pd
import matplotlib.pyplot as plt


# Step 1: Create a folder and database, then insert sensor data
os.makedirs('sensor_data', exist_ok=True)
conn = sqlite3.connect('sensor_data/sensor_data.db')
c = conn.cursor()


c.execute('''
   CREATE TABLE IF NOT EXISTS sensor_readings (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       timestamp TEXT,
       sensor_id TEXT,
       value REAL
   )
''')


for i in range(10):
   sensor_id = f"sensor_{i%3}"
   value = random.uniform(20.0, 30.0)
   timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   c.execute("INSERT INTO sensor_readings (timestamp, sensor_id, value) VALUES (?, ?, ?)",
             (timestamp, sensor_id, value))


conn.commit()
conn.close()


# Step 2: Read the data from the database
conn = sqlite3.connect('sensor_data/sensor_data.db')
df = pd.read_sql_query("SELECT * FROM sensor_readings", conn)
conn.close()


print(df)


# Step 3: Plot the data using matplotlib
for sensor_id in df['sensor_id'].unique():
   sensor_data = df[df['sensor_id'] == sensor_id]
   plt.plot(sensor_data['timestamp'], sensor_data['value'], label=sensor_id)


plt.xlabel('Timestamp')
plt.ylabel('Sensor Value')
plt.title('Sensor Readings Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# focus on the options given below

