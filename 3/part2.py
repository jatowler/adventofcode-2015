#!/usr/bin/env python

with open('input', 'r') as f:
    data = f.read()

# Store house positions and gift counts
gifts = {}

# Deliver the first present from Santa
# Use list to make it easy to update
santa_pos = [0, 0]
# Lists aren't hashable, but tuples are
gifts[tuple(santa_pos)] = 1

# Deliver the first present from Robo-Santa
# Use list to make it easy to update
robosanta_pos = [0, 0]
# Lists aren't hashable, but tuples are
gifts[tuple(robosanta_pos)] = 1

for pos, direction in enumerate(data):
    if direction == '^':
        change = [0, 1]
    elif direction == 'v':
        change = [0, -1]
    elif direction == '>':
        change = [1, 0]
    elif direction == '<':
        change = [-1, 0]
    else:
        continue

    if (pos % 2) == 0:
        santa_pos[0] = santa_pos[0] + change[0]
        santa_pos[1] = santa_pos[1] + change[1]
        index = tuple(santa_pos)

        # Use default value to create if not present
        gifts[index] = gifts.get(index, 0) + 1

        print 'S{} Position {} now has {} gifts'.format(direction,
                                                        santa_pos,
                                                        gifts[index])
    else:
        robosanta_pos[0] = robosanta_pos[0] + change[0]
        robosanta_pos[1] = robosanta_pos[1] + change[1]
        index = tuple(robosanta_pos)

        # Use default value to create if not present
        gifts[index] = gifts.get(index, 0) + 1

        print 'R{} Position {} now has {} gifts'.format(direction,
                                                        robosanta_pos,
                                                        gifts[index])

print '{} houses got at least one present'.format(len(gifts))
