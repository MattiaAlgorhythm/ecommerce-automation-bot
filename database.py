# database.py
import sqlite3

def create_connection():
    conn = sqlite3.connect("orders.db")
    return conn
    
def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        customer_name TEXT,
        product_name TEXT,
        quantity INTEGER,
        status TEXT,
        tracking_number TEXT
    )''')
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    initialize_database()