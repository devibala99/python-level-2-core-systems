from utils import (
    read_resume_file,
    extract_name,
    extract_email,
    extract_mobile,
    extract_skills,
    extract_education
)

SKILL_KEYWORDS = [
    "python", "java", "sql",
    "machine learning", "data analysis",
    "django", "flask"
]


def parse_resume():
    file_path = input("Enter resume file path: ").strip()

    resume_text = read_resume_file(file_path)
    if resume_text is None:
        return

    parsed_data = {
        "name": extract_name(resume_text),
        "email": extract_email(resume_text),
        "mobile": extract_mobile(resume_text),
        "skills": extract_skills(resume_text, SKILL_KEYWORDS),
        "education": extract_education(resume_text)
    }

    print("\n📄 Parsed Resume Data")
    print("-" * 30)
    for key, value in parsed_data.items():
        print(f"{key.capitalize():<12}: {value}")
    print("-" * 30)


def show_menu():
    print("\n📄 Resume Parser")
    print("1. Parse Resume")
    print("2. Exit")


while True:
    show_menu()
    choice = input("Enter choice (1-2): ").strip()

    if choice == "1":
        parse_resume()
    elif choice == "2":
        print("👋 Exiting Resume Parser")
        break
    else:
        print("❌ Invalid choice")
