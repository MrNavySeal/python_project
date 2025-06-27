from  app.Libraries.Mysql import Mysql

class UserModel(Mysql):
    def __init__(self):
        super().__init__()
        self.__id = None
        self.__name = None
        self.__email = None
        self.__password = None
    def find(self,id):
        sql = "select * from users where id = %s"
        request = super().find(sql,[id])
        return request
    def all(self):
        sql = "select * from users"
        request = super().all(sql)
        return request
    def create(self,name,email,password):
        self.__name = name
        self.__email = email
        self.__password = password
        sql = "insert into users(name,email,password) values(%s,%s,%s)"
        request = super().create(sql,[self.__name,self.__email,self.__password])
        return request
    def update(self,id,name,email,password):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__password = password
        sql = "update users set name=%s,email=%s,password=%s where id = %s"
        request = super().update(sql,[self.__name,self.__email,self.__password,self.__id])
        return request
    def destroy(self,id):
        self.__id = id
        sql = "delete from users where id = %s"
        request = super().destroy(sql,[self.__id])
        return request