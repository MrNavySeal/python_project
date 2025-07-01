import tkinter as ttk
import ttkbootstrap as ttk 
from app.Controllers.User import User
class Show():
    def __init__(self,root,data=""):
        
        self.__frame = ttk.Frame(root)
        ttk.Label(self.__frame, text=data["title"], font=("Arial", 20)).pack(pady=20)

        self.__result = ""
        label_name = ttk.Label(self.__frame,text="Name")
        label_email = ttk.Label(self.__frame,text="Email")
        label_password = ttk.Label(self.__frame,text="Password")
        self.__name = ttk.Entry(self.__frame)
        self.__email = ttk.Entry(self.__frame)
        self.__password = ttk.Entry(self.__frame)
        btn_save = ttk.Button(self.__frame,text="Save",command=self.save)
        self.__label_result = ttk.Label(self.__frame, text="",textvariable=self.__result,font=("Arial", 20))
        self.__table = ttk.Treeview(self.__frame,columns=("Name","Email","Options"),show="headings")
        self.__table.heading("Name",text="Name")
        self.__table.heading("Email",text="Email")
        self.__table.heading("Options",text="Options")
        
        self.get_users()

        label_name.pack()
        self.__name.pack()
        label_email.pack()
        self.__email.pack()
        label_password.pack()
        self.__password.pack()
        btn_save.pack()
        self.__label_result.pack()
        self.__table.pack()

    def get_users(self):
        for item in self.__table.get_children():
            self.__table.delete(item)
        
        arr_users = User().get_users()
        for user in arr_users:
            self.__table.insert(parent="",index=0,values=(user['name'],user['email'],""))
        
    def save(self):
        self.__result=  User().save(self.__name.get(),self.__email.get(),self.__password.get())
        self.__label_result.config(text=self.__result)
        self.get_users()

    def get_frame(self):
        return self.__frame
        
        