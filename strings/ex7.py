VWLS = "aeiou"


def ubbi_dubbi(word):
    splits, prev = [], 0
    for i, letter in enumerate(word):
        if letter in VWLS:
            splits.append(word[prev:i])
            prev = i
    splits.append(word[prev:])
    return "ub".join(splits)


if __name__ == "__main__":
    print(ubbi_dubbi("octopus"))
    print(ubbi_dubbi("elephant"))
    print(ubbi_dubbi("khszw"))
    print(ubbi_dubbi("khszwu"))
