import sys


def group_generator(f):
    group = []
    for line in open(f):
        if line.strip() == '':
            if len(group) != 0:
                yield group
            group = []
        else:
            group.append(line.strip())
    if len(group) != 0:
        yield group


def groups2sets1(groups):
    for group in groups:
        yess = set()
        for answers in group:
            for answer in answers:
                yess.add(answer)
        yield yess


def groups2sets2(groups):
    for group in groups:
        sets = []
        for answers in group:
            sets.append(set(answers))
        super_set = sets[0]
        for s in sets[1:]:
            super_set = super_set.intersection(s)
        yield super_set


def main(f, part):
    if part == 'part1':
        groups2sets = groups2sets1
    if part == 'part2':
        groups2sets = groups2sets2
    group_answers = list(groups2sets(group_generator(f)))
    return sum(len(g) for g in group_answers)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day06.py <part1|part2> <input_file>\n')
