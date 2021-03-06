#!/usr/bin/env python

import json
import pprint

with open('input', 'r') as f:
  data = json.load(f)

def walk(node):
  if isinstance(node, dict):
    return sum([walk(item) for item in node.iteritems()])
  elif (isinstance(node, list) or
        isinstance(node, tuple)):
    return sum([walk(item) for item in node])
  else:
    # It's a leaf, do something
    if isinstance(node, int):
      return node
    else:
      return 0

print walk(data)
