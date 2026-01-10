from utils import scan_files, dry_run, organize_files


def show_menu():
    print("\n📁 File Organizer")
    print("1. Dry Run (Preview)")
    print("2. Organize Files")
    print("3. Exit")


def main():
    folder_path = input("Enter folder path to organize: ").strip()

    while True:
        show_menu()
        try:
            choice = int(input("Enter choice (1-3): "))

            if choice == 3:
                print("👋 Exiting File Organizer")
                break

            files = scan_files(folder_path)

            if choice == 1:
                dry_run(files, folder_path)

            elif choice == 2:
                confirm = input("Are you sure you want to organize files? (yes/no): ").lower()
                if confirm == "yes":
                    organize_files(files, folder_path)
                else:
                    print("❌ Operation cancelled.")

            else:
                print("❌ Invalid choice")

        except ValueError:
            print("❌ Enter numeric value only")


if __name__ == "__main__":
    main()
