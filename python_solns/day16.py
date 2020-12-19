import sys
import re


n = re.compile('\d+')
def ranges2set(s):
    ns = [int(x) for x in n.findall(s)]
    oset = set(range(ns[0], ns[1]+1))
    oset.update(set(range(ns[2], ns[3]+1)))
    return oset


def get_input(f):
    overall_valid = set()
    field_allowables = {}
    nearby_tickets = []
    my_ticket = []
    mode = 0
    for line in open(f):
        if line.strip() == '':
            mode += 1
            continue
        if mode == 0:
            l = line.split(':')[0]
            s = ranges2set(line)
            field_allowables[l] = s
            overall_valid.update(s)
        elif mode == 1 and not line.startswith('your'):
            pass
        elif mode == 2 and not line.startswith('nearby'):
            nearby_tickets.append([int(x) for x in line.split(',')])
    return overall_valid, field_allowables, my_ticket, nearby_tickets


def work_out_fields(field_allowables, nearby_tickets):
    vals_at_index = [set() for i in nearby_tickets[0]]
    for t in nearby_tickets:
        for i, v in enumerate(t):
            vals_at_index[i].add(v)
    possible_field_labels = [set() for i in nearby_tickets[0]]
    print(sorted(vals_at_index[0]))
    print(sorted(vals_at_index[1]))
    for i, vals in enumerate(vals_at_index):
        for label, allowables in sorted(field_allowables.items()):
            if vals.issubset(allowables):
                sys.stderr.write(f'values at index {i:2d} of tickets are subset of allowable for {label:s}\n')
                possible_field_labels[i].add(label)
    field_labels = []
    for i, pfl in enumerate(possible_field_labels):
        field_labels.append(set(pfl))
        for j in range(len(possible_field_labels)):
            if j != i:
                field_labels[i].difference_update(possible_field_labels[j])
    print(field_labels)
    return field_labels


def main(f, part):
    overall_valid, field_allowables, my_ticket, nearby_tickets = get_input(f)
    if part == 'part1':
        invalid = 0
        for t in nearby_tickets:
            for x in t:
                if not x in overall_valid:
                    invalid += x
        return invalid
    elif part == 'part2':
        nearby_tickets = [t for t in nearby_tickets if all(x in overall_valid for x in t)]
        field_labels = work_out_fields(field_allowables, nearby_tickets)
        prod = 1
        for i, label in enumerate(field_labels):
            if label.startswith('departure'):
                prod *= my_ticket[i]
        return prod


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day16.py <part1|part2> <input_file>\n')
