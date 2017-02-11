import sys
import unicodedata


def print_unicode_table(words):
    filename = "unicode-table.txt"
    with open(filename, "w", encoding="utf8") as file:
        file.write("decimal   hex   chr  {0:^40}\n".format("name"))
        file.write("-------  -----  ---  {0:-<40}\n".format(""))

        for k in words[0]:
            word = k.lower()
            code = ord(" ")
            end = min(0xD800, sys.maxunicode)  # Stop at surrogate pairs
            while code < end:
                c = chr(code)
                name = unicodedata.name(c, "*** unknown ***")
                if word in name.lower():
                    file.write("{0:7}  {0:5X}  {0:^3c}  {1}\n".format(
                        code, name.title()))
                code += 1
    print("wrote results to", filename)

l_words = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string1] [stringN]".format(sys.argv[0]))
        l_words = None
    else:
        l_words.append(sys.argv[1::])
if l_words is not None:
    print_unicode_table(l_words)
