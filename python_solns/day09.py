import sys
from itertools import combinations


def check_for_combinations(p25, num):
    for n1, n2 in combinations(p25, 2):
        if n1 != n2 and n1 + n2 == num:
            return n1, n2


def main(f, part):
    nums = [int(l) for l in open(f).readlines()]
    i = 25
    while True:
        sum_pair = check_for_combinations(nums[i-25:i], nums[i])
        if sum_pair is None:
            break
        i += 1
    p1num = nums[i]
    if part == 'part1':
        return p1num
    elif part == 'part2':
        i0, i1 = 0, 2
        while True:
            contig_range = nums[i0:i1]
            s = sum(contig_range)
            if s < p1num:
                i1 += 1
            elif s == p1num:
                break
            else:
                if i1 - i0 == 2:
                    i1 += 1
                else:
                    i0 += 1
        return min(contig_range) + max(contig_range)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day09.py <part1|part2> <input_file>\n')
