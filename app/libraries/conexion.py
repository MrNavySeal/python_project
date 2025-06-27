
from config.settings import DB_CONFIG
import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        try:
            self.__connection= mysql.connector.connect(
                host = DB_CONFIG['host'],
                database = DB_CONFIG['database'],
                user = DB_CONFIG['user'],
                password = DB_CONFIG['password'],
                port =DB_CONFIG['port']
            )
            if self.__connection.is_connected():
                info = self.__connection.server_info
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
    def getConnection(self):
        return self.__connection