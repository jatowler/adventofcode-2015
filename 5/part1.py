#!/usr/bin/env python


def has_three_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Use the below for *unique* vowels ('eee' => 1)
    # vowel_counts = [1 for vowel in vowels if string.find(vowel) != -1]

    # Use the below for *total* vowels ('eee' => 3)
    vowel_counts = [string.count(vowel) for vowel in vowels]

    return sum(vowel_counts) >= 3


def has_double_letter(string):
    import re
    double_letter = re.compile(r'.*(.)\1.*', re.IGNORECASE)

    return double_letter.match(string)


def contains_naughty_strings(string):
    naughty_substrings = ['ab',
                          'cd',
                          'pq',
                          'xy']

    naughty_counts = [string.count(x) for x in naughty_substrings]

    return sum(naughty_counts) > 0


def is_nice(string):
    if not has_three_vowels(string):
        print '  String needs more vowels'
        return False

    if not has_double_letter(string):
        print '  No double letter'
        return False

    if contains_naughty_strings(string):
        print '  Contains naughty strings'
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
