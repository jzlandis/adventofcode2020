import sys
from itertools import combinations


def get_nums(c, f):
    nums = [int(l) for l in open(f, 'r').readlines()]
    for cnums in combinations(nums, c):
        if sum(cnums) == 2020:
            return cnums


def main(f, part):
    if part == 'part1':
        c = 2
    elif part == 'part2':
        c = 3
    else:
        exit(-1)
    nums = get_nums(c, f)
    p = 1
    for n in nums:
        p *= n
    return p


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day01.py <part1|part2> <input_file>\n')
