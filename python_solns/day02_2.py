import sys
from operator import xor


def parse_line(line):
    cs = line.split()[0]
    cl, ch = [int(x) for x in cs.split('-')]
    l = line.split()[1][0]
    pw = line.split()[-1]
    return cl, ch, l, pw


def check_pw(cl, ch, l, pw):
    return xor(pw[cl-1] == l, pw[ch-1] == l)


def main(f):
    passes, fails = 0, 0
    for line in open(f):
        cl, ch, l, pw = parse_line(line)
        if check_pw(*parse_line(line)):
            passes += 1
        else:
            fails += 1
    sys.stdout.write(f'PASSES: {passes:d}; FAILS: {fails:d}\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.stderr.write('USAGE: python day02_2.py <input_list>\n')
