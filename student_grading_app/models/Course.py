import sqlite3
import traceback
from sqlite3 import *


class CourseModel:

    def add_course(self, course_code, course_name, lecturer_id, level, semester):
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute(f'''INSERT INTO Courses(course_code,course_name,lecturer_id,level,semester) VALUES(?,?,?,?,?)''',
                       (course_code, course_name, lecturer_id, level,
                        semester))  # this insertion format helps protect the system from sqlinjection Attackd
        conn.commit()
        conn.close()

    def delete_a_course(self, course_code):
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute(f''' DELETE  FROM Courses WHERE course_code=?''', (course_code,))
        conn.commit()
        conn.close()

    def update_a_course(self, course_code, course_name, lecturer_id, level, semester):
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE Courses 
        SET course_name=?,lecturer_id=?,level=?,semester=? WHERE course_code=?
        ''', (course_name, lecturer_id, level, semester, course_code))
        conn.commit()
        conn.close()

    def get_course_names(self):
        self.cursor.execute(''' SELECT course_name FROM Courses ''')

        courses = self.cursor.fetchall()
        return [course[0] for course in courses]

    def fetch_courses_from_name(self, course_name):
        try:
            conn = sqlite3.connect('../../sg.db')
            cursor = conn.cursor()
            #the JOIN stetement makes a bridge to the Lecturers Table
            cursor.execute('''
                    SELECT c.course_name, c.course_code,l.lecturer_name 
                    FROM Courses c
                    JOIN Lecturers l ON c.lecturer_id=l.lecturer_id
                    WHERE c.course_name=?
                    
                ''', (course_name,))
            courses = cursor.fetchone()
            conn.close()
            return courses
        except sqlite3.Error as e:
            print(f"An SQLite error occurred: {e}")
            traceback.print_exc()

    def fetch_course_from_name(self):
        try:
            conn = sqlite3.connect('../../sg.db')
            cursor = conn.cursor()
            # the JOIN stetement makes a bridge to the Lecturers Table
            cursor.execute('''
                          SELECT course_name FROM Courses

                       ''')
            courses = cursor.fetchall()
            conn.close()
            return [course[0] for course in courses]
        except sqlite3.Error as e:
            print(f"An SQLite error occurred: {e}")
            traceback.print_exc()
