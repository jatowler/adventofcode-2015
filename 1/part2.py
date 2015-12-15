#!/usr/bin/env python

with open('input', 'r') as f:
    data = f.read()

cur_floor = 0
floor_map = {}
for pos, move in enumerate(data):
    if move == '(':
        cur_floor = cur_floor + 1

    if move == ')':
        cur_floor = cur_floor - 1

    floor_map[pos] = cur_floor

first_underground_pos = -1
for pos, floor in floor_map.iteritems():
    if floor < 0:
        first_underground_pos = pos
        break

if first_underground_pos < 0:
    print 'Never goes underground'

# Because enumerate() is zero-based, but character positions in this puzzle are
# one-based
print 'First underground floor at position {}'.format(first_underground_pos + 1)
