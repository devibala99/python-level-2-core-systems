def normalize_word(word):
    if not word:
        return None
    return word.strip().lower()


def add_word(dictionary, word, meaning):
    if word in dictionary:
        return False
    dictionary[word] = meaning
    return True


def search_word(dictionary, word):
    return dictionary.get(word)


def update_word(dictionary, word, new_meaning):
    if word not in dictionary:
        return False
    dictionary[word] = new_meaning
    return True


def delete_word(dictionary, word):
    if word not in dictionary:
        return False
    del dictionary[word]
    return True


def suggest_words(dictionary, fragment):
    if not fragment:
        return []
    fragment = fragment.lower()
    starts_with = []
    contains = []

    for word in dictionary:
        if word.startswith(fragment):
            starts_with.append(word)
        elif fragment in word:
            contains.append(word)
    
    return starts_with + contains