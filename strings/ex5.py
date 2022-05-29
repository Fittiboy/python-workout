def pig_latin(word):
    return word+"way" if (s := word[0]) in "aeiou" else word[1:]+s+"ay"


# Beyond the exercise


if __name__ == "__main__":
    print(pig_latin("python"))
    print(pig_latin("eat"))
