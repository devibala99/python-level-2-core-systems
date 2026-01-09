from utils import (
    normalize_voter_id,
    validate_candidate,
    display_results
)

candidates = {
    "A": 0,
    "B": 0,
    "C": 0
}

registered_voters = set()
voted_voters = set()   


def register_voter():
    voter_id_input = input("Enter voter ID: ")
    voter_id = normalize_voter_id(voter_id_input)

    if not voter_id:
        print("❌ Invalid voter ID")
        return

    if voter_id in registered_voters:
        print("⚠️ Voter already registered")
        return

    registered_voters.add(voter_id)
    print(f"✅ Voter {voter_id} registered successfully")


def cast_vote():
    voter_id_input = input("Enter voter ID: ")
    voter_id = normalize_voter_id(voter_id_input)

    if not voter_id:
        print("❌ Invalid voter ID")
        return

    if voter_id not in registered_voters:
        print("❌ Voter not registered")
        return

    if voter_id in voted_voters:
        print("❌ You have already voted")
        return

    candidate_choice = input("Vote for candidate (A/B/C): ").strip().upper()

    if not validate_candidate(candidate_choice, candidates):
        print("❌ Invalid candidate")
        return

    candidates[candidate_choice] += 1
    voted_voters.add(voter_id)

    print("🗳️ Vote cast successfully")


def show_results():
    display_results(candidates)


def show_menu():
    print("\n🗳️ Voting System")
    print("1. Register Voter")
    print("2. Cast Vote")
    print("3. Show Results")
    print("4. Exit")


while True:
    show_menu()

    try:
        choice = int(input("Enter choice (1-4): "))

        if choice == 4:
            print("👋 Exiting Voting System")
            break

        elif choice == 1:
            register_voter()
        elif choice == 2:
            cast_vote()
        elif choice == 3:
            show_results()
        else:
            print("❌ Invalid choice")

    except ValueError:
        print("❌ Enter numeric value only")
