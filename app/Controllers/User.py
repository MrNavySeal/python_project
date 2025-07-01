from app.Libraries.Controller import Controller
class User(Controller):
    def __init__(self,root=None):
        self.__root = root
        super().__init__(self.__class__.__name__)
    def show(self):
        data = {"title":"Users"}
        view = super().view().get_view("Show",data=data,root=self.__root)
        return view.get_frame()
    def save(self,name,email,password):
        request = self.model().create(name,email,password)
        if request > 0:
            return "New user created successfully"
        else:
            return "It has ocurred an error, try again."
    def get_users(self):
        return self.model().all()

