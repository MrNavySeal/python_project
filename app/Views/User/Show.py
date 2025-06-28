import tkinter as tk

class Show():
    def __init__(self,root,data=""):
        self.__frame = tk.Frame(root)
        tk.Label(self.__frame, text=data["title"], font=("Arial", 20)).pack(pady=20)
        tk.Button(self.__frame, text="Submit", command=lambda: print("Submit logic")).pack()
    def get_frame(self):
        return self.__frame
        
        