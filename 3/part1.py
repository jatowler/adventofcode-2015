#!/usr/bin/env python

with open('input', 'r') as f:
    data = f.read()

gifts = {}

# Deliver the first present
cur_x = 0
cur_y = 0
gifts[(cur_x, cur_y)] = 1

for direction in data:
    if direction == '^':
        cur_y = cur_y + 1
    elif direction == 'v':
        cur_y = cur_y - 1
    elif direction == '>':
        cur_x = cur_x + 1
    elif direction == '<':
        cur_x = cur_x - 1
    else:
        continue

    cur_pos = (cur_x, cur_y)
    if cur_pos in gifts:
        gifts[cur_pos] = gifts[cur_pos] + 1
    else:
        gifts[cur_pos] = 1

    print '{} Position {} now has {} gifts'.format(direction, cur_pos, gifts[cur_pos])

print '{} houses got at least one present'.format(len(gifts))
