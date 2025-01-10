from student_grading_app.models.Student import StudentModel


class StudentControl:
    def __init__(self):
        super().__init__()
        self.S = StudentModel()

    def get_grades_from_control(self, course_code):
        return self.S.get_grades(course_code)

    def get_matricule_from_name(self, name):
        return self.S.get_matricule_from_name(name)

    def add_grades_from_control(self, grade_id, matriculation_id, course_code, ca_score, exam_score, final, grade,
                                credit):
        return self.S.add_grades(grade_id, matriculation_id, course_code, ca_score, exam_score, final, grade, credit)

    def get_matricule_from_student_id(self, student_id):
        return self.S.get_matricule_from_id(student_id)
