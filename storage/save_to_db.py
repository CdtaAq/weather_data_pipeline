import sqlite3
from utils.logger import get_logger

logger = get_logger()

def save_to_db(data):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                        city TEXT, 
                        temperature REAL, 
                        humidity INTEGER, 
                        weather TEXT
                      )''')
    cursor.execute('INSERT INTO weather VALUES (?, ?, ?, ?)',
                   (data['city'], data['temperature'], data['humidity'], data['weather']))
    conn.commit()
    conn.close()
    logger.info("Data saved to database.")
