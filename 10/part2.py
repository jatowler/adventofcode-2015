#!/usr/bin/env python


def look_and_say(string):
  chars = list(reversed(string))

  new_string = []
  while len(chars) > 0:
    char = chars.pop()
    count = 1
    while len(chars) > 0 and chars[-1] == char:
      chars.pop()
      count = count + 1

    new_string.append(str(count))
    new_string.append(char)

  return ''.join(new_string)


with open('input', 'r') as f:
  data = f.read()[:-1]

for i in xrange(50):
  data = look_and_say(data)
  print 'Iteration {}: {}'.format(i, len(data))

print 'The final string is {} chars long'.format(len(data))
