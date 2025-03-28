import mysql.connector

def get_connection():
    return mysql.connector.connect (
        host = "localhost",
        user = "root",
        password = "",
        database = "clothesdb",
        port = 3306
    )