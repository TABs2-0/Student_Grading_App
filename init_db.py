import sqlite3


def initialise():
    try:
        conn = sqlite3.connect('sg.db')
        cursor = conn.cursor()
        # SQLITE USES 0 AND 1 FOR TRUE OR FALSE
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        user_id TEXT PRIMARY KEY,
        user_name TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role NOT NULL CHECK (role in("lecturer","Admin","student"))
      
        );
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students(
        student_id TEXT PRIMARY KEY,
        matriculation_id  TEXT NOT NULL ,
        name TEXT  NOT NULL , 
        semester TEXT NOT NULL ,
        level INTEGER NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL
        );
        ''')
        cursor.execute('''
           CREATE TABLE IF NOT EXISTS Courses(
           course_code TEXT PRIMARY KEY,
           course_name TEXT NOT NULL,
           lecturer_id TEXT NOT NULL,
           
           FOREIGN KEY (lecturer_id) REFERENCES Lecturers(lecturer_id)
            );
    ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lecturers(
        
        lecture_id TEXT PRIMARY KEY,
        lecturer_name TEXT NOT NULL,
        department TEXT NOT NULL,
        lecturer_mail TEXT NOT NULL 
       
        );
        ''')
        cursor.execute(
            '''
            CREATE  TABLE IF NOT EXISTS admin(
            admin_id TEXT PRIMARY KEY,
            admin_name TEXT NOT NULL
            
            
            );
            
            ''')
        cursor.execute('''
           CREATE TABLE IF NOT EXISTS Enrolled(
           enrollment_id TEXT PRIMARY KEY,
           student_id TEXT NOT NULL,
           course_id TEXT NOT NULL,
           FOREIGN KEY(student_id)  REFERENCES Students(student_id),
           FOREIGN KEY(course_id )  REFERENCES Courses(course_code)
            );
           ''')
        cursor.execute('''
                                 CREATE TABLE IF NOT EXISTS Grads(
                                 grade_id INT PRIMARY KEY,
                                 matriculation_id TEXT NOT NULL,
                                 course_code TEXT NOT NULL,
                                 ca_score REAL ,
                                 exam_score REAL,
                                 final score  REAL,
                                 grade TEXT,
                                 credit TEXT,
                                 FOREIGN KEY (course_code) REFERENCES Courses(course_code),
                                 FOREIGN KEY(matriculation_id)  REFERENCES Student(matriculation_id)
                                  );
                                 ''')

                #THE COMMENTED PIECE OF CODE BELOW IS NOT DEONTOLOGICAL AND NEEDS LATER MODIFICATIONS SINCE IT ALTERS  A TABLE WITHOUT VERIFYING ITS CHANGES STATUS
       # cursor.execute('''
        #    ALTER TABLE Courses ADD   level TEXT ''')
        #cursor.execute(''' ALTER TABLE Courses ADD COLUMN semester TEXT ''')
        #cursor.execute('''
         #   ALTER TABLE Students ADD COLUMN gender TEXT CHECK(gender IN ('female', 'male')) NOT NULL DEFAULT 'male'
        #''')

        #cursor.execute('''
        #    ALTER TABLE Students ADD COLUMN address TEXT NOT NULL DEFAULT 'messassi'
        #''')


        cursor.execute('''
                   ALTER   TABLE Grads RENAME TO Grades
                ''')

        conn.commit()
        print("successful creation")
        conn.close()
    except sqlite3.Error as error:

        print("an error has occurred during connection", error)
        print(error)


initialise()
