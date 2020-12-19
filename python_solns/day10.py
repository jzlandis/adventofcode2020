import sys
from collections import defaultdict


def main(f, part):
    joltages = [int(l) for l in open(f).readlines()]
    mnj = min(joltages)
    mxj = max(joltages)
    joltages.append(mxj+3)
    sj = sorted(joltages)
    if part == 'part1':
        diffs = []
        c1, c3 = 0, 0
        for i in range(len(sj)):
            if i == 0:
                diffs.append(sj[i] - 0)
                i0 = 0
                i1 = sj[i]
            else:
                i0, i1 = sj[i-1:i+1]
                diffs.append(i1 - i0)
            if diffs[-1] == 1:
                c1 += 1
            elif diffs[-1] == 3:
                c3 += 1
        return diffs.count(1) * diffs.count(3)
    elif part == 'part2':
        # part 2 soln uses the elegant solution from u/daggerdragon found at:
        # https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfcxuxf/?utm_source=reddit&utm_medium=web2x&context=3
        sj = [0,] + sj
        paths = defaultdict(int)
        paths[0] = 1
        for a in sj:
            for j in range(1, 4):
                if a + j in sj:
                    paths[a + j] += paths[a]
        return paths[sj[-1]]


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day10.py <part1|part2> <input_file>\n')
