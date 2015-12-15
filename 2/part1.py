#!/usr/bin/env python


def area(line_string):
    (l, w, d) = [int(x) for x in line_string.split('x')]

    sides = [l * w,
             l * d,
             w * d]

    smallest_side = min(sides)

    return 2 * sum(sides) + smallest_side

total_area = 0

with open('input', 'r') as f:
    for line in f:
        cur_area = area(line)
        total_area = total_area + cur_area
        print cur_area

print 'Total area is {}'.format(total_area)
