class CourseModel:
    def __init__(self,course_name,level,semester,course_code,number_enrolled,lecturer_id):
        self.course_name= course_name
        self.semester= semester
        self.course_code = course_code
        self.number_enrolled =number_enrolled
        self.lecturer_id=lecturer_id
        self.level= level