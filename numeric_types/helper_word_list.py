import csv


def make_word_list():
    with open("english-word-list-total.csv") as words_csv:
        word_reader = csv.reader(words_csv, delimiter=';')
        words = [word[1] for word in word_reader if word[0]]
    with open("word_list.txt", "w") as word_list_file:
        for word in words[:100]:
            word_list_file.write(word+"\n")


if __name__ == "__main__":
    make_word_list()
