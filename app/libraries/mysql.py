from app.Libraries.Conexion import Conexion
class Mysql:
    def __init__(self):
        self.__connection = Conexion().getConnection()
    def find(self,query,params=[]):
        cursor = self.__connection.cursor(dictionary=True)
        cursor.execute(query,params)
        result = cursor.fetchone()
        return result
    def all(self,query,params=[]):
        cursor = self.__connection.cursor(dictionary=True)
        cursor.execute(query,params)
        result = cursor.fetchall()
        return result
    def create(self,query,params):
        cursor = self.__connection.cursor()
        cursor.execute(query,params)
        self.__connection.commit()
        result = cursor.lastrowid
        return result
    def update(self,query,params):
        cursor = self.__connection.cursor()
        cursor.execute(query,params)
        self.__connection.commit()
        result = cursor.rowcount
        return result
    def destroy(self,query,params=[]):
        cursor = self.__connection.cursor()
        cursor.execute(query,params)
        self.__connection.commit()
        result = cursor.rowcount
        return result