class LecturerModel:
    def __init__(self, name, id ,post,is_intern=True):
        self.name = name
        self.__id = id
        self.is_intern = is_intern
        self.post = post


