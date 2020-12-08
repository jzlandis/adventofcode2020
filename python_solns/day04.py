import sys
import re
import functools


int4match = re.compile('\d{4}')
def int4_validator(low, high):
    def sub_validator(s):
        match = int4match.findall(s)
        if len(match) != 1:
            return False
        match = match[0]
        if len(match) != len(s):
            return False
        match = int(match)
        if match < low or match > high:
            return False
        return True
    return sub_validator


hgtmatch = re.compile('(\d+cm)|(\d+in)')
def hgt_validator(s):
    match = hgtmatch.findall(s)
    if len(match) != 1:
        return False
    if match[0][0] != '':
        match = match[0][0]
    else:
        match = match[0][1]
    if len(match) != len(s):
        return False
    value = int(match[:-2])
    if match[-2:] == 'cm' and (value < 150 or value > 193):
        return False
    if match[-2:] == 'in' and (value < 59 or value > 76):
        return False
    return True


hclmatch = re.compile('#[0-9a-f]{6}')
def hcl_validator(s):
    match = hclmatch.findall(s)
    if len(match) != 1:
        return False
    match = match[0]
    if len(match) != len(s):
        return False
    return True


eyecolors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


pidmatch = re.compile('\d{9}')
def pid_validator(s):
    match = pidmatch.findall(s)
    if len(match) != 1:
        return False
    match = match[0]
    if len(match) != len(s):
        return False
    return True


validators = {'byr': int4_validator(1920, 2002),
              'iyr': int4_validator(2010, 2020),
              'eyr': int4_validator(2020, 2030),
              'hgt': hgt_validator,
              'hcl': hcl_validator,
              'ecl': lambda s: s in eyecolors,
              'pid': pid_validator,
              }


headers = set(validators.keys())


def pp_gen(f, check_values=False):
    """generate passports from input"""
    pp = set()
    for line in open(f):
        if line.strip() == '' and not len(pp) == 0:
            yield pp
            pp = set()
        else:
            for pair in line.split():
                if not check_values:
                    pp.add(pair.split(':')[0])
                else:
                    key, value = pair.split(':')
                    if key in headers and validators[key](value):
                        pp.add(key)
    if not len(pp) == 0:
        yield pp


def main(part, f):
    valid = 0
    for pp in pp_gen(f, check_values=(part=='part2')):
        if len(headers.difference(pp)) == 0:
            valid += 1
    print(valid)


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] in ('part1', 'part2'):
        main(sys.argv[1], sys.argv[2])
    else:
        sys.stderr.write('USAGE: python day04.py <part1|part2> <input_file>\n')
