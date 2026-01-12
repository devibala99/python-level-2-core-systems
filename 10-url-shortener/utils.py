import random
import string


def generate_short_code(length=6):
    """
    Generate a random alphanumeric short code.
    Example: aZ39xP
    """
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def shorten_url(url_map, long_url):
    """
    Logic:
    - If URL already exists, return existing short code
    - Else generate a unique short code
    """
    # Check if URL already shortened
    for short, original in url_map.items():
        if original == long_url:
            return short

    # Generate unique short code
    while True:
        short_code = generate_short_code()
        if short_code not in url_map:
            url_map[short_code] = long_url
            return short_code


def expand_url(url_map, short_code):
    """
    Return original URL if exists
    """
    return url_map.get(short_code)


def display_all_urls(url_map):
    """
    Display all stored URLs
    """
    if not url_map:
        print("❌ No URLs stored.")
        return

    print("\n🔗 Stored URLs:")
    for short, long in url_map.items():
        print(f"{short} → {long}")
