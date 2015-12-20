#!/usr/bin/env python

target = 36000000
max_houses = 1000000
houses = [0 for h in xrange(max_houses)]

# No point in checking more elves than houses
for elf in xrange(1,max_houses):
    for house in xrange(elf, max_houses, elf):
        houses[house] += elf * 10

for i,h in enumerate(houses):
    if h > target:
        print i
        break
