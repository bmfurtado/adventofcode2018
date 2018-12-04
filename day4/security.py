#!/usr/bin/env python

import re

def guard_sleeps():
  """Iterator over the guard sleep blocks."""

  with open('input') as f:
    sorted_records = sorted((x.rstrip() for x in f.readlines()))

  guard = None

  for record in sorted_records:
    if record.endswith('begins shift'):
      guard = int(re.split(r'#(\d+)', record)[1])
    if record.endswith('falls asleep'):
      asleep = int(re.split(r'00:(\d+)', record)[1])
    if record.endswith('wakes up'):
      awake = int(re.split(r'00:(\d+)', record)[1])
      yield(guard, asleep, awake)

class SleepTracker(object):
  def __init__(self):
    self._sleeps = {}
    self._sleep_totals = {}
  
  def add_sleep(self, id, sleep, awake):
    guard_sleeps = self._sleeps.setdefault(id, [0] * 60)
    for min in range(sleep, awake):
      guard_sleeps[min] = guard_sleeps[min] + 1
      self._sleep_totals[id] = self._sleep_totals.get(id, 0) + 1
  
  def get_sleepiest_guard(self):
    return [x for x in self._sleep_totals.keys() if self._sleep_totals[x] == max(self._sleep_totals.values())][0]
  
  def get_sleepiest_minute(self, id):
    highest = max(self._sleeps.get(id))
    for i, x in enumerate(self._sleeps.get(id)):
      if x == highest:
        return i
  
  def get_total_sleep_for_minute(self, id, minute):
    return self._sleeps.get(id)[minute]
  
  def get_most_frequent_minute_of_all_ids(self):
    id_result = None
    minute_result = None
    max_amount = 0
    for id in self._sleeps.keys():
      minute = self.get_sleepiest_minute(id)
      amount = self.get_total_sleep_for_minute(id, minute)
      if amount > max_amount:
        id_result = id
        minute_result = minute
        max_amount = amount
    return id_result, minute_result


tracker = SleepTracker()
for record in guard_sleeps():
  tracker.add_sleep(*record)

guard_id = tracker.get_sleepiest_guard()
minute = tracker.get_sleepiest_minute(guard_id)

print guard_id * minute

id, minute = tracker.get_most_frequent_minute_of_all_ids()

print id * minute