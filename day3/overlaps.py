#!/usr/bin/env python

import re
import itertools

def claims():
  """Iterator over the claims."""
  with open('input') as f:
    for line in f.readlines():
      l = line.rstrip()
      yield tuple([int(x) for x in re.split(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', l)[1:-1]])


class Fabric(object):
  def __init__(self):
    self._fabric = {}

  def get_claims(self, x, y):
    return self._fabric.setdefault((x, y), [])
  
  def add_claim(self, id, x, y):
    self.get_claims(x, y).append(id)
  
  def get_overlapping_sqin(self):
    return [len(x) for x in self._fabric.values() if len(x) > 1]

  def get_safe_claims(self):
    single_claims = set()
    multi_claims = set()

    for claims in self._fabric.values():
      if len(claims) == 1:
        single_claims.update(claims)
      else:
        multi_claims.update(claims)
    
    return single_claims - multi_claims

fabric = Fabric()
for id, offset_width, offset_height, width, height in claims():
  for x in range(offset_width + 1, offset_width + width + 1):
    for y in range(offset_height + 1, offset_height + height + 1):
      fabric.add_claim(id, x, y)
print len(fabric.get_overlapping_sqin())
print fabric.get_safe_claims()