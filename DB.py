import psycopg2
import info
from datetime import date
import datetime

class DB:
    def __init__(self):
        self.connection = info.getConnection()
        self.cursor = self.connection.cursor()

    def getPurses(self):
        self.cursor.execute("SELECT * from purses;")
        record = self.cursor.fetchall()
        return record


    def getPrices(self, id):
        self.cursor.execute(f"SELECT * from prices WHERE id={id};")
        record = self.cursor.fetchall()
        return record
    
    def getLatestPrice(self, id):
        statement = f"SELECT * FROM prices WHERE id={id} ORDER BY date DESC LIMIT 1;"
        self.cursor.execute(statement)
        record = self.cursor.fetchall()
        return record
        
    
    def addPrice(self, id, p):
        d = date.today()
        statement = f"INSERT INTO prices (id, price, date) VALUES ({id},{p},DATE(\'{d}\'));" 
        self.cursor.execute(statement)
        self.connection.commit()
        