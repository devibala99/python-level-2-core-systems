import re


def read_resume_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("❌ Resume file not found.")
        return None


def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group() if match else None


def extract_mobile(text):
    match = re.search(r"\b[6-9]\d{9}\b", text)
    return match.group() if match else None


def extract_name(text):
    lines = text.strip().split("\n")
    for line in lines[:3]:  # usually name is at top
        if len(line.split()) <= 4 and line.isalpha() is False:
            return line.strip()
    return None


def extract_skills(text, skill_keywords):
    found_skills = []
    text_lower = text.lower()

    for skill in skill_keywords:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


def extract_education(text):
    education_keywords = [
        "b.e", "b.tech", "m.tech", "mca", "bca",
        "b.sc", "m.sc", "mba", "phd"
    ]

    text_lower = text.lower()
    for edu in education_keywords:
        if edu in text_lower:
            return edu.upper()

    return None
