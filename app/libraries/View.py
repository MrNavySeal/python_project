import os
import importlib
class View():
    def __init__(self,controller):
        self.__controller = controller
    def get_view(self,view,root=None,data=""):
        path = f"./app/Views/{ self.__controller}"
        if (os.path.exists(path)):
            view_path = f"./app/Views/{ self.__controller}/{view}.py"
            if (os.path.exists(view_path)):
                import_path = f"app.Views.{ self.__controller}.{view}"
                module = importlib.import_module(import_path)
                ViewClass = getattr(module,view)
                return ViewClass(root,data)
            else:
                raise Exception(f"The {view} view doesn't exist")
        else:
            raise Exception(f"The { self.__controller} folder doesn't exist in Views folder")