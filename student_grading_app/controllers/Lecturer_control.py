from student_grading_app.models import Lecturer


class LecturerControl:
    def __init__(self):
        super().__init__()
        self.LecturerModel = Lecturer.LecturerModel()

    def get_lecturer_courses(self, lecturer_name):
        return self.LecturerModel.get_lecturer_courses(lecturer_name)

    def get_lecturer_id(self, name):
        return self.LecturerModel.Get_Lecturer_Id(name)
