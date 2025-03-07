import sqlite3
import requests
from datetime import datetime

API_KEY = "YOUR_API_KEY"
CITY = "Kyiv"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        datetime TEXT,
        temperature REAL
    )
''')

response = requests.get(URL)
data = response.json()
temperature = data["main"]["temp"]

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute("INSERT INTO weather (datetime, temperature) VALUES (?, ?)", (now, temperature))

conn.commit()
conn.close()

print(f"Дані збережено: {now} - {temperature}°C")
