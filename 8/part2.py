#!/usr/bin/env python

def encode(string):
  print 'Encoding string {}'.format(string)

  # Replace backslashes
  string = string.replace('\\', '\\\\')
  print '  Replace \\: {}'.format(string)

  # Replace quotes
  string = string.replace('"', '\\"')
  print '  Replace ": {}'.format(string)

  # Add quotes
  string = '"{}"'.format(string)
  print '  Surround: {}'.format(string)

  return string

def decode(string):
  print 'Decoding string {}'.format(string)

  # Strip the start and end quotes
  string = string[1:-1]
  print '  Strip quotes: {}'.format(string)

  # Replace char codes
  def replace_char_code(matchobject):
    try:
      return chr(int(matchobject.group(1), 16))
    except ValueError:
      return '\\x' + matchobject.group(1)

  import re
  char_code = re.compile(r'\\x(..)')
  string = re.sub(char_code, replace_char_code, string)
  print '  Replace \\x: {}'.format(string)

  # Replace quotes
  string = string.replace('\\"', '"')
  print '  Replace \\": {}'.format(string)

  # Replace backslashes
  string = string.replace('\\\\', '\\')
  print '  Replace \\\\: {}'.format(string)

  return string


code_chars = 0
string_chars = 0

with open('input', 'r') as f:
  for line in f:
    if line.endswith('\n'):
      line = line[:-1]

    encoded_string = encode(line)

    code_chars = code_chars + len(line)
    string_chars = string_chars + len(encoded_string)

print 'Code chars: {}'.format(code_chars)
print 'String chars: {}'.format(string_chars)
print 'Difference: {}'.format(string_chars - code_chars)
