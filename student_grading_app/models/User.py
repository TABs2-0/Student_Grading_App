import sqlite3


class UserModel:
    def __init__(self):
        self.conn = sqlite3.connect('../../sg.db')

    def fetchuserrole(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT role FROM users WHERE user_name=? AND password=?""", (username, password))
        user_db_role = cursor.fetchone()  # this attribute is needed to store the username and pass from our db
        print(f"User_db_role all >>> {user_db_role}")
        return user_db_role
