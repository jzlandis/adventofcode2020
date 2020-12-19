import sys
import re


def funny_eval1(exp):
    v = None
    actions = {'+': lambda x,y: x+y,
               '*': lambda x,y: x*y}
    action = None
    for c in exp.split():
        if v is None:
            v = int(c)
        elif c in ('+', '*'):
            action = actions[c]
        else:
            v = action(v, int(c))
    return v


a = re.compile('\d+ \+ \d+')
def funny_eval2(exp):
    while '+' in exp:
#        print(exp)
        aexp = a.findall(exp)[0]
        exp = exp.replace(aexp, str(eval(aexp)))
#    print(exp)
    return eval(exp)


p = re.compile('\([^(]+?\)')
def line_eval(l, funny):
    while '(' in l:
#        print(l)
        exp = p.findall(l)[0]
        v = funny(exp[1:-1])
        l = l.replace(exp, str(v))
#    print(l)
    return int(funny(l))


def main(f, part):
    if part == 'part1':
        funny = funny_eval1
    elif part == 'part2':
        funny = funny_eval2
    s = 0
    for line in open(f):
        v = line_eval(line, funny)
        #print(line.strip(),'=',v)
        s += line_eval(line, funny)
    return s


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day18.py <part1|part2> <input_file>\n')
