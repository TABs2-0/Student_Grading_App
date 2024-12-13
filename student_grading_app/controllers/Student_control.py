from student_grading_app.models.Student import StudentModel
class StudentControl:
    def __init__(self):
        super().__init__()
        self.S=StudentModel()

    def get_grades_from_control(self,course_code):

        return self.S.get_grades(course_code)

    def add_grades_from_control(self,grade_id, matriculation_id, course_code, ca_score, exam_score ):

        return self.S.add_grades(grade_id, matriculation_id, course_code, ca_score, exam_score)
