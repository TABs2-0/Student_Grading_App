from pathlib import Path
import win32com.client
import re  # for xters not recognised by microsoft
import csv
import pandas


# the function below will download any CSV file having as messaage " Student Grading App" from mailbox
def autodownload_marks():
    def non_recognised(subj):
        cleaned_subj = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '_', subj)
        return cleaned_subj

    #create a folder to store the results
    output_dir = Path.cwd() / "Marks"
    output_dir.mkdir(parents=True,
                     exist_ok=True)  # parents help recreate any missen parent directory amd exist_ok returns an error if the folder already exist

    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace(
        "MAPI")  # connects the App with Outlook using the Messaging API  (MAPI)

    inbox = outlook.GetDefaultFolder(
        6)  # precise the folder in outlook where the attachment will be collected 6 stands for inbox,23 for junk folder

    # introduce a given condition
    #sender = "yoan1661@gmail.com"
    t_subject = "Student Grading App"
    #Get messages

    messages = inbox.Items

    for message in messages:
        if message.Subject == t_subject:
            subject = message.Subject
            cleaned_subject = non_recognised(subject)
            body = message.body
            attachments = message.Attachments

            #Create a Separate file for each Attachment
            target_folder = output_dir / cleaned_subject
            target_folder.mkdir(parents=True, exist_ok=True)

            # store each attachment in our output_dir folder
            for attachment in attachments:
                if attachment.FileName.endswith(".csv"):
                    attachment.SaveAsFile(output_dir / attachment.FileName)
    print(f"Attachments are saved in: {output_dir}")


def read_csv(file_path):
    file = pandas.read_csv(file_path)
    return file


def calculate_final_score(ca_score, exam_score):
    return ca_score + exam_score


def calculate_grade(final_score):
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


def extract_marks(file, ca_mark=None, exam_mark=None, grade=None):
    ca_mark = []
    exam_mark = []
    grade = []
    final_mark = []
    ca_mark = file["CAScore"]
    exam_mark = file["ExamScore"]
    for ca in ca_mark:
        for exam in exam_mark:
            F = calculate_final_score(ca, exam)  #final Mark
            G = calculate_grade(F)  #grades
            final_mark.append(F)
            grade.append(G)

    print(ca_mark)
    print(final_mark)
    print(grade)
