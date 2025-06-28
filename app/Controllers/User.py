from app.Libraries.Controller import Controller
class User(Controller):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    def show(self):
        data = {"title":"Users"}
        view = super().view().get_view("Show",data)
        return view.get_frame()

#print(User().show())