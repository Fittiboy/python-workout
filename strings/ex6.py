from ex5 import pig_latin


def pl_sentence(sentence):
    return " ".join(pig_latin(word) for word in sentence.split())


if __name__ == "__main__":
    print(pl_sentence("this is a test translation"))