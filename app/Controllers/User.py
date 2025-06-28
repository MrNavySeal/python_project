from app.Libraries.Controller import Controller
class User(Controller):
    def __init__(self,root=None):
        self.__root = root
        super().__init__(self.__class__.__name__)
    def show(self):
        data = {"title":"Users"}
        view = super().view().get_view("Show",data=data,root=self.__root)
        return view.get_frame()
