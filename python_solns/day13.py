import sys
import math


def get_reqd_mult(a, b, i):
    x = 1
    while (a*x - i) % b != 0:
        x += 1
    return x


def main(f, part):
    f = open(f, 'r')
    etime = int(f.readline().rstrip())
    indexed_buses = [(i, int(z)) for i, z in enumerate(f.readline().split(',')) if z != 'x']
    f.close()
    buses = [x[1] for x in indexed_buses]
    if part == 'part1':
        wait_times = []
        for b in buses:
            m = 0
            while m < etime:
                m += b
            wait_times.append(m - etime)
        min_wait_time = min(wait_times)
        rel_bus = buses[wait_times.index(min_wait_time)]
        print(min_wait_time, rel_bus, min_wait_time*rel_bus)
    elif part == 'part2':
        s = buses[0]
        mults = []
        for i, b in indexed_buses:
            x = 1
            while (s*x - i) % b != 0:
                x += 1
            mults.append(x)
        t = 1
        ns = [1 for i in indexed_buses]
        print(indexed_buses)
        print(ns)
        i, b = indexed_buses[0]
        x = s
        for (i, b), x in zip(indexed_buses, mults):
            pass
#        for i, bus in indexed_buses:
#            sys.stdout.write(f'{i:2d} {bus:3d}\n')
#        c = buses[0]
#        while any( c % (b-i) != 0 for i, b in indexed_buses):
#            for i, b in buses:
#                while c % (b - i) != 0:
#                    c += b
#            c += buses[i]
#            pass


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[2], sys.argv[1])
    else:
        sys.stderr.write('USAGE: python day13.py <part1|part2> <input_file>\n')
