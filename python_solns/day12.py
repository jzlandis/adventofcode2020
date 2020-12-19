import sys
import numpy as np


lrots = {0: lambda x: x, 90: lambda x: np.array([-x[1], x[0]]),
            180: lambda x: np.array([-x[0], -x[1]]), 270: lambda x: np.array([x[1], -x[0]])}
rrots = {0: lrots[0], 90: lrots[270], 180: lrots[180], 270: lrots[90]}
class waypoint2:
    def __init__(self, e, n, debug=False):
        self.loc = np.array([e, n])
        self.debug = debug
    def trans(self, d, dist):
        if self.debug:
            sys.stderr.write(f'{str(self):s} translated {d:s} {dist:3d} to ')
        self.loc += {'N':np.array([0,  1]), 'E':np.array([ 1, 0]),
                     'S':np.array([0, -1]), 'W':np.array([-1, 0])}[d]*dist
        if self.debug:
            sys.stderr.write(f'{str(self):s}\n')
    def rot(self, d, angle):
        if self.debug:
            sys.stderr.write(f'{str(self):s} rotated    {d:s} {angle:3d} to ')
        if d == 'L':
            foo = lrots[angle]
        elif d == 'R':
            foo = rrots[angle]
        else:
            raise AssertionError
        self.loc = foo(self.loc)
        if self.debug:
            sys.stderr.write(f'{str(self):s}\n')
    def __add__(self, other):
        return self.loc + other
    def __repr__(self):
        return f'waypoint({self.loc[0]:3d}, {self.loc[1]:3d})'


def main(f, part):
    action2add = {'N':np.array([0, 1]), 'E':np.array([1, 0]),
                'S':np.array([0, -1]), 'W':np.array([-1, 0])}
    if part == 'part1':
        pos = np.array([0, 0])
        positions = []
        lorients = 'ENWSENWS'
        rorients = 'ESWNESWN'
        action2add = {'N':np.array([0, 1]), 'E':np.array([1, 0]),
                    'S':np.array([0, -1]), 'W':np.array([-1, 0])}
        orient = 'E'
        for line in open(f, 'r'):
            action = line[0]
            val = int(line.rstrip()[1:])
            if action == 'L':
                orient = lorients[lorients.index(orient) + int(val/90)]
            elif action == 'R':
                orient = rorients[rorients.index(orient) + int(val/90)]
            elif action == 'F':
                pos += action2add[orient]*val
            else:
                pos += action2add[action]*val
            positions.append(np.array(pos))
    elif part == 'part2':
        waypoint = waypoint2(10, 1)
        pos = np.array([0, 0])
        positions = []
        waypoints = []
        for line in open(f, 'r'):
            action = line[0]
            val = int(line.rstrip()[1:])
            if action in ('L', 'R'):
                waypoint.rot(action, val)
            elif action == 'F':
                pos += waypoint.loc*val
            else:
                waypoint.trans(action, val)
            positions.append(np.array(pos))
            waypoints.append(np.array(waypoint.loc) + pos)
    return abs(pos[0]) + abs(pos[1])


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day12.py <part1|part2> <input_file>\n')
