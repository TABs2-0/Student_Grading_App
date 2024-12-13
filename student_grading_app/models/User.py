import sqlite3
import traceback


class UserModel:
    def __init__(self):
        self.conn = sqlite3.connect('../../sg.db')

    def fetchuserrole(self, username, password):
        try:
            cursor = self.conn.cursor()

            cursor.execute("""SELECT role FROM Users WHERE  user_name==? AND password==?""", (username, password))
            user_db_role = cursor.fetchone()  # this attribute is needed to store the username and pass from our db
            print(f"User_db_role all >>> {user_db_role}")
            return user_db_role
        except sqlite3.Error as e:
            print(f"An SQLite error occurred: {e}")  # Print detailed traceback information
            traceback.print_exc()
        finally:
            if self.conn:
                self.conn.close()

