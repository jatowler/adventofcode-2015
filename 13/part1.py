#!/usr/bin/env python

import itertools

def parse_edge(string):
  tokens = string.split(' ')
  if tokens[2] == 'gain':
    gain = int(tokens[3])
  elif tokens[2] == 'lose':
    gain = -int(tokens[3])
  else:
    print '***INVALID INPUT***'
    return None

  return (tokens[0], tokens[-1][:-1], gain)

def arrangement_cost(edges, order):
  cost = 0

  pairs = zip(order, order[1:] + (order[0],))
  for pair in pairs:
    cost = cost + edges[pair[0]][pair[1]]
    cost = cost + edges[pair[1]][pair[0]]

  return cost

edges = {}

with open('input', 'r') as f:
  for line in f:
    if line.endswith('\n'):
      line = line[:-1]

    edge = parse_edge(line)
    if edge[0] not in edges:
      edges[edge[0]] = {}

    edges[edge[0]][edge[1]] = edge[2]

max_cost = -float('inf')
best_p = None
for p in itertools.permutations(edges.keys()):
  p_cost = arrangement_cost(edges, p)
  if p_cost > max_cost:
    max_cost = p_cost
    best_p = p

print best_p
print max_cost
