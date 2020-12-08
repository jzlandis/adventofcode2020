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


def main(f, right, down):
    treecount = count_trees(right, down, read_map(f))
    sys.stdout.write(f'TREES HIT: {treecount:d}\n')


if __name__ == '__main__':
    if len(sys.argv) > 3:
        main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    else:
        sys.stderr.write('USAGE: python day03.py <input_file> <right> <down>\n')
