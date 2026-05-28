import csv
from database import connect_db

def export_to_csv():

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    with open("students.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "NAME", "AGE", "DEPARTMENT", "MARKS"]
        )

        writer.writerows(students)

    print("Data exported successfully!")

    cursor.close()
    connection.close()