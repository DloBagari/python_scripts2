from sys import argv, exit
import re
from collections import defaultdict


def word_index(filename, pattern):
    """find location of a pattern in each line in a file, using dictionary"""
    result = {}
    word_reg = re.compile(pattern)
    with open(filename, encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            for match in word_reg.finditer(line):
                word = match.group()
                word_start_index = match.start() + 1
                word_location = (line_number, word_start_index)
                # setdefault: preform searching and adding key  in one lookup
                result.setdefault(word, []).append(word_location)
    return result


def word_index2(filename, pattern):
    """find location of a pattern in each line in a file, using defaultdict"""
    result = defaultdict(list)
    word_reg = re.compile(pattern)
    with open(filename, encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            for match in word_reg.finditer(line):
                word = match.group()
                word_start_index = match.start() + 1
                word_location = (line_number, word_start_index)
                result[word].append(word_location)
    return result


if __name__ == "__main__":
    if len(argv) != 2:
        print("usage: word_index.py 'fileName'")
        exit()
    words = word_index("/home/ubuntu/output.txt", r"(\W|^)\w{3}\s")
    for w in sorted(words, key=str.lower):
        print(w.strip(), words[w])
