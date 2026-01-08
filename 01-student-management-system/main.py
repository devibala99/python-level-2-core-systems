# main.py

from utils import (
    create_student_template,
    generate_student_id,
    check_email_uniqueness,
    check_mobile_uniqueness,
    email_validation,
    mobile_validation,
    get_valid_int,
    normalize_student_id
)

students = {}


def create_student_data():
    student_id = generate_student_id(students)
    student = create_student_template()

    # -------- Personal --------
    student["personal"]["name"] = input("Enter name: ").strip()
    student["personal"]["age"] = get_valid_int("Enter age: ", 5, 100)
    student["personal"]["gender"] = input("Enter gender (M/F): ").strip().upper()

    email = input("Enter email: ").strip()
    if not email_validation(email) or not check_email_uniqueness(students, email):
        return "❌ Invalid or duplicate email"

    mobile = input("Enter mobile number: ").strip()
    if not mobile_validation(mobile) or not check_mobile_uniqueness(students, mobile):
        return "❌ Invalid or duplicate mobile"

    student["personal"]["email"] = email
    student["personal"]["mobile"] = mobile

    # -------- Academics --------
    student["academics"]["class"] = input("Enter class/course: ").strip()
    student["academics"]["year"] = get_valid_int("Enter year (1-4): ", 1, 4)

    # Optional subjects
    while True:
        subject = input("Enter subject name (or press enter to stop): ").strip()
        if not subject:
            break
        marks = get_valid_int(f"Enter marks for {subject}: ", 0, 100)
        student["academics"]["subjects"][subject] = marks

    # -------- Address --------
    student["address"]["city"] = input("Enter city: ").strip()
    student["address"]["state"] = input("Enter state: ").strip()

    students[student_id] = student
    return f"✅ Student added successfully (ID: {student_id})"


def read_student_data():
    raw_id = input("Enter student ID to search: ")
    student_id = normalize_student_id(raw_id)

    if student_id not in students:
        return "❌ Student not found"

    print(students[student_id])
    return "✅ Displayed successfully"


def update_student_data():
    raw_id = input("Enter student ID to update: ")
    student_id = normalize_student_id(raw_id)

    if student_id not in students:
        return "❌ Student not found"

    student = students[student_id]

    section = input("Section (personal/academics/address/status): ").strip().lower()
    if section not in student:
        return "❌ Invalid section"

    # Special handling for subjects
    if section == "academics":
        choice = input("Update class/year/subjects? ").strip().lower()

        if choice == "subjects":
            subject = input("Enter subject name: ").strip()
            marks = get_valid_int("Enter new marks: ", 0, 100)
            student["academics"]["subjects"][subject] = marks
            return "✅ Subject updated"

        if choice in student["academics"]:
            value = input("Enter new value: ").strip()
            student["academics"][choice] = value
            return "✅ Academic data updated"

        return "❌ Invalid academic field"

    # Normal update
    print("Available fields:", student[section].keys())
    field = input("Enter field name: ").strip()
    if field not in student[section]:
        return "❌ Invalid field"

    student[section][field] = input("Enter new value: ").strip()
    return "✅ Student data updated"


def delete_student_data():
    raw_id = input("Enter student ID to delete: ")
    student_id = normalize_student_id(raw_id)

    if student_id not in students:
        return "❌ Student not found"

    del students[student_id]
    return "🗑️ Student deleted"


def show_menu():
    print("\n🎓 Student Management System")
    print("1. Add new student")
    print("2. View student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")


while True:
    show_menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(create_student_data())
        elif choice == 2:
            print(read_student_data())
        elif choice == 3:
            print(update_student_data())
        elif choice == 4:
            print(delete_student_data())
        elif choice == 5:
            break
        else:
            print("❌ Invalid choice")
    except ValueError:
        print("❌ Numbers only")
