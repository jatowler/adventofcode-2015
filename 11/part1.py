#!/usr/bin/env python

import re
pair = re.compile(r'(.)\1')

def contains_two_pairs(string):
  return len(re.findall(pair, string)) >= 2

def contains_iol(string):
  banned_letters = ['i','o','l']
  for letter in banned_letters:
    if letter in string:
      return True

  return False

def contains_abc_string(string):
  ords = [ord(x) for x in string]
  for i in xrange(len(ords) - 2):
    if ords[i + 1] - ords[i] != 1:
      continue
    if ords[i + 2] - ords[i + 1] != 1:
      continue
    return True

  return False

def valid_password(string):
  return (~contains_iol(string) and
          contains_two_pairs(string) and
          contains_abc_string(string))

def increment_string(string):
  s = list(reversed(string))

  for i in xrange(len(s)):
    if s[i] == 'z':
      s[i] = 'a'
      continue

    s[i] = chr(ord(s[i]) + 1)

    # If we're banned, go ahead and skip it
    if s[i] in ['i','o','l']:
      s[i] = chr(ord(s[i]) + 1)

    # We are done incrementing now
    break

  return ''.join(reversed(s))


with open('input', 'r') as f:
  password = f.read()
  if password.endswith('\n'):
    password = password[:-1]

count = 0
while not valid_password(password):
  password = increment_string(password)
  count = count + 1

  if count % 10000 == 0:
    print password, count

print password
