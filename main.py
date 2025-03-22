import sqlite3
#initialize
def init_db():
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        course TEXT NOT NULL)''')
    conn.commit()
    conn.close()

#to register a student
def register_student():
    name=input("Enter student name:")
    email=input("Enter student email:")
    course=input("Enter course name:")

    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO Students(name,email,course) VALUES(?,?,?)",(name,email,course))
        conn.commit()
        print("Student registered Successfully!")
    except sqlite3.IntegrityError:
        print("Error:Email already exists!")
    conn.close()


#view student in terminal
def view_students():
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Students")
    Students=cursor.fetchall()#to fetch all students
    conn.close()

    if Students:
        print("\nRegistered Students:")
        print("{:5}{:<20}{:25}{:<15}".format("id","name","email","course"))
        print("-"*70)
    for student in Students:
        print("{:5} {:<20} {:<25} {:<15}".format(student[0],student[1],student[2],student[3]))
    else:
        print("No Students Registered yet.")

def generate_report():
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Students")
    Students=cursor.fetchall()
    conn.close()


def main():
    init_db()
    while True:
        print("\nStudent Registration System")
        print("1.Register Student")
        print("2.View Students")
        print("3.Generate HTML Report")
        print("4.Exit")
        choice=input("Enter choice:")

        if choice=="1": 
            register_student()
        elif choice=="2":
            view_students()
        elif choice=="3":
            generate_report()
            print("Report Generated!")
        elif choice=="4":
            print("Exiting.......")
            break
        else:
            print("Invalid choice,please try again.")


if __name__=="__main__":
    main()