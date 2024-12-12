# this file will store majority of user related functions

from student_grading_app.models.User import UserModel


class Usercontrol:
    def __init__(self):
        self.model = UserModel()

    def fetchrole(self, username, password):  # this is the controller form of FectUserrole in models
        return self.model.fetchuserrole(username, password)
