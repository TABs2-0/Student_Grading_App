import sqlite3
import traceback
from student_grading_app import view


class AdminModel:
    def __init__(self):

        self.conn = sqlite3.connect('../../sg.db')  #the ../  indicates that sg is out of our sub and main directory

    def read_csv_or_excel(self):
        pass

    def publish_result(self):
        pass


    def add_student(self):
        pass

    def __del__(self):
        if self.conn:
            self.conn.close()

    def fetch_each_level_course(self):
        # REMEMBER TO CONSIDER YR LEVEL DASHBORD AS A 2D ARRAY SUCH THAT TO KNOW WHICH SUBJECT  SHOULD BE DISPLAY
        # JUST CHECK THE SEMESTER INDEX
        pass