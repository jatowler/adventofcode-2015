#!/usr/bin/env python

target = 36000000
num_houses = 1000000
houses = [0 for c in xrange(num_houses)]

# No point in checking more elves than houses
for elf in xrange(1, num_houses):
    for house in xrange(elf, num_houses, elf):
        # Elves only visit 50 houses, so they never see
        # a house higher than 50x their value
        if house > elf * 50:
            break
        
        houses[house] += elf * 11

for i,h in enumerate(houses):
    if h > target:
        print i
        break
