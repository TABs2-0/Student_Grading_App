import sqlite3


class UserModel:
    def __init__(self):
        self.conn = sqlite3.connect('../../sg.db')
        self.create_table()

    def fetchuserrole(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT role FROM users WHERE username=? AND password=?""", (username, password))
        user_db_role = cursor.fetchone()  # this attribute is needed to store the username and pass from our db
        print(f"User_db_role all >>> {user_db_role}")
        return user_db_role

    def create_table(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id  INTEGER PRIMARY KEY,
        user_name TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role NOT NULL CHECK (role in("lecturer","Admin","student"))
      
        );
         """)
