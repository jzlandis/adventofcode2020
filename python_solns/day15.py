import sys


def main(f, part):
    if part == 'part1':
        goal = 2020
    else:
        goal = 30000000
    spoken = [int(x) for x in open(f).readlines()[0].split(',')]
    indexes = {n:spoken.index(n) for n in spoken}
    t = len(spoken)
    prev = spoken[-1]
    while t < goal:
        i = indexes.get(prev, None)
        indexes[prev] = t - 1
        if i is None or i == t - 1:
            prev = 0
        else:
            prev = t - i - 1
        spoken.append(prev)
        t += 1
    print(prev)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[2], sys.argv[1])
    else:
        sys.stderr.write('USAGE: python day15.py <part1|part2> <input_file>\n')
