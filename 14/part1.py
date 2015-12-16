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

reindeers = []

with open('input', 'r') as f:
  for line in f:
    if line.endswith('\n'):
      line = line[:-1]
    
    reindeer = parse_reindeer(line)
    reindeers.append(reindeer)

race_length = 2503

max_distance = -1
for reindeer in reindeers:
  distance = calc_distance(race_length, reindeer)
  if distance > max_distance:
    max_distance = distance

print max_distance
