import sys


def read_map(f):
    tmap = []
    for line in open(f):
        tmap.append(line.strip())
    return tmap


def get_location(row, column, tmap):
    mrow = tmap[row]
    while not column < len(mrow):
        column -= len(mrow)
    return mrow[column]


def count_trees(right, down, tmap):
    hits = 0
    c, r = 0, 0
    while r < len(tmap):
        if get_location(r, c, tmap) == '#':
            hits += 1
        c += right
        r += down
    return hits


def main(f, part):
    m = read_map(f)
    if part == 'part1':
        return count_trees(3, 1, m)
    elif part == 'part2':
        p = 1
        for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
            p *= count_trees(right, down, m)
        return p


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day03.py <part1|part2> <input_file>\n')
