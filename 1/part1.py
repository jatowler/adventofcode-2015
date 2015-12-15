#!/usr/bin/env python

with open('input', 'r') as f:
    data = f.read()

final_floor = data.count('(') - data.count(')')

print 'The final floor is {}'.format(final_floor)
