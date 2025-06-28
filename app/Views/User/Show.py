from tkinter import ttk

class Show():
    def __init__(self,root,data=""):
        self.__frame = ttk.Frame(root)
        ttk.Label(self.__frame, text=data["title"], font=("Arial", 20)).pack(pady=20)
    def get_frame(self):
        return self.__frame
        
        