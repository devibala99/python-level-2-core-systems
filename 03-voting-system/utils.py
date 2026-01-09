def normalize_voter_id(raw_id):
    if not raw_id or len(raw_id) != 8:
        return None
    return raw_id.strip().upper()

def validate_candidate(candidate, candidates):
    return candidate in candidates

def display_results(candidates):
    print("\n📊 Voting Results")
    max_votes = -1
    winner = None

    for name, votes in candidates.items():
        print(f"Candidate {name}: {votes} votes")
        if votes > max_votes:
            max_votes = votes
            winner = name

    print(f"\n🏆 Winner: Candidate {winner}")