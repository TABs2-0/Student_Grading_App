from student_grading_app.view import login


def run_login():
    page = login.Login()
    page.mainloop()


if __name__ == "__main__":
    run_login()
