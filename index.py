import tkinter as tk
from tkinter import ttk
from app.Controllers.User import User
class Main():
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title("Demo")
        self.__window.geometry("800x600")
        User().show().pack(fill="both", expand=True)

    def render(self):
        self.__window.mainloop()

Main().render()
