import sqlite3
def initialise():


    try:
        conn = sqlite3.connect('sg.db')
        cursor=conn.cursor()
    #SQLITE USES 0 AND 1 FOR TRUE OR FALSE
        cursor.execute('''
        CREATE TABLE IF NOT EXIST users(
        user_id INTEGER PRIMARY KEY,
        user_name TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        is_admin BOOL NOT NULL DEFAULT  0
        
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXIST student(
        matricule  TEXT PRIMARY KEY,
        name TEXT  NOT NULL , 
        level TEXT NOT NULL,
        semester TEXT NOT NULL ,
        level INTEGER NOT NULL ,
        ''')
        cursor.execute('''
           CREATE TABLE IF NOT EXIST course(
            course_code INTEGER PRIMARY KEY,
           number_enrolled INTEGER NOT NULL,
           name TEXT NOT NULL,
           semester TEXT NOT NULL,
           lecturer TEXT NOT NULL,
            )
    ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXIST lecturer(
        
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        post TEXT NOT NULL,
        is _intern BOOL NOT NULL DEFAULT 0)
        ''')
        cursor.execute(
            '''
            CREATE  TABLE IF NOT EXIST admin(
            admin_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            post TEXT NOT NULL,
            
            )
            
            ''')
        cursor.execute('''
           CREATE TABLE IF NOT EXIST enrolled(
           enrollment_id INT PRIMARY KEY
           matricule INT NOT NULL
           course_id TEXT NOT NULL
           FOREIGN KEY(course_id )  REFRENCES course(course_code)
           FOREIGN KEY(matricule)  REFRENCES student(matricule)
    
           ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as error:

        print("an error has occured during connection", error)



