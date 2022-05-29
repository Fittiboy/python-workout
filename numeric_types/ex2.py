def mysum(*numbers):
    partial_sum = 0
    for n in numbers:
        partial_sum += n
    return partial_sum


# Beyond the exercise
def mysum_extended(numbers, starting_point=0):
    for n in numbers:
        starting_point += n
    return starting_point


def avg(numbers):
    total = mysum(*numbers)
    return total / len(numbers)


def word_lengths(words):
    lengths = [len(word) for word in words]
    average_word_length = avg(lengths)
    return (min(lengths), max(lengths), average_word_length)


def cleaned_sum(objects):
    partial_sum = 0
    for obj in objects:
        try:
            partial_sum += int(obj)
        except ValueError:
            pass
    return partial_sum


if __name__ == "__main__":
    print(f"1+3+5+7={mysum(1, 3, 5, 7)}")
    print(f"1+3+5+7+9+11={mysum(1, 3, 5, 7, 9, 11)}")
    print(f"1+3+5+7+9+11+13+15={mysum(1, 3, 5, 7, 9, 11, 13, 15)}")
    print("\nBeyond the exercise:\n")
    print(f"7+(1+3+5)={mysum_extended([1, 3, 5], 7)}")
    print(f"The average of 1, 3, 8 is {avg([1, 3, 8])}")
    word_list = ["this", "is", "an", "incredibly", "nice", "list"]
    shortest, longest, average = word_lengths(word_list)
    print(f"\nThe list of words is {word_list}")
    print(f"The shortest word has {shortest} letters, the longest "
          f"word has {longest} letters, and on average, they have "
          f"{average:.2f} letters!")
    list_of_stuff = ["Word", 3, "9", 8.5, "twelve"]
    print(f"\nOur list of stuff is {list_of_stuff}")
    print(f"The sum of the stuff is {cleaned_sum(list_of_stuff)}")
