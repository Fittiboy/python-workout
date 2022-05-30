VWLS = "aeiou"


def ubbi_dubbi(word):
    splits, prev = [], 0
    for i, letter in enumerate(word):
        if letter in VWLS:
            splits.append(word[prev:i])
            prev = i
    return "ub".join(splits + [word[prev:]])


# Beyond the exercise
def ubbi_dubbi_capitalized(word):
    transformed = ubbi_dubbi(word.lower())
    if word[0] == word[0].upper():
        transformed = transformed.title()
    return transformed


def remove_authors(filename, authors):
    with open(filename) as article_file:
        article = article_file.read()
    for author in authors:
        article = article.replace(author, "_")
    return article


def url_encode(string):
    legal = list(range(48, 58)) + list(range(65, 91)) +  \
            list(range(97, 123))

    class Table():
        def __getitem__(self, order):
            if order in legal:
                return chr(order)
            else:
                return "%" + str(hex(order))[2:].upper()
    table = Table()
    return string.translate(table)


if __name__ == "__main__":
    print(ubbi_dubbi("octopus"))
    print(ubbi_dubbi("elephant"))
    print(ubbi_dubbi("khszw"))
    print(ubbi_dubbi("khszwu"))
    print("\nBeyond the exercise\n")
    print(ubbi_dubbi_capitalized("octopus"))
    print(ubbi_dubbi_capitalized("Octopus"), "\n")
    AUTHORS = [
        "Robert Greene",
        "Nassim Nicholas Taleb",
        "George Polya",
        "Roger Penrose"
    ]
    print(remove_authors("./authors.txt", AUTHORS), "\n")
    print(url_encode("This is a non-url-friendly string!"))
