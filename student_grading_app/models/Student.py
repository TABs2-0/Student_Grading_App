import sqlite3


class StudentModel:

    def checkdepartment(self, department):  # this function makes sure that a corect departement is selected
        if self.department.upper() not in ['ICT', 'BMS']:
            raise ValueError(" Select a valuable department ")

    import sqlite3

    def add_student(self, id, matricule, name, semester, level, phone, gender, address, email):
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute('''
                INSERT INTO Students (student_id, matriculation_id, name, semester, level, email, phone, gender, address) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (id, matricule, name, semester, level, email, phone, gender.strip().lower(),
                  address))  #strip.lower einsures that the choice will be in lower case
        conn.commit()
        conn.close()

    def update_student(self, student_id, new_semester, new_level, new_email, new_phone, new_address):
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute('''
                         UPDATE Students 
                         SET semester=?,level=?,email=?, phone=?,address=? WHERE student_id=?
                        ''', (new_semester, new_level, new_email, new_phone, new_address, student_id))
        conn.commit()
        conn.close()

    def fetch_student_from_level(self, level):
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute('''
                                    SELECT * FROM Students 
                                    WHERE level=?
                                   ''', (level,))
        ls = cursor.fetchall()

        conn.commit()
        conn.close()
        return

    def fetch_student_from_student_id(self, student_id):
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute('''
                                    SELECT * FROM Students 
                                    WHERE student_id=?
                                   ''', (student_id,))
        ls = cursor.fetchone()

        conn.commit()
        conn.close()
        print(ls)
        return ls

    def get_matricule_from_id(self,student_id):
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute('''
                                              SELECT matriculation_id FROM Students 
                                              WHERE  student_id=?
                                             ''', (student_id,))
        ls = cursor.fetchall()

        conn.commit()
        conn.close()
        return ls

    def get_matricule_from_name(self,name):
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute('''
                                              SELECT matriculation_id FROM Students
                                              WHERE  name=?
                                             ''', (name,))
        ls = cursor.fetchone()

        conn.commit()
        conn.close()
        print(ls)
        return ls
    def fetch_student_from_matricule(self, matricule):
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute('''
                                       SELECT * FROM Students 
                                       WHERE  matriculation_id=?
                                      ''', (matricule,))
        ls = cursor.fetchall()

        conn.commit()
        conn.close()
        return ls

    def add_grades(self, grade_id, matriculation_id, course_code, ca_score, exam_score, final, grade, credit):  #
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Grades(grade_id,matriculation_id, course_code,ca_score,exam_score,final,grade,credit) 
            VALUES(?,?,?,?,?,?,?,?)''',
                       (grade_id, matriculation_id, course_code, ca_score, exam_score, final, grade, credit))

        conn.commit()
        conn.close()

    def get_grades(self, course_code):
        conn = sqlite3.connect('../../sg.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT  s.name,g.matriculation_id,g.ca_score,g.exam_score,g.final,g.grade,g.credit, c.course_name FROM  Grades g 
             JOIN Courses c ON c.course_code=g.course_code
             JOIN Students s ON s.matriculation_id=g.matriculation_id
             WHERE c.course_code=?
            ''', (course_code,))
        grade = cursor.fetchall()
        return grade


#S = StudentModel()
#S.add_grades("GR07", 'ictu20241587', 'OS401', 40, 10, 50, "C", 3)
