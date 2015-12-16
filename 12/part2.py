#!/usr/bin/env python

import json
import pprint

with open('input', 'r') as f:
  data = json.load(f)

def walk(node):
  if isinstance(node, dict):
    if u'red' in node.values():
      return 0

    return sum([walk(item) for item in node.iteritems()])
  elif (isinstance(node, list) or
        isinstance(node, tuple)):
    return sum([walk(item) for item in node])
  else:
    if isinstance(node, int):
      return node
    else:
      return 0

print walk(data)
