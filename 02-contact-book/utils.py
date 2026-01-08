import re

def create_contact_template():
    return {
        "name": "",
        "mobile": "",
        "email": "",
        "address": {
            "city": "",
            "state": "",
            "pincode": "",

        },
        "is_favorite": False
    }

def generate_contact_id(contacts):
    if not contacts:
        return "CON-001"
    suffix_numbers = [
        int(cid.split("-")[1]) for cid in contacts.keys()
    ]
    next_id = max(suffix_numbers) + 1
    return f"CON-{str(next_id).zfill(3)}"

def normalize_contact_id(raw_id):
    raw_id = raw_id.strip().upper()
    if not raw_id.startswith("CON-"):
        return None
    suffix = raw_id.split("-")[1]
    if not suffix.isdigit():
        return None
    return f"CON-{suffix.zfill(3)}"


def email_validation(email):
    pattern = r"^[a-zA-Z0-9._/-]+@[a-zA-Z0-9._-]+\.[a-zA-z]{2,}$"
    return bool(re.match(pattern, email))

def mobile_validation(mobile):
    return mobile.isdigit() and len(mobile) == 10

def check_email_uniqueness(contacts, email):
    return all(c["email"] == email for c in contacts.values())

def check_mobile_uniqueness(contacts, mobile):
    return not any(c["mobile"] == mobile for c in contacts.values())

def get_valid_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Out of range! Please enter between {min_val} and {max_val}.")
                continue
            return val
        except ValueError:
            print("Invalid input! Please enter a whole number.")
