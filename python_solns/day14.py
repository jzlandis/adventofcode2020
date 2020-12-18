import sys
from itertools import product


mem = dict()
mask = None
def parse_input1(f):
    global mask
    for line in open(f):
        if line.startswith('mask'):
            mask = line.split()[-1]
        else:
            yield int(line[line.index('[')+1:line.index(']')]), bin(int(line.split()[-1]))


def parse_input2(f):
    global mask
    for line in open(f):
        if line.startswith('mask'):
            mask = line.split()[-1]
        else:
            yield bin(int(line[line.index('[')+1:line.index(']')])), int(line.split()[-1])


def apply_mask1(b):
    b = list(b[2:])
    b = ['0',]*(36-len(b)) + b
    for i, m in enumerate(mask[::-1]):
        b[-(i+1)] = b[-(i+1)] if m == 'X' else m
    return eval('0b' + ''.join(b))


def get_float_combos(b):
    b = list(b)
    indexes = [i for i in range(len(b)) if b[i] == 'X']
    for subs in product(*([('0','1'),]*len(indexes))):
        for i, s in zip(indexes, subs):
            b[i] = s
        yield b


def apply_mask2(b):
    b = list(b[2:])
    b = ['0',]*(36-len(b)) + b
    for i, m in enumerate(mask[::-1]):
        b[-(i+1)] = m if m in ('X', '1') else b[-(i+1)]
    return set([eval('0b' + ''.join(c)) for c in get_float_combos(b)])


def main(f, part):
    if part == 'part1':
        for i, b in parse_input1(f):
            mem[i] = apply_mask1(b)
        print(sum(mem.values()))
    elif part == 'part2':
        for i, b in parse_input2(f):
            for m in apply_mask2(i):
                mem[m] = b
        print(sum(mem.values()))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[2], sys.argv[1])
    else:
        sys.stderr.write('USAGE: python day14.py <part1|part2> <input_file>\n')
