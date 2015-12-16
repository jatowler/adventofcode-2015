#!/usr/bin/env python

import re

pattern = re.compile(r'(.*) (\d+),(\d+) through (\d+),(\d+)', re.IGNORECASE)

def parse_line(string):
  result = pattern.match(string)

  if result is None:
    print '***ERROR: INVALID INPUT***'
    return None

  return (result.group(1),
          (int(result.group(2)),
           int(result.group(3))),
          (int(result.group(4)),
           int(result.group(5))))

def turn_on(grid, start, end):
  for i in xrange(start[0], end[0] + 1):
    for j in xrange(start[1], end[1] + 1):
      grid[i][j] = grid[i][j] + 1

def turn_off(grid, start, end):
  for i in xrange(start[0], end[0] + 1):
    for j in xrange(start[1], end[1] + 1):
      if grid[i][j] > 0:
        grid[i][j] = grid[i][j] - 1

def toggle(grid, start, end):
  for i in xrange(start[0], end[0] + 1):
    for j in xrange(start[1], end[1] + 1):
      grid[i][j] = grid[i][j] + 2

def total_brightness(grid):
  return sum([sum(l) for l in grid])

grid = [[0 for i in xrange(1000)] for j in xrange(1000)]

with open('input', 'r') as f:
  for line in f:
    # Only lop off the last character if it's a newline
    # Otherwise, we might cut off an important number
    # This is probably unnecessary, because the regex will
    # ignore the newline, but this way we sent clean data
    # to the parser
    if line.endswith('\n'):
      line = line[:-1]

    command = parse_line(line)
    if command is None:
      continue

    print command

    if command[0] == 'turn on':
      turn_on(grid, command[1], command[2])
    elif command[0] == 'turn off':
      turn_off(grid, command[1], command[2])
    elif command[0] == 'toggle':
      toggle(grid, command[1], command[2])

print 'The total brightness is {}'.format(total_brightness(grid))
