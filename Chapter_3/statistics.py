import collections
import sys


Statistics = collections.namedtuple("Statistics", "mean mode median std_dev")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "-help"}:
        print("usage: {0} file1 [file2 [...fileN]]".format(sys.argv[0]))
        sys.exit()

    numbers = []
    frequencies = collections.defaultdict(int)
    for filename in sys.argv[1:]:
        read_data(filename, numbers, frequencies)
    if numbers:
        statistics = calculate_statistics(numbers, frequencies)
        print_results(len(numbers), statistics)
    else:
        print("no numbers found")


def read_data(filename, numbers, frequencies):
    for lino, line in enumerate(open(filename, encoding="ascii"), start=1):
        for x in line.split():
            try:
                number = float(x)
                numbers.append(number)
                frequencies[number] += 1
            except ValueError as err:
                print("{0}:{1}: skipping {2}: {3}".format(filename, lino, x, err))


def calculate_statistics(numbers, frequencies):
    mean = sum(numbers) / len(numbers))
    mode = calculate_mode(frequencies, 3)
    median = calculate_median(numbers)
    std_dev = calculate_std_dev(numbers, mean)
    return Statistics(mean, mode, median, std_dev)



