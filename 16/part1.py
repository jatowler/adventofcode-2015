#!/usr/bin/env python

def parse_sue(string):
  import regex

  sue_pattern = regex.compile(r'Sue (\d+): ( ?(\w+): (\d+),?)+')
  match = sue_pattern.match(string)
  sue_num = match.captures(1)[0]
  attributes = {k:int(v) for k,v in zip(match.captures(3),
                                   match.captures(4))}

  return (sue_num, attributes)

def match_sue(sue, clues):
  for k,v in sue.iteritems():
    if clues[k] != v:
      print '  sue has {} {}, but clues have {}'.format(v, k, clues[k])
      return False

  return True

sues = {}

with open('input', 'r') as f:
  for line in f:
    if line.endswith('\n'):
      line = line[:-1]

    sue = parse_sue(line)
    sues[sue[0]] = sue[1]

clues = {'children': 3,
         'cats': 7,
         'samoyeds': 2,
         'pomeranians': 3,
         'akitas': 0,
         'vizslas': 0,
         'goldfish': 5,
         'trees': 3,
         'cars': 2,
         'perfumes': 1}

for sue_num, sue in sues.iteritems():
  print 'testing sue {}'.format(sue_num)
  if match_sue(sue, clues):
    print sue_num, sue
    break
