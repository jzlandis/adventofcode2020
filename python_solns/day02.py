import sys
from operator import xor


def parse_line(line):
    cs = line.split()[0]
    cl, ch = [int(x) for x in cs.split('-')]
    l = line.split()[1][0]
    pw = line.split()[-1]
    return cl, ch, l, pw


def check_pw1(cl, ch, l, pw):
    c = pw.count(l)
    return cl <= c <= ch


def check_pw2(cl, ch, l, pw):
    return xor(pw[cl-1] == l, pw[ch-1] == l)


def main(f, part):
    passes, fails = 0, 0
    if part == 'part1':
        check = check_pw1
    elif part == 'part2':
        check = check_pw2
    for line in open(f):
        if check(*parse_line(line)):
            passes += 1
        else:
            fails += 1
    return passes


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day02.py <part1|part2> <input_file>\n')
