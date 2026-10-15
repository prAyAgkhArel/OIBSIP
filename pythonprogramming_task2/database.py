import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="bmi_records.db"):
        self.db_name = db_name
        self.create_table()
        
    def connect(self):
        return sqlite3.connect(self.db_name)
    
    def create_table(self):
        try:
            with self.connect() as connection:
                cursor = connection.cursor()
                
                cursor.execute(
                    '''
                    CREATE TABLE IF NOT EXISTS bmi_records(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        weight REAL NOT NULL,
                        height REAL NOT NULL,
                        bmi REAL NOT NULL,
                        category TEXT NOT NULL,
                        date TEXT NOT NULL
                    )
                    '''
                )
                connection.commit()
        except sqlite3.Error as error:
            print(f"Database Error {error}")
    
    def save_record(self, name, weight, height, bmi, category):
        try:
            with self.connect() as connection:
                cursor = connection.cursor()
                
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                cursor.execute(
                    '''
                    INSERT INTO bmi_records
                    (name, weight, height, bmi, category, date)
                    VALUES(?, ?, ?, ?, ?, ?)
                    ''', (name, weight, height, bmi, category, date)
                    
                )
                connection.commit()
        except sqlite3.Error as error:
            raise Exception(f"Unable to save BMI record. {error}")  
        
    
    def get_user_history(self, name):
        try:
            with self.connect() as connection:
                cursor = connection.cursor()
                
                cursor.execute(
                    '''
                    SELECT date, bmi
                    FROM bmi_records
                    WHERE name = ?
                    ORDER BY id
                    ''',(name,)
                    )   
                return cursor.fetchall()
        except sqlite3.Error as error:
            raise Exception (f"Unable to read BMI history: {error}")