from utils import shorten_url, expand_url, display_all_urls

url_map = {}


def create_short_url():
    long_url = input("Enter long URL: ").strip()
    if not long_url:
        print("❌ URL cannot be empty.")
        return

    short_code = shorten_url(url_map, long_url)
    print(f"✅ Short URL created: {short_code}")


def open_short_url():
    short_code = input("Enter short code: ").strip()
    original_url = expand_url(url_map, short_code)

    if not original_url:
        print("❌ Short URL not found.")
    else:
        print(f"🌐 Redirecting to: {original_url}")


def show_menu():
    print("\n🔗 URL Shortener")
    print("1. Shorten URL")
    print("2. Open Short URL")
    print("3. View All URLs")
    print("4. Exit")


while True:
    show_menu()

    try:
        choice = int(input("Enter choice (1-4): "))

        if choice == 4:
            print("👋 Exiting URL Shortener")
            break
        elif choice == 1:
            create_short_url()
        elif choice == 2:
            open_short_url()
        elif choice == 3:
            display_all_urls(url_map)
        else:
            print("❌ Invalid choice")

    except ValueError:
        print("❌ Enter numeric value only")
