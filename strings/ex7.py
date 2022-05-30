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


if __name__ == "__main__":
    print(ubbi_dubbi("octopus"))
    print(ubbi_dubbi("elephant"))
    print(ubbi_dubbi("khszw"))
    print(ubbi_dubbi("khszwu"))
    print("\nBeyond the exercise\n")
    print(ubbi_dubbi_capitalized("octopus"))
    print(ubbi_dubbi_capitalized("Octopus"))