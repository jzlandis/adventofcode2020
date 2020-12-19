import sys


def make_parser(ispan, lhalf):
    def parse_row(code, span=ispan):
        if len(code) == 1:
            if code[0] == lhalf:
                return int(span[0])
            else:
                return int(span[1]-1)
        else:
            if code[0] == lhalf:
                span = (span[0], sum(span)/2)
            else:
                span = (sum(span)/2, span[1])
            return parse_row(code[1:], span=span)
    return parse_row


parse_row = make_parser((0, 128), 'F')
parse_column = make_parser((0, 8), 'L')


def main(f, part):
    outcomes = []
    for line in open(f):
        row = parse_row(line.strip()[:7])
        column = parse_column(line.strip()[7:])
        ID = row*8 + column
        outcomes.append((line.strip(), row, column, ID))
    if part == 'part1':
        return max(outcomes, key=lambda x: x[3])[-1]
    if part == 'part2':
        IDs = sorted(x[-1] for x in outcomes)
        for i in range(IDs[0], IDs[-1]+1):
            if not i in IDs and i-1 in IDs and i+1 in IDs:
                return i


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day05.py <part1|part2> <input_file>\n')
