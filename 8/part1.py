#!/usr/bin/env python


def count_code_chars(string):
  return len(string)


def count_string_chars(string):
  length = len(string)
  print 'Processing string {} ({})'.format(string, length)

  # Strip the start and end quotes
  string = string[1:-1]
  length = len(string)
  print '  Strip quotes: {} ({})'.format(string, length)

  # Replace char codes
  def replace_char_code(matchobject):
    try:
      return chr(int(matchobject.group(1), 16))
    except ValueError:
      return '\\x' + matchobject.group(1)

  import re
  char_code = re.compile(r'\\x(..)')
  string = re.sub(char_code, replace_char_code, string)
  length = len(string)
  print '  Replace \\x: {} ({})'.format(string, length)

  # Replace quotes
  string = string.replace('\\"', '"')
  length = len(string)
  print '  Replace \\": {} ({})'.format(string, length)

  # Replace backslashes
  string = string.replace('\\\\', '\\')
  length = len(string)
  print '  Replace \\\\: {} ({})'.format(string, length)

  return length


code_chars = 0
string_chars = 0

with open('input', 'r') as f:
  for line in f:
    if line.endswith('\n'):
      line = line[:-1]

    cur_code = count_code_chars(line)
    cur_string = count_string_chars(line)

    code_chars = code_chars + cur_code
    string_chars = string_chars + cur_string

print 'Code chars: {}'.format(code_chars)
print 'String chars: {}'.format(string_chars)
print 'Difference: {}'.format(code_chars - string_chars)
