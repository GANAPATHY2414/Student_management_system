from database import connect_db
from auth import login
from export import export_to_csv


#Adding the students
def add_student():

    try:

        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        department = input("Enter department: ")
        marks = float(input("Enter marks: "))

        connection = connect_db()
        cursor = connection.cursor()

        query = """
        INSERT INTO students(name, age, department, marks)
        VALUES(%s, %s, %s, %s)
        """

        values = (name, age, department, marks)

        cursor.execute(query, values)

        connection.commit()

        print("Student added successfully!")

        cursor.close()
        connection.close()

    except ValueError:
        print("Please enter valid number")

#viewing student
def view_students():

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    for student in students:
        print(student)

    cursor.close()
    connection.close()
#search students

def search_student():

    name = input("Enter student name: ")

    connection = connect_db()
    cursor = connection.cursor()

    query = "SELECT * FROM students WHERE name=%s"

    cursor.execute(query, (name,))

    result = cursor.fetchall()

    for student in result:
        print(student)

    cursor.close()
    connection.close()
#update students
def update_student():

    student_id = int(input("Enter student ID: "))
    new_marks = float(input("Enter new marks: "))

    connection = connect_db()
    cursor = connection.cursor()

    query = "UPDATE students SET marks=%s WHERE id=%s"

    cursor.execute(query, (new_marks, student_id))

    connection.commit()

    print("Student updated successfully!")

    cursor.close()
    connection.close()
#delete students

def delete_student():

    student_id = int(input("Enter student ID: "))

    connection = connect_db()
    cursor = connection.cursor()

    query = "DELETE FROM students WHERE id=%s"

    cursor.execute(query, (student_id,))

    connection.commit()

    print("Student deleted successfully!")

    cursor.close()
    connection.close()

if login():

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Export CSV")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            export_to_csv()

        elif choice == "7":
            print("Thank You!")
            break

        else:
            print("Invalid choice")