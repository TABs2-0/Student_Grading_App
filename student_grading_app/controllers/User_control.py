# this file will store majority of user related functions
from student_grading_app.models import User
class UserControl:
    def __init__(self) :
        super.__init__(self)
        
        
    def FetchUser(self,username,password):    # this is the controller form of FectUserrole in models
        return  self.User.UserModel.Fetchuserrole(username,password)
