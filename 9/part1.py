#!/usr/bin/env python

import itertools

def parse(string):
  import re

  # The format is "<src> to <dest> = <cost>"
  route = re.compile(r'(.*) to (.*) = (\d+)', re.IGNORECASE)
  match = route.match(string)
  if match is None:
    print '***INVALID INPUT***'
    return None

  return (match.group(1), match.group(2), int(match.group(3)))

routes = {}

with open('input', 'r') as f:
  for line in f:
    if line.endswith('\n'):
      line = line[:-1]

    route = parse(line)

    if route[0] not in routes:
      routes[route[0]] = {}

    routes[route[0]][route[1]] = route[2]

    if route[1] not in routes:
      routes[route[1]] = {}

    routes[route[1]][route[0]] = route[2]

# Instead of running a complete Djikstra's, there aren't that many paths, so
# just get every possible permutation
plans = itertools.permutations(routes.keys())

min_cost = float('inf')
shortest_plan = []
for plan in plans:
  cost = 0
  for (src,dst) in zip(plan[:-1], plan[1:]):
    cost = cost + routes[src][dst]
   
  if cost < min_cost:
    min_cost = cost
    shortest_plan = plan

print 'Cheapest route costs {}'.format(min_cost)
print '{}'.format(shortest_plan)
