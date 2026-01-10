import re


def normalize_seat_id(raw_id):
    """
    Normalize and validate seat ID.
    Valid formats: A1, B2, C10, etc.
    """
    if not raw_id:
        return None

    seat_id = raw_id.strip().upper()

    if re.match(r"^[A-Z]\d+$", seat_id):
        return seat_id

    return None


def is_seat_available(seats, seat_id):
    """
    Check if seat exists and is available.
    """
    return seats.get(seat_id, {}).get("status") == "available"


def book_seat(seats, seat_id):
    """
    Book a seat and return its price.
    Assumes validation already done.
    """
    seats[seat_id]["status"] = "booked"
    return seats[seat_id]["price"]


def cancel_seat(seats, seat_id):
    """
    Cancel a booking if seat is booked.
    Returns True if cancelled, else False.
    """
    if seats[seat_id]["status"] == "booked":
        seats[seat_id]["status"] = "available"
        return True
    return False


def display_seats(seats):
    """
    Display seat availability and prices.
    """
    print(f"\n{'SEAT':<8}{'STATUS':<15}{'PRICE':<10}")
    print("-" * 33)

    for seat_id, info in seats.items():
        status = info["status"]
        status_icon = "✅" if status == "available" else "❌"
        price = info["price"]

        print(f"{seat_id:<8}{status.capitalize() + ' ' + status_icon:<15}₹{price:<10}")

    print("-" * 33)
