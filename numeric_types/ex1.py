from random import randint, choice


def guessing_game():
    random_integer = randint(1, 100)
    pr = [0, 100]  # possible range
    prompt = "Guess a number between {l}-{h} (inclusive): "
    while (n := input(prompt.format(l=pr[0], h=pr[1]))) != str(random_integer):
        try:
            if int(n) > random_integer:
                print("Too high!")
                pr[1] = min(int(n)-1, pr[1])
            else:
                print("Too low!")
                pr[0] = max(int(n)+1, pr[0])
        except ValueError:
            print("Not a number, try again!")
    return "You got it!"


# Beyond the exercise
def guessing_game_limited():
    random_integer = randint(1, 100)
    pr = [0, 100]  # possible range
    prompt = "Guess a number between {l}-{h} (inclusive): "
    tries = 0
    while (n := input(prompt.format(l=pr[0], h=pr[1]))) != str(random_integer):
        if (tries := tries + 1) >= 3:
            return "Ran out of tries!"
        try:
            if int(n) > random_integer:
                print("Too high!")
                pr[1] = min(int(n)-1, pr[1])
            else:
                print("Too low!")
                pr[0] = max(int(n)+1, pr[0])
        except ValueError:
            print("Not a number, try again!")
            tries -= 1
    return "You got it!"


def guessing_game_limited_base():
    random_integer = randint(1, 100)
    random_base = randint(2, 16)
    pr = [0, 100]  # possible range
    prompt = "Guess a number between {l}-{h} (inclusive), " \
             f"but represented in base {random_base}: "
    while (n := input(prompt.format(l=pr[0], h=pr[1]))) != str(random_integer):
        try:
            if int(n, random_base) > random_integer:
                print("Too high!")
                pr[1] = min(int(n, random_base)-1, pr[1])
            else:
                print("Too low!")
                pr[0] = max(int(n, random_base)+1, pr[0])
        except ValueError:
            print("Not a number, try again!")
    return "You got it!"


def guessing_game_words():
    with open("./word_list.txt") as words_file:
        words = {w[:-1]: i for i, w in enumerate(list(words_file))}
    index = words[(word := choice(list(words.keys())))]
    least, most = ("use", 499), ("the", 0)
    prompt = "Guess a word at least as frequent as '{0}' but no more " \
             "frequent than '{1}': "
    while (guess := input(prompt.format(least[0], most[0]))) != word:
        try:
            if (guess_index := words[guess]) > index:
                print("Too rare!")
                if guess_index < least[1]:
                    least = (guess, guess_index)
            elif (guess_index := words[guess]) < index:
                print("Too frequent!")
                if guess_index > most[1]:
                    most = (guess, guess_index)
        except KeyError:
            print("Not a word from the list, try again!")
    return "You got it!"


if __name__ == "__main__":
    print(guessing_game())
    print("\nBeyond the exercise\n")
    print(guessing_game_limited(), "\n")
    print(guessing_game_limited_base(), "\n")
    print(guessing_game_words())
