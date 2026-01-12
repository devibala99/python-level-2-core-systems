from utils import search_documents

DOCUMENTS = {
    1: "Python is a powerful programming language",
    2: "Machine learning uses Python extensively",
    3: "Data science includes statistics and programming",
    4: "Java and Python are popular languages",
    5: "Search engines work on text processing"
}


def display_documents():
    print("\nAvailable Documents:")
    for doc_id, content in DOCUMENTS.items():
        print(f"{doc_id}. {content}")


def main():
    print("🔍 Mini Search Engine (CLI)")
    display_documents()

    query = input("\nEnter search keyword: ").strip()
    if not query:
        print("❌ Search query cannot be empty")
        return

    results = search_documents(DOCUMENTS, query)

    if not results:
        print("\n❌ No matching documents found.")
        return

    print("\n✅ Search Results (Ranked):")
    for doc_id, score, content in results:
        print(f"[Score: {score}] Document {doc_id}: {content}")


if __name__ == "__main__":
    main()
