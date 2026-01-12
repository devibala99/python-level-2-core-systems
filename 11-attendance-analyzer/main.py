from utils import (
    calculate_attendance_percentage,
    determine_status,
    get_valid_int
)

students = []


def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    total_classes = get_valid_int("Enter total classes: ")
    if total_classes == 0:
        print("❌ Total classes cannot be zero.")
        return

    attended_classes = get_valid_int("Enter attended classes: ")
    if attended_classes > total_classes:
        print("❌ Attended classes cannot exceed total classes.")
        return

    percentage = calculate_attendance_percentage(
        total_classes, attended_classes
    )
    status = determine_status(percentage)

    student = {
        "name": name,
        "percentage": percentage,
        "status": status
    }

    students.append(student)
    print(f"✅ Record added for {name}")


def view_students():
    if not students:
        print("❌ No attendance records found.")
        return

    print("\n📋 Attendance Report")
    print("-" * 40)
    print(f"{'Name':<15} {'%':<10} {'Status':<15}")
    print("-" * 40)

    for student in students:
        print(
            f"{student['name']:<15} "
            f"{student['percentage']:<10} "
            f"{student['status']:<15}"
        )
    print("-" * 40)


def show_menu():
    print("\n📊 Attendance Analyzer")
    print("1. Add Student Attendance")
    print("2. View Report")
    print("3. Exit")


while True:
    show_menu()

    try:
        choice = int(input("Enter choice (1-3): "))

        if choice == 3:
            print("👋 Exiting Attendance Analyzer")
            break
        elif choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        else:
            print("❌ Invalid choice")

    except ValueError:
        print("❌ Enter numeric value only")
