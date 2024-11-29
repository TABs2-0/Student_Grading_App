class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def check_pass(self, password):
        return self.password == password

