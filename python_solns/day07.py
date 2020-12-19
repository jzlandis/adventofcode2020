import sys


def parse_bags(f):
    bag_dict = {}
    for line in open(f):
        bag = '_'.join(line[:line.find('contain')-1].split(' ')[:-1])
        bag_dict[bag] = []
        if 'contain no other bags' in line:
            continue
        for sub_bag_str in line[line.find('contain')+8:].split(','):
            c = int(sub_bag_str.split()[0])
            sub_bag = '_'.join(sub_bag_str.split()[1:-1])
            bag_dict[bag].append((c, sub_bag))
    return bag_dict


def get_sub_bags(bag_dict, bag, multi=False):
    sub_bags = set()
    bag_count = 0
    for c, sub_bag in bag_dict[bag]:
        bag_count += c
        sub_bags.add(sub_bag)
        for _ in range(c if multi else 1):
            scount, sset = get_sub_bags(bag_dict, sub_bag, multi=multi)
            bag_count += scount
            sub_bags.update(sset)
    return bag_count, sub_bags


def main(f, part):
    bag_dict = parse_bags(f)
    if part == 'part1':
        c = 0
        for k in bag_dict.keys():
            if k == 'shiny_gold':
                continue
            bag_count, sub_bags = get_sub_bags(bag_dict, k)
            if 'shiny_gold' in sub_bags:
                c += 1
        return c
    elif part == 'part2':
        bag_count, sub_bags = get_sub_bags(bag_dict, 'shiny_gold', multi=True)
        return bag_count

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(main(sys.argv[2], sys.argv[1]))
    else:
        sys.stderr.write('USAGE: python day07.py <part1|part2> <input_file>\n')
