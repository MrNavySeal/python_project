from app.libraries.conexion import Conexion
class Mysql(Conexion):
    def __init__(self):
        self.__connection = Conexion().getConnection()
    def find(self,query,params=[]):
        result = "The statement is incorrect for this method"
        if "SELECT" in query:
            cursor = self.__connection.cursor(dictionary=True)
            cursor.execute(query,params)
            result = cursor.fetchone()
        return result
    def all(self,query,params=[]):
        result = "The statement is incorrect for this method"
        if "SELECT" in query:
            cursor = self.__connection.cursor(dictionary=True)
            cursor.execute(query,params)
            result = cursor.fetchall()
        return result
    def create(self,query,params):
        result = "The statement is incorrect for this method"
        cursor = self.__connection.cursor()
        cursor.execute(query,params)
        self.__connection.commit()
        result = cursor.lastrowid
        return result
    def update(self,query,params):
        result = "The statement is incorrect for this method"
        if "UPDATE" in query:
            cursor = self.__connection.cursor()
            cursor.execute(query,params)
            self.__connection.commit()
            result = cursor.rowcount
        return result
    def destroy(self,query,params=[]):
        result = "The statement is incorrect for this method"
        if "DELETE" in query:
            cursor = self.__connection.cursor()
            cursor.execute(query,params)
            self.__connection.commit()
            result = cursor.rowcount
        return result
print(Mysql().find("SELECT * FROM humnomina"))