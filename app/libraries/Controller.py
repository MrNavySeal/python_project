import os
import importlib
from app.Libraries.View import View
class Controller:
    def __init__(self,controller):
        self.__model=""
        self.__view = View(controller)
        controller_path = f"./app/Controllers/{controller}.py"
        if (os.path.exists(controller_path)):
            model_name = controller+"Model"
            model_path = f"./app/Models/{model_name}.py"
            if(os.path.exists(model_path)):
                import_path = f"app.Models.{model_name}"
                module = importlib.import_module(import_path) #Import dynamically models regarding controller
                ModelClass = getattr(module,model_name)
                self.__model = ModelClass()
        else:
            raise Exception(f"The {controller} controller  doesn't exist")
    def view(self):
        return self.__view
    def model(self):
        return self.__model
        
