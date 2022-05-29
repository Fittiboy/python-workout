from ex5 import pig_latin


def pl_sentence(sentence):
    return " ".join(map(pig_latin, sentence.split()))


# Beyond the exercise
def nonsense():
    sentence = []
    with open("./nonsense.txt") as ns_file:
        lines = ns_file.read().split('\n')
    for i, line in enumerate(lines[:10]):
        sentence.append(line.split()[i])
    return " ".join(sentence)


if __name__ == "__main__":
    print(pl_sentence("this is a test translation"))
    print("\nBeyond the exercise\n")
    print(nonsense())
