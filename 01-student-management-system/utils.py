# utils.py

import re

def create_student_template():
    return {
        "personal": {
            "name": "",
            "age": 0,
            "gender": "",
            "email": "",
            "mobile": ""
        },
        "academics": {
            "class": "",
            "year": 0,
            "subjects": {}
        },
        "address": {
            "city": "",
            "state": ""
        },
        "status": {
            "active": True
        }
    }


def generate_student_id(students):
    if not students:
        return "STU1001"
    last_id = max(int(sid[3:]) for sid in students.keys())
    return f"STU{last_id + 1}"


def normalize_student_id(raw_id):
    if not raw_id or len(raw_id) < 4:
        return None
    prefix = raw_id[:3].upper()
    number = raw_id[3:]
    if not number.isdigit():
        return None
    return prefix + number


def email_validation(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


def mobile_validation(mobile):
    return mobile.isdigit() and len(mobile) == 10


def check_email_uniqueness(students, email):
    return all(s["personal"]["email"] != email for s in students.values())


def check_mobile_uniqueness(students, mobile):
    return all(s["personal"]["mobile"] != mobile for s in students.values())


def get_valid_int(prompt, min_value=None, max_value=None):
    try:
        value = int(input(prompt))
        if min_value is not None and value < min_value:
            return None
        if max_value is not None and value > max_value:
            return None
        return value
    except ValueError:
        return None
