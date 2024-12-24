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
    
    def getPurseWithLink(self, link):
        self.cursor.execute(f"SELECT * from purses WHERE link=\'{link}\';")
        record = self.cursor.fetchall()
        return record
    
    def getLatestPurseID(self):
        statement = f"SELECT * FROM purses ORDER BY id DESC LIMIT 1;"
        self.cursor.execute(statement)
        record = self.cursor.fetchall()
        return record
    
    def getPrices(self):
        self.cursor.execute(f"SELECT * from prices;")
        record = self.cursor.fetchall()
        return record


    def getPricesWithID(self, id):
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

    def addPurse(self, id, name, link):
        statement = f"INSERT INTO purses (id, name, link) VALUES ({id},\'{name}\',\'{link}\');" 
        self.cursor.execute(statement)
        self.connection.commit()
        