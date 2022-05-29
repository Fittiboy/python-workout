def pig_latin(word):
    return word+"way" if (s := word[0]) in VWLS else word[1:]+s+"ay"


# Beyond the exercise
def pig_latin_capitals(word):
    new = word+"way" if (s := word[0].lower()) in VWLS else word[1:]+s+"ay"
    return new.title() if word.title() == word else new


def pig_latin_capitals_punctuation(word):
    punctuation = ""
    if word[-1] in '.,?!':
        word, punctuation = word[:-1], word[-1]
    new = word+"way" if (s := word[0].lower()) in VWLS else word[1:]+s+"ay"
    new += punctuation
    return new.title() if word.title() == word else new


def alternate_pig_latin(word):
    punctuation = ""
    if word[-1] in '.,?!':
        word, punctuation = word[:-1], word[-1]
    vowels = set(letter for letter in word if letter in VWLS)
    way = (len(vowels) > 1 or (s := word[0].lower()) in VWLS)
    new = word+"way" if way else word[1:]+s+"ay"
    new += punctuation
    return new.title() if word.title() == word else new


if __name__ == "__main__":
    VWLS = "aeiou"
    print(pig_latin("python"))
    print(pig_latin("eat"))
    print("\nBeyond the exercise\n")
    print(pig_latin_capitals("Python"))
    print(pig_latin_capitals("python"))
    print(pig_latin_capitals("Eat"))
    print(pig_latin_capitals("eat"), "\n")
    print(pig_latin_capitals_punctuation("Python"))
    print(pig_latin_capitals_punctuation("Python."))
    print(pig_latin_capitals_punctuation("Eat"))
    print(pig_latin_capitals_punctuation("Eat,"), "\n")
    print(alternate_pig_latin("Wine."))
    print(alternate_pig_latin("Wind."))
