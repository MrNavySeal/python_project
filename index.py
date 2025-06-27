import tkinter as tk
from tkinter import ttk

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        self.geometry("1024x768")
        
        # Create a container frame for sub-views
        self.container_frame = ttk.Frame(self)
        self.container_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Status bar
        self.status_bar = ttk.Label(self, text="Ready", relief=tk.SUNKEN)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
    
    def set_status(self, message):
        self.status_bar.config(text=message)

    def run(self):
        self.mainloop()

MainView().run()