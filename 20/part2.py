#!/usr/bin/env python

target = 36000000
# Each house gets at least ten times its house number, so we know house
# (target/10) succeeds
max_houses = target / 10
houses = [0 for c in xrange(max_houses)]

# No point in checking more elves than houses
for elf in xrange(1, max_houses):
    for house in xrange(elf, max_houses, elf):
        # Elves only visit 50 houses, so they never see
        # a house higher than 50x their value
        if house > elf * 50:
            break
        
        houses[house] += elf * 11

for i,h in enumerate(houses):
    if h > target:
        print i
        break
