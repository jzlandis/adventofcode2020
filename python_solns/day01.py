import sys
from itertools import combinations


def get_nums(c, f):
    nums = [int(l) for l in open(f, 'r').readlines()]
    for cnums in combinations(nums, c):
        if sum(cnums) == 2020:
            return cnums


def main(c, f):
    nums = get_nums(c, f)
    p = 1
    for n in nums:
        p *= n
    sys.stdout.write(f'{" ".join("%d" % n for n in nums):s} {p}\n')


if __name__ == '__main__':
    if len(sys.argv) > 2:
        main(int(sys.argv[1]), sys.argv[2])
    else:
        sys.stderr.write('USAGE: python day01.py <count_to_sum> <number_list>\n')
