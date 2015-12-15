#!/usr/bin/env python


def ribbon_length(line_string):
    (l, w, d) = [int(x) for x in line_string.split('x')]

    # Unique perimeters; each occurs twice on the prism
    perimeters = [2 * l + 2 * w,
                  2 * l + 2 * d,
                  2 * w + 2 * d]

    # Wrap around smallest perimeter
    wrap_length = min(perimeters)

    # Equal to volume in cubic feet
    bow_length = l * w * d

    return wrap_length + bow_length

total_ribbon_length = 0

with open('input', 'r') as f:
    for line in f:
        cur_length = ribbon_length(line)
        total_ribbon_length = total_ribbon_length + cur_length
        print cur_length

print 'Total ribbon length is {} feet'.format(total_ribbon_length)
