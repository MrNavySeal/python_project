from Conexion import Conexion
class Mysql(Conexion):
    def __init__(self):
        self.__connection = Conexion().getConnection()
        print(self.__connection)
    def find(self,query):
        cursor = self.__connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    def all(self,query):
        cursor = self.__connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        return result

print(Mysql().find("SELECT * FROM humnomina")['id_nom'])