from student_grading_app.models.Course import CourseModel


class CourseControl:
    def __init__(self):
        super().__init__()
        self.C = CourseModel()

    def fetch_courses_from_control(self, course_name):
        courses = self.C.fetch_courses_from_name(course_name)
        return courses

    def fetch_courses_from_name_control(self):
        courses = self.C.fetch_course_from_name()
        return courses

    def add_courses_from_control(self, course_code, course_name, lecturer_id, level, semester):
        self.C.add_course(course_code, course_name, lecturer_id, level, semester)

    def update_courses_from_control(self, course_code, course_name, lecturer_id, level, semester):
        self.C.update_a_course(course_code, course_name, lecturer_id, level, semester)

    def delete_course_from_control(self, course_code):
        self.C.delete_a_course(course_code)
