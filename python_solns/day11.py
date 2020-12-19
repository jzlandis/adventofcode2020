import sys
import time


def print_seatmap(seatmap):
    rtrans = {0: 'L', 1: '#', 2: '.'}
    sys.stderr.write('  ')
    for i in range(len(seatmap[0])):
        sys.stderr.write(f'{str(i)[-1]:s}')
    sys.stderr.write('\n')
    for i, r in enumerate(seatmap):
        sys.stderr.write(f'{str(i)[-1]:s} {"".join(rtrans[c] for c in r):s}\n')


def read_seat_map(f):
    #  0 = empty
    #  1 = occupied
    #  2 = floor
    trans = {'L': 0, '#': 1, '.': 2}
    seatmap = []
    for line in open(f):
        row = [trans[c] for c in line.rstrip()]
        seatmap.append(row)
    return len(seatmap), len(seatmap[0]), seatmap


def get_check_indexes(length, i):
    if i == 0:
        return (0, 1)
    elif i == length - 1:
        return (i - 1, i)
    else:
        return (i - 1, i, i + 1)


def check_adjacent_empty1(seatmap, rows, columns, i, j):
    rs = get_check_indexes(rows, i)
    cs = get_check_indexes(columns, j)
    for r in rs:
        for c in cs:
            if r == i and c == j:
                continue
            if seatmap[r][c] == 1:
                return False
    return True


def check_adjacent_occupied1(seatmap, rows, columns, i, j, count):
    rs = get_check_indexes(rows, i)
    cs = get_check_indexes(columns, j)
    occ = 0
    for r in rs:
        for c in cs:
            if r != i or c != j:
                if seatmap[r][c] == 1:
                    occ += 1
            if occ >= count:
                return True
    return False


def get_next_in_direction(rows, columns, i, j, dir, seatmap):
    di, dj = {0: (-1,  0), 1: (-1,  1), 2: ( 0,  1), 3: ( 1,  1),
              4: ( 1,  0), 5: ( 1, -1), 6: ( 0, -1), 7: (-1, -1)}[dir]
    while True:
        i += di
        j += dj
        if i < 0 or i >= rows or j < 0 or j >= columns:
            return None
        else:
            x = seatmap[i][j]
            if not x == 2:
                return x


def check_adjacent_empty2(seatmap, rows, columns, i, j):
    for dir in range(8):
        if get_next_in_direction(rows, columns, i, j, dir, seatmap) == 1:
            return False
    return True


def check_adjacent_occupied2(seatmap, rows, columns, i, j, count):
    occ = 0
    for dir in range(8):
        if get_next_in_direction(rows, columns, i, j, dir, seatmap) == 1:
            occ += 1
        if occ >= count:
            return True
    return False


def apply_rules(rows, columns, seatmap, mode=1):
    mod_seatmap, change_count = [], 0
    if mode == 1:
        check_adjacent_empty = check_adjacent_empty1
        check_adjacent_occupied = check_adjacent_occupied1
        threshold = 4
    elif mode == 2:
        check_adjacent_empty = check_adjacent_empty2
        check_adjacent_occupied = check_adjacent_occupied2
        threshold = 5
    else:
        raise AssertionError
    for r in range(rows):
        mod_seatmap.append([])
        for c in range(columns):
            #floor: insert a floor marker
            if seatmap[r][c] == 2:
                mod_seatmap[r].append(2)
            #empty seat
            elif seatmap[r][c] == 0:
                #check all adjacent spaces are unoccupied
                if check_adjacent_empty(seatmap, rows, columns, r, c):
                    mod_seatmap[r].append(1)
                    change_count += 1
                else:
                    mod_seatmap[r].append(0)
            #occupied seat
            elif seatmap[r][c] == 1:
                #check for >= 4 adjacent occupied seats
                if check_adjacent_occupied(seatmap, rows, columns, r, c, threshold):
                    mod_seatmap[r].append(0)
                    change_count += 1
                else:
                    mod_seatmap[r].append(1)
            else:
                raise AssertionError(f'invalid seatmap code: {seatmap[r][c]:d} at ({r:d}, {c:d})')
    return mod_seatmap, change_count


def main(f, part):
    if part == 'part1':
        mode = 1
    elif part == 'part2':
        mode = 2
    else:
        raise AssertionError
    rows, columns, seatmap = read_seat_map(f)
    i = 0
    while True:
        i += 1
        seatmap, c = apply_rules(rows, columns, seatmap, mode=mode)
        if c == 0:
            break
    occupied = 0
    for r in range(rows):
        for c in range(columns):
            if seatmap[r][c] == 1:
                occupied += 1
    return occupied


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day11.py <part1|part2> <input_file>\n')
