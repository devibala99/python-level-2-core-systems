from utils import (
    normalize_word,
    add_word,
    search_word,
    update_word,
    delete_word,
    suggest_words
)

dictionary = {}


def add_new_word():
    word = normalize_word(input("Enter word: "))
    if not word:
        print("❌ Invalid word")
        return

    meaning = input("Enter meaning: ").strip()
    if not meaning:
        print("❌ Meaning cannot be empty")
        return

    if add_word(dictionary, word, meaning):
        print("✅ Word added successfully")
    else:
        print("⚠️ Word already exists")


def search_dictionary():
    word = normalize_word(input("Enter word to search: "))
    meaning = search_word(dictionary, word)

    if meaning:
        print(f"📖 {word}: {meaning}")
    else:
        print("❌ Word not found")
        suggestions = suggest_words(dictionary, word[:2])
        if suggestions:
            print("🔍 Did you mean:", ", ".join(suggestions))


def update_dictionary():
    word = normalize_word(input("Enter word to update: "))
    if word not in dictionary:
        print("❌ Word not found")
        return

    new_meaning = input("Enter new meaning: ").strip()
    update_word(dictionary, word, new_meaning)
    print("✅ Word updated successfully")


def delete_dictionary_word():
    word = normalize_word(input("Enter word to delete: "))
    if delete_word(dictionary, word):
        print("🗑️ Word deleted")
    else:
        print("❌ Word not found")


def show_menu():
    print("\n📘 Dictionary App")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Update Word")
    print("4. Delete Word")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        add_new_word()
    elif choice == "2":
        search_dictionary()
    elif choice == "3":
        update_dictionary()
    elif choice == "4":
        delete_dictionary_word()
    elif choice == "5":
        print("👋 Exiting Dictionary App")
        break
    else:
        print("❌ Invalid choice")
