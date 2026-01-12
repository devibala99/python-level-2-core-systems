def calculate_attendance_percentage(total_classes, attended_classes):
    """
    Calculate attendance percentage safely.
    """
    if total_classes == 0:
        return 0.0

    percentage = (attended_classes / total_classes) * 100
    return round(percentage, 2)


def determine_status(percentage):
    """
    Determine eligibility based on percentage.
    """
    if percentage >= 75:
        return "Eligible"
    return "Not Eligible"


def get_valid_int(prompt):
    """
    Take a non-negative integer input from user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("❌ Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("❌ Enter a valid integer.")
