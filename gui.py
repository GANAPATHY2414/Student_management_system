from tkinter import *
from tkinter import messagebox, ttk

from database import connect_db
from export import export_to_csv
from auth import login

root = Tk()

root.title("Student Management System")

root.geometry("900x700")

root.configure(bg="#dbeafe")

heading = Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#2563eb",
    fg="white",
    pady=10
)

heading.pack(fill=X)




container = Frame(root, bg="#dbeafe")

container.pack(pady=20)

main_frame = Frame(
    container,
    bg="white",
    padx=20,
    pady=20
)

main_frame.grid(row=0, column=0, padx=20)

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview",
    font=("Arial", 10),
    rowheight=25
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 11, "bold")
)


#Adding Students

def add_student():

    try:

        name = name_entry.get()
        age = age_entry.get()
        department = dept_entry.get()
        marks = marks_entry.get()

        print(name, age, department, marks)

        connection = connect_db()

        print("Database Connected")

        cursor = connection.cursor()

        query = """
        INSERT INTO students(name, age, department, marks)
        VALUES(%s, %s, %s, %s)
        """

        values = (name, age, department, marks)

        cursor.execute(query, values)

        connection.commit()

        print("Data Inserted")

        messagebox.showinfo(
            "Success",
            "Student added successfully!"
        )

        cursor.close()
        connection.close()

        view_students()

    except Exception as e:

        print(e)

        messagebox.showerror(
            "Error",
            str(e)
        )

#Viewing Students
def view_students():

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    # print(students)

    # CLEAR OLD DATA

    for data in tree.get_children():
        tree.delete(data)

    # INSERT DATA INTO TABLE

    for student in students:

        tree.insert(
            "",
            "end",
            values=(
                student[0],
                student[1],
                student[2],
                student[3],
                student[4]
            )
        )

    cursor.close()
    connection.close()

#Search Students
def search_student():

    name = search_entry.get()

    connection = connect_db()
    cursor = connection.cursor()

    query = "SELECT * FROM students WHERE name=%s"

    cursor.execute(query, (name,))

    result = cursor.fetchall()

    for row in tree.get_children():
        tree.delete(row)

    for student in result:

        tree.insert(
            "",
            END,
            values=student
        )

    cursor.close()
    connection.close()

#Delete Students
def delete_student():

    student_id = delete_entry.get()

    connection = connect_db()
    cursor = connection.cursor()

    query = "DELETE FROM students WHERE id=%s"

    cursor.execute(query, (student_id,))

    connection.commit()

    messagebox.showinfo(
        "Deleted",
        "Student deleted successfully!"
    )

    cursor.close()
    connection.close()

#Update Students

def update_student():

    student_id = update_id_entry.get()
    new_marks = update_marks_entry.get()

    connection = connect_db()
    cursor = connection.cursor()

    query = "UPDATE students SET marks=%s WHERE id=%s"

    cursor.execute(query, (new_marks, student_id))

    connection.commit()

    messagebox.showinfo(
        "Updated",
        "Marks updated successfully!"
    )

    cursor.close()
    connection.close()

Label(
    main_frame,
    text="Student Name",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=0, column=0, pady=5)

name_entry = Entry(
    main_frame,
    font=("Arial", 11),
    width=30
)

name_entry.grid(row=0, column=1, pady=5)


Label(
    main_frame,
    text="Age",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=1, column=0, pady=5)

age_entry = Entry(
    main_frame,
    font=("Arial", 11),
    width=30
)

age_entry.grid(row=1, column=1, pady=5)


Label(
    main_frame,
    text="Department",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=2, column=0, pady=5)

dept_entry = Entry(
    main_frame,
    font=("Arial", 11),
    width=30
)

dept_entry.grid(row=2, column=1, pady=5)


Label(
    main_frame,
    text="Marks",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=3, column=0, pady=5)

marks_entry = Entry(
    main_frame,
    font=("Arial", 11),
    width=30
)

marks_entry.grid(row=3, column=1, pady=5)

Button(
    main_frame,
    text="Add Student",
    command=add_student,
    bg="#2563eb",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20
).grid(row=4, column=0, pady=10)

Button(
    main_frame,
    text="View Students",
    command=view_students,
    bg="#16a34a",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20
).grid(row=4, column=1, pady=10)

Label(
    main_frame,
    text="Search Student",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=5, column=0, pady=5)

search_entry = Entry(
    main_frame,
    width=30
)

search_entry.grid(row=5, column=1)

Button(
    main_frame,
    text="Search",
    command=search_student,
    bg="#f59e0b",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20
).grid(row=6, column=0, columnspan=2, pady=10)

Label(
    main_frame,
    text="Delete Student ID",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=7, column=0, pady=5)

delete_entry = Entry(
    main_frame,
    width=30
)

delete_entry.grid(row=7, column=1)

Button(
    main_frame,
    text="Delete",
    command=delete_student,
    bg="#dc2626",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20
).grid(row=8, column=0, columnspan=2, pady=10)

Label(
    main_frame,
    text="Update Student ID",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=9, column=0, pady=5)

update_id_entry = Entry(
    main_frame,
    width=30
)

update_id_entry.grid(row=9, column=1)


Label(
    main_frame,
    text="New Marks",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=10, column=0, pady=5)

update_marks_entry = Entry(
    main_frame,
    width=30
)

update_marks_entry.grid(row=10, column=1)

Button(
    main_frame,
    text="Update Marks",
    command=update_student,
    bg="#7c3aed",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20
).grid(row=11, column=0, columnspan=2, pady=10)

Button(
    main_frame,
    text="Export CSV",
    command=export_to_csv,
    bg="#92400e",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20
).grid(row=12, column=0, columnspan=2, pady=10)

table_frame = Frame(
    container,
    bg="white",
    padx=10,
    pady=10
)

table_frame.grid(row=0, column=1)

Label(
    table_frame,
    text="STUDENT RECORDS",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#2563eb"
).pack(pady=10)



tree = ttk.Treeview(
    table_frame,
    columns=(
        "ID",
        "NAME",
        "AGE",
        "DEPARTMENT",
        "MARKS"
    ),
    show="headings",
    height=15
)

# HEADINGS

tree.heading("ID", text="ID")
tree.heading("NAME", text="NAME")
tree.heading("AGE", text="AGE")
tree.heading("DEPARTMENT", text="DEPARTMENT")
tree.heading("MARKS", text="MARKS")

# COLUMN WIDTH

tree.column("ID", width=60, anchor=CENTER)
tree.column("NAME", width=180, anchor=CENTER)
tree.column("AGE", width=80, anchor=CENTER)
tree.column("DEPARTMENT", width=180, anchor=CENTER)
tree.column("MARKS", width=80, anchor=CENTER)

tree.pack()

root.mainloop()