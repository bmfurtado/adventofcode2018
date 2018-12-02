def get_box_ids():
  """Read the box ids from input file.

  Returns:
      List of box ids.
  """
  with open('input') as f:
      return f.readlines()


def has_2_or_3_repetitions(box_id):
  counts = {}
  for char in box_id:
    counts[char] = counts.get(char, 0) + 1
  has_2 = False
  has_3 = False
  count_values = counts.values()
  if 2 in counts.values():
    has_2 = True
  if 3 in counts.values():
    has_3 = True
  return has_2, has_3

def calculate_checksum(box_ids):
  rep_2 = 0
  rep_3 = 0
  
  for box_id in box_ids:
    has_2, has_3 = has_2_or_3_repetitions(box_id)
    if has_2:
      rep_2 = rep_2 + 1
    if has_3:
      rep_3 = rep_3 + 1
  
  return rep_2 * rep_3

if __name__ == '__main__':
  print calculate_checksum(get_box_ids())