import tkinter as ttk
import ttkbootstrap as ttk 
from app.Controllers.User import User
class Show():
    def __init__(self,root,data=""):
        self.__frame = ttk.Frame(root)
        
        ttk.Label(self.__frame, text=data["title"], font=("Arial", 20)).pack(pady=20)
        
        label_name = ttk.Label(self.__frame,text="Name")
        label_email = ttk.Label(self.__frame,text="Email")
        label_password = ttk.Label(self.__frame,text="Passowrd")
        self.__name = ttk.Entry(self.__frame)
        self.__email = ttk.Entry(self.__frame)
        self.__password = ttk.Entry(self.__frame)
        self.__result = ""
        self.__label_result = ttk.Label(self.__frame, text="Result: ",textvariable=self.__result,font=("Arial", 20))
        btn_save = ttk.Button(self.__frame,text="Save",command=self.test)
        label_name.pack()
        self.__name.pack()
        label_email.pack()
        self.__email.pack()
        label_password.pack()
        self.__password.pack()
        btn_save.pack()
        self.__label_result.pack()
        
    def test(self):
        self.__result=  User().save(self.__name.get(),self.__email.get(),self.__password.get())
        self.__label_result.config(text=self.__result)

    def get_frame(self):
        return self.__frame
        
        