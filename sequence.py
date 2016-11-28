"""This is a comment for the module."""
__author__ = "Gabor Racz"
__version__ = "1.0"


def text_to_sentances(text):
    """ from text to stentances """
    sentances = []
    for punct in ".?":
        text = text.strip().replace(punct, "!")
    for sentance in text.split("!"):
        sentances.append(sentance.strip())
    return sentances


def to_words(sentance):
    words = sentance.split()
    stripped_words = []
    for word in words:
        stripped_words.append(word.strip(",;:()"))
    return stripped_words


def process(file_):
    out = []
    text = open(file_).read()
    for sentance in text_to_sentances(text):
        words = to_words(sentance)
        out.append(words)
    return out


def joefy(line):
    out = []
    for i in line:
        for j in i:
            if i.index(j) != 0 and j.istitle():
                out.append("Joe")
            else:
                out.append(j)
    return out


def game(file_):
    for i in process(file_):
        for j in i:
            if i.index(j) == 4:
                word = i[4]
                print(word)
                print(word[:(len(word)-1)/2] + "*" * len(word[len(word)/2:]))
            else:
                print(j)

def symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def transpose(matrix):
    out = []
    for i in range(len(matrix[0])):
        line = []
        for j in range(len(matrix)):
            line.append(matrix[j][i])
        out.append(line)
    return out


def nested_transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


def func(line, string):
    return [x for x in line if x.startswith(string)]


def process_data(filename):
    data = {}
    file_ = open(filename)
    for line in file_:
        title, year, genres = line.strip().split("\t")
        title = title.strip()
        year = int(year)
        genres = genres.split(",")
        for genre in genres:
            if genre not in data:
                data[genre] = []
            data[genre].append((title, year))
    return data
