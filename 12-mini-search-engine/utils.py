def normalize_text(text):
    """
    Convert text to lowercase and strip spaces
    """
    return text.lower().strip()


def search_documents(documents, query):
    """
    Search for query inside documents
    Returns matched documents with relevance score
    """
    query = normalize_text(query)
    results = []

    for doc_id, content in documents.items():
        content_normalized = normalize_text(content)

        if query in content_normalized:
            score = content_normalized.count(query)
            results.append((doc_id, score, content))

    # Sort by relevance score (highest first)
    results.sort(key=lambda x: x[1], reverse=True)
    return results
