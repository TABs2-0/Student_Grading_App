class StudentModel:

    def __init__(self, name: str, matricule: str, level: str, semester: str, department: str, gender: str, courses,
                 status="Top_up", ):
        self.name = name
        self.gender = gender
        self.semester = semester
        self.__matricule = matricule  # the__indicates matricule is private
        self.level = level
        self.courses = []
        self.department = department

    def checkdepartment(self, department):  # this function makes sure that a corect departement is selected
        if self.department.upper() not in ['ICT', 'BMS']:
            raise ValueError(" Select a valuable department ")
