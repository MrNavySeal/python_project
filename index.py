import tkinter as tk
from tkinter import ttk
from app.Controllers.User import User
class Main():
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title("Demo")
        self.__window.geometry("800x600")
        User(self.__window).show().pack(fill="both", expand=True)
    def render(self):
        self.__center_window(width=1024,height=700)
        self.__window.mainloop()
    def __center_window(self, width=800, height=600):
        screen_width = self.__window.winfo_screenwidth()
        screen_height = self.__window.winfo_screenheight()
        x = int((screen_width  - width )/2)
        y = int((screen_height - height)/2)
        self.__window.geometry(f"{width}x{height}+{x}+{y}")


Main().render()
