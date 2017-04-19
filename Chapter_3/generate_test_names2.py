import random


def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "forenames.txt"), (surnames, "surnames.txt")):
        for name in open(filename, encoding="utf8"):
            names.append(name.rstrip())
    return forenames, surnames

forenames, surnames = get_forenames_and_surnames()
fh = open("test-names2.txt", "w", encoding="utf8")
limit = 100
years = list(range(1970, 2017))*3
for year, forename, surname in zip(random.sample(years, limit), random.sample(forenames, limit), random.sample(surnames, limit)):
    line = "{0} {1} {2}\n".format(forename, surname, year)
    fh.write(line)

