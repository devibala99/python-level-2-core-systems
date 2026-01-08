from utils import (
    create_contact_template,
    generate_contact_id,
    normalize_contact_id,
    email_validation,
    mobile_validation,
    check_email_uniqueness,
    check_mobile_uniqueness
)

contacts = {}


def create_contact():
    contact_id = generate_contact_id(contacts)
    contact = create_contact_template()

    name = input("Enter name: ").strip()
    if not name:
        return "❌ Name cannot be empty"

    mobile = input("Enter mobile number: ").strip()
    if not mobile_validation(mobile):
        return "❌ Invalid mobile number"
    if not check_mobile_uniqueness(contacts, mobile):
        return "❌ Mobile number already exists"

    email = input("Enter email: ").strip()
    if not email_validation(email):
        return "❌ Invalid email format"
    if not check_email_uniqueness(contacts, email):
        return "❌ Email already exists"

    city = input("Enter city: ").strip()
    state = input("Enter state: ").strip()
    pincode = input("Enter pincode: ").strip()

    contact["name"] = name
    contact["mobile"] = mobile
    contact["email"] = email
    contact["address"]["city"] = city
    contact["address"]["state"] = state
    contact["address"]["pincode"] = pincode

    contacts[contact_id] = contact
    return f"✅ Contact added successfully (ID: {contact_id})"


def read_contact():
    if not contacts:
        return "❌ Contact book is empty"

    raw_id = input("Enter contact ID: ").strip()
    contact_id = normalize_contact_id(raw_id)

    if not contact_id or contact_id not in contacts:
        return "❌ Contact not found"

    contact = contacts[contact_id]

    print(f"\n📞 Contact ID: {contact_id}")
    print(f"Name   : {contact['name']}")
    print(f"Mobile : {contact['mobile']}")
    print(f"Email  : {contact['email']}")
    print("Address:")
    for k, v in contact["address"].items():
        print(f"  {k.capitalize()}: {v}")
    print(f"Favorite: {contact['is_favorite']}")

    return "✅ Contact displayed successfully"


def update_contact():
    raw_id = input("Enter contact ID to update: ").strip()
    contact_id = normalize_contact_id(raw_id)

    if not contact_id or contact_id not in contacts:
        return "❌ Contact not found"

    contact = contacts[contact_id]

    print("Updatable fields: name, mobile, email, city, state, pincode, favorite")
    field = input("Enter field to update: ").strip().lower()

    if field == "name":
        value = input("Enter new name: ").strip()
        if not value:
            return "❌ Name cannot be empty"
        contact["name"] = value

    elif field == "mobile":
        value = input("Enter new mobile: ").strip()
        if not mobile_validation(value):
            return "❌ Invalid mobile"
        if not check_mobile_uniqueness(contacts, value):
            return "❌ Mobile already exists"
        contact["mobile"] = value

    elif field == "email":
        value = input("Enter new email: ").strip()
        if not email_validation(value):
            return "❌ Invalid email"
        if not check_email_uniqueness(contacts, value):
            return "❌ Email already exists"
        contact["email"] = value

    elif field in ("city", "state", "pincode"):
        value = input(f"Enter new {field}: ").strip()
        contact["address"][field] = value

    elif field == "favorite":
        contact["is_favorite"] = not contact["is_favorite"]

    else:
        return "❌ Invalid field"

    return "✅ Contact updated successfully"


def delete_contact():
    raw_id = input("Enter contact ID to delete: ").strip()
    contact_id = normalize_contact_id(raw_id)

    if not contact_id or contact_id not in contacts:
        return "❌ Contact not found"

    del contacts[contact_id]
    return f"🗑️ Contact {contact_id} deleted successfully"


def show_menu():
    print("\n📒 Contact Book")
    print("1. Add new contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Exit")


while True:
    show_menu()

    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("👋 Exiting Contact Book")
            break

        if choice < 1 or choice > 5:
            print("⚠️ Invalid choice")
            continue

        if choice == 1:
            result = create_contact()
        elif choice == 2:
            result = read_contact()
        elif choice == 3:
            result = update_contact()
        elif choice == 4:
            result = delete_contact()

        print(result)

    except ValueError:
        print("❌ Enter numeric value only")
