import sys


def get_instructions(f):
    instr = []
    for line in open(f):
        instr.append([line[:3], int(line[4:])])
    return instr


def run_instructions(instr):
    indexes_run = set()
    acc = 0
    i = 0
    l = len(instr)
    while True:
        if i in indexes_run:
            return acc, False
        if i == l:
            return acc, True
        indexes_run.add(i)
        action, val = instr[i]
        if action == 'acc':
            acc += val
            i += 1
        elif action == 'jmp':
            i += val
        else:
            i += 1


def main(f, part):
    instr = get_instructions(f)
    if part == 'part1':
        acc, smooth_exit = run_instructions(instr)
    elif part == 'part2':
        for i in range(len(instr)):
            action, val = instr[i]
            if action in ('jmp', 'nop'):
                instr[i][0] = {'jmp':'nop', 'nop':'jmp'}[action]
                acc, smooth_exit = run_instructions(instr)
                if smooth_exit:
                    break
                instr[i][0] = action
    return acc


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day08.py <part1|part2> <input_file>\n')
