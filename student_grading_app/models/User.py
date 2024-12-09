import sqlite3


class UserModel:
    def __init__(self, user_name, password, status):
        self.user_name = user_name
        self.password = password
        self.status = status

    def Fetchuserrole(self, username, password):
        con = sqlite3.connect(self.sg.db)
        cursor = con.cursor()
        cursor.execute("""SELECT role FROM users WHERE user_name=? AND password=?""", (username, password))
        user_db_role = cursor.fetchone  #this attributeis needed to store the user nameand pass from our db
        return user_db_role
