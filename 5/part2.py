#!/usr/bin/env python


def contains_double_pair(string):
    import re
    double_pair = re.compile(r'.*(..).*\1.*', re.IGNORECASE)

    return double_pair.match(string)


def contains_aba(string):
    import re
    aba_pattern = re.compile(r'.*(.).\1.*', re.IGNORECASE)

    return aba_pattern.match(string)


def is_nice(string):
    if not contains_double_pair(string):
        print '  Fails to contain double pair'
        return False

    if not contains_aba(string):
        print '  Fails to contain aba pattern'
        return False

    return True

nice_strings = 0
naughty_strings = 0

with open('input', 'r') as f:
    for line in f:
        clean_line = line[:-1]
        print 'Testing {}'.format(clean_line)
        if is_nice(clean_line):
            nice_strings = nice_strings + 1
        else:
            naughty_strings = naughty_strings + 1

print 'Found {} nice strings'.format(nice_strings)
print 'Found {} naughty strings'.format(naughty_strings)
