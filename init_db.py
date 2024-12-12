import sqlite3


def initialise():
    try:
        conn = sqlite3.connect('sg.db')
        cursor = conn.cursor()
        # SQLITE USES 0 AND 1 FOR TRUE OR FALSE
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
        user_id TEXT PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role NOT NULL CHECK (role in("lecturer","Admin","student"))
      
        );
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS student(
        matricule  TEXT PRIMARY KEY,
        name TEXT  NOT NULL , 
        semester TEXT NOT NULL ,
        level INTEGER NOT NULL );
        ''')
        cursor.execute('''
           CREATE TABLE IF NOT EXISTS course(
            course_code INTEGER PRIMARY KEY,
           number_enrolled INTEGER NOT NULL,
           name TEXT NOT NULL,
           semester TEXT NOT NULL,
           lecturer TEXT NOT NULL
            );
    ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturer(
        
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        post TEXT NOT NULL,
        is_intern BOOL NOT NULL DEFAULT 0
        );
        ''')
        cursor.execute(
            '''
            CREATE  TABLE IF NOT EXISTS admin(
            admin_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            post TEXT NOT NULL
            
            );
            
            ''')
        cursor.execute('''
           CREATE TABLE IF NOT EXISTS enrolled(
           enrollment_id INT PRIMARY KEY,
           matricule INT NOT NULL,
           course_id TEXT NOT NULL,
           FOREIGN KEY(course_id )  REFERENCES course(course_code),
           FOREIGN KEY(matricule)  REFERENCES student(matricule)
            );
           ''')
        conn.commit()
        print("successful creation")
        conn.close()
    except sqlite3.Error as error:

        print("an error has occured during connection", error)
        print(error)


initialise()
