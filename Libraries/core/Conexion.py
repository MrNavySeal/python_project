
import sys
from pathlib import Path
project_root = Path(__file__).parent.parent.parent  # Adjust based on your actual structure
sys.path.append(str(project_root))
from config import DB_CONFIG
import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        strBase = DB_CONFIG['database']
        strUserName = DB_CONFIG['user']
        strHostName = DB_CONFIG['host']
        strPassword = DB_CONFIG['password']
        intPort =DB_CONFIG['port']
        try:
            __connection= mysql.connector.connect(
                host = DB_CONFIG['host'],
                database = DB_CONFIG['database'],
                user = DB_CONFIG['user'],
                password = DB_CONFIG['password'],
                port =DB_CONFIG['port']
            )
            if __connection.is_connected():
                info = __connection.server_info
                print(f"Conexion succesfull {info}")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
Conexion()