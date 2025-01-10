import sqlite3


class LecturerModel:
    def __init__(self):
        super().__init__()

    def get_lecturer_courses(self, lecturer_name):
        conn = sqlite3.connect('../../sg.db')  # move two directories ouut to get yr db
        cursor = conn.cursor()
        cursor.execute('''
        SELECT c.course_name FROM Courses c 
        JOIN Lecturers l ON c.lecturer_id=l.lecturer_id
        WHERE l.lecturer_name=?
        ''', (lecturer_name,))
        Ls = cursor.fetchall()
        conn.commit()
        conn.close()
        return Ls

    def Get_Lecturer_Id(self, name):
        conn = sqlite3.connect('../../sg.db')  # move two directories ouut to get yr db
        cursor = conn.cursor()
        cursor.execute('''
                SELECT lecturer_id FROM Lecturers WHERE lecturer_name=?
                ''', (name,))
        Ls = cursor.fetchall()
        conn.commit()
        conn.close()
        return Ls
#L = LecturerModel()
#L.get_lecturer_courses("John Smith")
