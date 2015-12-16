#!/usr/bin/env python

def parse_reindeer(specs):
  tokens = specs.split(' ')

  # name, speed, flight time, rest time
  return (tokens[0], int(tokens[3]), int(tokens[6]), int(tokens[13]))

def calc_distance(time, specs):
  flight_plus_rest = specs[2] + specs[3]
  # Number of full flights
  full_flights = time / flight_plus_rest

  # Time left over after all full flights
  time_left = time % flight_plus_rest

  final_flight_time = min(time_left, specs[2])

  return full_flights * (specs[1] * specs[2]) + final_flight_time * specs[1]

def calc_points(time, reindeers):
  # Just simulate the whole thing
  points = {r[0]: 0 for r in reindeers}
  pos = {r[0]: 0 for r in reindeers}

  for i in xrange(1,time + 1):
    for r in reindeers:
      pos[r[0]] = calc_distance(i, r)

    max_pos = max(pos.values())
    for r in pos:
      if pos[r] == max_pos:
        points[r] = points[r] + 1

  return points

reindeers = []

with open('input', 'r') as f:
  for line in f:
    if line.endswith('\n'):
      line = line[:-1]
    
    reindeer = parse_reindeer(line)
    reindeers.append(reindeer)

race_length = 2503

points = calc_points(race_length, reindeers)
print points
print max(points.values())
