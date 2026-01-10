from utils import (
    normalize_seat_id,
    is_seat_available,
    book_seat,
    cancel_seat,
    display_seats
)

# GLOBAL STATE (single source of truth)
seats = {
    "A1": {"status": "available", "price": 150},
    "A2": {"status": "available", "price": 150},
    "B1": {"status": "available", "price": 120},
    "B2": {"status": "booked", "price": 120}
}


def show_menu():
    print("\n🎟 Movie Ticket Booking System")
    print("1. View Seats")
    print("2. Book Seat")
    print("3. Cancel Booking")
    print("4. Exit")


def handle_booking():
    raw_id = input("Enter seat ID to book: ")
    seat_id = normalize_seat_id(raw_id)

    if seat_id is None:
        print("❌ Invalid seat format")
        return

    if seat_id not in seats:
        print("❌ Seat does not exist")
        return

    if not is_seat_available(seats, seat_id):
        print("❌ Seat already booked")
        return

    price = book_seat(seats, seat_id)
    print(f"✅ Seat {seat_id} booked successfully. Price: ₹{price}")


def handle_cancellation():
    raw_id = input("Enter seat ID to cancel: ")
    seat_id = normalize_seat_id(raw_id)

    if seat_id is None:
        print("❌ Invalid seat format")
        return

    if seat_id not in seats:
        print("❌ Seat does not exist")
        return

    success = cancel_seat(seats, seat_id)

    if success:
        print(f"✅ Booking for seat {seat_id} cancelled")
    else:
        print("❌ Seat is not booked")


while True:
    show_menu()

    try:
        choice = int(input("Enter choice (1-4): "))

        if choice == 4:
            print("👋 Exiting system")
            break

        elif choice == 1:
            display_seats(seats)

        elif choice == 2:
            handle_booking()

        elif choice == 3:
            handle_cancellation()

        else:
            print("❌ Invalid choice")

    except ValueError:
        print("❌ Enter numbers only")
