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


def jumble(sentences):
    wordlists = []
    for sentence in sentences:
        wordlists.append(sentence.split())
    return [" ".join(wordlist[i] for wordlist in wordlists)
            for i in range(len(wordlists))]


def apache_log():
    with open("apache_log.txt") as logfile:
        logs = logfile.read().split("\n")
    for line in logs:
        try:
            code = line.split('"')[2].split()[0]
            if code == "404":
                yield line.split()[0]
        except IndexError:
            continue


if __name__ == "__main__":
    print(pl_sentence("this is a test translation"))
    print("\nBeyond the exercise\n")
    print(nonsense(), "\n")
    print(jumble(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']), "\n")
    for ip in apache_log():
        print(ip)
