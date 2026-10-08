# Final Challenge - Student Registration System
students = {}  # id -> {"name": str, "age": int, "course": str, "marks": float}


def read_marks(prompt):
    while True:
        try:
            m = float(input(prompt))
            if 0 <= m <= 100:
                return m
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_student():
    sid = input("Student ID: ").strip()
    if sid in students:
        print("A student with this ID already exists.")
        return
    name = input("Name: ").strip()
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        return
    course = input("Course: ").strip()
    marks = read_marks("Marks (0-100): ")
    students[sid] = {"name": name, "age": age, "course": course, "marks": marks}
    print("Student added successfully.")


def print_student(sid, s):
    print(f"ID: {sid} | Name: {s['name']} | Age: {s['age']} | "
          f"Course: {s['course']} | Marks: {s['marks']}")


def view_students():
    if not students:
        print("No students registered.")
        return
    for sid, s in students.items():
        print_student(sid, s)


def search_student():
    sid = input("Enter ID to search: ").strip()
    if sid in students:
        print_student(sid, students[sid])
    else:
        print("Student not found.")


def update_student():
    sid = input("Enter ID to update: ").strip()
    if sid not in students:
        print("Student not found.")
        return
    s = students[sid]
    print("Leave a field blank to keep the current value.")
    name = input(f"Name [{s['name']}]: ").strip()
    age = input(f"Age [{s['age']}]: ").strip()
    course = input(f"Course [{s['course']}]: ").strip()
    marks = input(f"Marks [{s['marks']}]: ").strip()

    if name:
        s["name"] = name
    if age:
        try:
            s["age"] = int(age)
        except ValueError:
            print("Invalid age, keeping old value.")
    if course:
        s["course"] = course
    if marks:
        try:
            m = float(marks)
            if 0 <= m <= 100:
                s["marks"] = m
            else:
                print("Marks out of range, keeping old value.")
        except ValueError:
            print("Invalid marks, keeping old value.")
    print("Student updated.")


def delete_student():
    sid = input("Enter ID to delete: ").strip()
    if sid in students:
        del students[sid]
        print("Student deleted.")
    else:
        print("Student not found.")


def class_average():
    if not students:
        print("No students registered.")
        return
    total = 0
    for s in students.values():
        total += s["marks"]
    print(f"Class average marks: {total / len(students):.2f}")


def top_student():
    if not students:
        print("No students registered.")
        return
    best_id = None
    for sid, s in students.items():
        if best_id is None or s["marks"] > students[best_id]["marks"]:
            best_id = sid
    print("Top performer:")
    print_student(best_id, students[best_id])


def main():
    while True:
        print("\n--- STUDENT REGISTRATION SYSTEM ---")
        print("1. Add student")
        print("2. View all students")
        print("3. Search by ID")
        print("4. Update student")
        print("5. Delete student")
        print("6. Class average marks")
        print("7. Highest-performing student")
        print("8. Exit")
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
            class_average()
        elif choice == "7":
            top_student()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
