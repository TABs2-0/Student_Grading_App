from pathlib import Path
import win32com.client
import re  # for xters not recognised by microsoft
import csv
import pandas
from student_grading_app.models import Student


# the function below will download any CSV file having as messaage " Student Grading App" from mailbox
class AdminControl:
    def __init__(self):
        super().__init__()
        self.A = Student.StudentModel()

    def autodownload_marks(self):
        def non_recognised(subj):
            cleaned_subj = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '_', subj)
            return cleaned_subj

        # Create a folder to store the results
        output_dir = Path.cwd() / "Marks"
        output_dir.mkdir(parents=True, exist_ok=True)

        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.GetDefaultFolder(6)
        t_subject = "Student Grading App"
        messages = inbox.Items

        for message in messages:
            if message.Subject == t_subject:
                subject = message.Subject
                cleaned_subject = non_recognised(subject)
                body = message.body
                attachments = message.Attachments

                # Create a Separate file for each Attachment
                target_folder = output_dir / cleaned_subject
                target_folder.mkdir(parents=True, exist_ok=True)

                # Store each attachment in our output_dir folder
                for attachment in attachments:
                    if attachment.FileName.endswith(".csv"):
                        attachment.SaveAsFile(output_dir / attachment.FileName)

        print(f"Attachments are saved in: {output_dir}")

    def read_csv(self, file_path):
        print(f"Reading CSV from: {file_path}")
        A = pandas.read_csv(file_path)
        print(A.columns)
        print(A.head())
        return A

    def calculate_final_score(self, ca_score, exam_score):
        return ca_score + exam_score

    def calculate_grade(self, final_score):
        if final_score >= 70:
            return "A", 4.0
        elif final_score >= 60:
            return "B+", 3.5
        elif final_score >= 50:
            return "B", 3.0
        elif final_score >= 45:
            return "C+", 2.5
        else:
            return "F", 0.0

    def extract_marks(self, file):
        grades = []
        final_marks = []

        file["CAScore"] = pandas.to_numeric(file["CAScore"], errors="coerce")
        file['ExamScore'] = pandas.to_numeric(file["ExamScore"], errors="coerce")

        ca_scores = file['CAScore'].values
        exam_scores = file['ExamScore'].values

        for ca, exam in zip(ca_scores, exam_scores):
            final_score = self.calculate_final_score(ca, exam)
            grade = self.calculate_grade(final_score)
            final_marks.append(final_score)
            grades.append(grade)

        # Debug print
        print(f"Processed {len(final_marks)} students")
        print("Final marks:", final_marks)
        print("Grades:", grades)

        return final_marks, grades

    def add_grades_to_csv(self, path_file, final_marks, grades):
        df = pandas.read_csv(path_file)
        df["FinalScore"] = final_marks
        df['Grade'] = [grade[0] for grade in grades]
        df['Credits'] = [grade[1] for grade in grades]

        df.to_csv(path_file, index=True)

        print("grades updated")
        print(df.head())

    def main_csv_marks(self, path):
        fichier = self.read_csv(path)
        final, gra = self.extract_marks(fichier)
        print(final)
        self.add_grades_to_csv(path, final, gra)

        return fichier  # this statement is a test can be removed


# Example usage
if __name__ == "__main__":
    p = "C:/Users/Tab's/PycharmProjects/SGApp/student_grading_app/controllers/Marks/index.csv"
    admin = AdminControl()
    #admin.autodownload_marks()
    admin.main_csv_marks(p)
