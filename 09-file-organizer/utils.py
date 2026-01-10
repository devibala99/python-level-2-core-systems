import os
import shutil

# Rule-based classification
RULES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mkv"],
    "Others": []
}


def scan_files(folder_path):
    """
    Return list of files (skip directories)
    """
    files = []

    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return files

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            files.append(item)

    return files


def classify_file(filename):
    """
    Decide destination folder using file extension
    """
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    for folder, extensions in RULES.items():
        if ext in extensions:
            return folder

    return "Others"


def dry_run(files, folder_path):
    """
    Preview file movements without moving
    """
    if not files:
        print("No files to organize.")
        return

    print("\n🔍 Dry Run Preview:")
    for file in files:
        destination = classify_file(file)
        print(f"{file}  ➜  {destination}/")


def organize_files(files, folder_path):
    """
    Move files safely based on rules
    """
    if not files:
        print("No files to organize.")
        return

    for file in files:
        source_path = os.path.join(folder_path, file)
        destination_folder = classify_file(file)
        destination_path = os.path.join(folder_path, destination_folder)

        # Create destination folder if missing
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        target_file_path = os.path.join(destination_path, file)

        # Prevent overwrite
        if os.path.exists(target_file_path):
            print(f"⚠️ Skipped (already exists): {file}")
            continue

        shutil.move(source_path, target_file_path)
        print(f"✅ Moved: {file} → {destination_folder}/")

    print("\n🎉 File organization completed.")
