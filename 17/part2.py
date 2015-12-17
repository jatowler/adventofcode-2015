#!/usr/bin/env python

import itertools

def fill_containers(amount, containers):
  # If we have no containers left, we fail
  if len(containers) == 0:
    return None

  # If our smallest container is too big, we fail
  if containers[-1] > amount:
    return None

  # If all the remaining containers couldn't hold it, we fail
  # This case will actually be handled correctly, but we can
  # catch it explicitly and not worry about it
  if amount > sum(containers):
    return None

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
      new_amount = amount - c
      available_containers = containers[(i + 1):]

      result = fill_containers(new_amount, available_containers)

      if result is None:
        # It can't be done, so add no combos
        continue

      for r in result:
        if type(r) is int:
          combo = [c,r]
        else:
          combo = [c] + r
        combos.append(combo)

  return combos

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

min_containers = min([len(c) for c in smart_combos])
num_min_combos = sum([1 for c in smart_combos if len(c) == min_containers])

print '{} combos of {} containers'.format(num_min_combos, min_containers)
