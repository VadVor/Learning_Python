import string
import sys
import collections


def countvolues(vol):
    return vol[1]

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename, encoding="UTF-8"):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1
for word in sorted(words.items(), key=countvolues, reverse=True):
    print("'{0}' встречается {1} раз".format(word[0], word[1]))



