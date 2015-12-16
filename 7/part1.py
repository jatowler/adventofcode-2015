#!/usr/bin/env python

def parse_line(string):
  import re

  # Looks like 'NOT a -> b'
  unary = re.compile(r'NOT (\w+) -> (\w+)', re.IGNORECASE)
  # Looks like 'a AND b -> c'
  binary = re.compile(r'(\w+) (\w+) (\w+) -> (\w+)', re.IGNORECASE)
  # Looks like 'a -> b'
  raw = re.compile(r'(\w+) -> (\w+)', re.IGNORECASE)

  # Return (destination, op, arguments)

  match = unary.match(string)
  if match:
    return (match.group(2), 'NOT', match.group(1))

  match = binary.match(string)
  if match:
    return (match.group(4), match.group(2), match.group(1), match.group(3))

  match = raw.match(string)
  if match:
    return (match.group(2), 'RAW', match.group(1))

  print '***INVALID INPUT***'
  return None

def resolve(signal, signals, commands, level):
  if signal.isdigit():
    return int(signal)

  if signal not in signals:
    print '***SIGNAL {} NOT IN LIST***'.format(signal)
    return

  print 'Resolving {} at level {}'.format(signal, level)

  command = commands[signals[signal]]
  print '  Command: ''{}'''.format(command)

  result = None
  if command[0] == 'RAW':
    if command[1].isalpha():
      result = resolve(command[1], signals, commands, level + 1)
    else:
      result = int(command[1])
  elif command[0] == 'AND':
    result = (resolve(command[1], signals, commands, level + 1) &
              resolve(command[2], signals, commands, level + 1))
  elif command[0] == 'OR':
    result = (resolve(command[1], signals, commands, level + 1) |
              resolve(command[2], signals, commands, level + 1))
  elif command[0] == 'NOT':
    result = ~resolve(command[1], signals, commands, level + 1)
  elif command[0] == 'LSHIFT':
    result = (resolve(command[1], signals, commands, level + 1) <<
              resolve(command[2], signals, commands, level + 1))
  elif command[0] == 'RSHIFT':
    result = (resolve(command[1], signals, commands, level + 1) >>
              resolve(command[2], signals, commands, level + 1))
  else:
    print '***UNKNOWN COMMAND***'
    result = None

  # Avoid recalculating by replacing function calls with their result
  # Fortunately, commands is passed by reference so we can modify it
  # Otherwise, we could just return the new command list
  commands[signals[signal]] = ('RAW', str(result))
  return result


signals = {}
commands = []

with open('input', 'r') as f:
  for line in f:
    if line.endswith('\n'):
      line = line[:-1]

    command = parse_line(line)

    commands.append(command[1:])
    command_index = len(commands) - 1

    signals[command[0]] = command_index

# We want the output on signal 'a'
print 'a is {}'.format(resolve('a', signals, commands, 0))
