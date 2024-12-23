import psycopg2
import info

class DB:
    global connection
    def __init__(self):
        self.connection = info.getConnection()
        cursor = self.connection.cursor()

        cursor.execute("SELECT * from purses;")
        # Fetch all rows from database
        record = cursor.fetchall()
        print("Data from Database:- ", record)

    
    def getPrices(self, id):
        self.cursor.execte("SELECT * from prices WHERE id=" + id)
        record = self.cursor.fetchall()
        print("Data from Database:- ", record)
        return record