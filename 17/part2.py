#!/usr/bin/env python

import itertools

def fill_containers(amount, containers):
  # For every container size left, use it and try to use the rest
  combos = []
  for i, c in enumerate(containers):
    if amount == c:
      # Simply use this container and we're done
      combos.append([c])
      continue

    if amount > c:
      # Use this container and fit the remaining liquid into the
      # remaining containers
      result = fill_containers(amount - c,
                               containers[(i + 1):])

      for r in result:
        combos.append([c] + r)

  return combos

# From the reddit
def fill_containers_gen(amount, containers):
  for i, container in enumerate(containers):
    if amount - container == 0:
      yield [container]

    for tail in fill_containers_gen(amount - container,
                                    containers[(i + 1):]):
      yield [container] + tail


eggnog_amount = 150
containers = []
with open('input', 'r') as f:
  for line in f:
    containers.append(int(line))

containers = list(reversed(sorted(containers)))

# The dumb way
combinations = []
for i in xrange(len(containers)):
  combinations.extend(itertools.combinations(containers, i))

dumb_combos = []
for c in combinations:
  if sum(c) == eggnog_amount:
    dumb_combos.append(c)

print 'There are {} available combos (dumb)'.format(len(dumb_combos))

# The smart way
smart_combos = fill_containers(eggnog_amount, containers)
print 'There are {} available combos (smart):'.format(len(smart_combos))

# The generator way
gen_combos = list(fill_containers_gen(eggnog_amount, containers))
print 'There are {} available combos (gen):'.format(len(gen_combos))

min_containers = min([len(c) for c in smart_combos])
num_min_combos = len([c for c in smart_combos if len(c) == min_containers])

print '{} combos of {} containers'.format(num_min_combos, min_containers)
