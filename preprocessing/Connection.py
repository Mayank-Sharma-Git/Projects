import mysql.connector


class DBConnect:
    
    def getconnection():
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port = 3306,
            user = "root",
            database = "SalesReport",
            password = "1234"
            )
        
       
        return conn



    


























