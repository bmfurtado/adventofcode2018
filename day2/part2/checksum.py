def get_box_ids():
  """Read the box ids from input file.

  Returns:
      List of box ids.
  """
  with open('input') as f:
      return [x.rstrip() for x in f.readlines()]


def get_distance(a, b):
  diffs = 0
  for a, b in zip(a, b):
    if a != b:
      diffs = diffs + 1
  return diffs

def find_similar(box_ids):
  for i, box_id_1 in enumerate(box_ids):
    for box_id_2 in box_ids[i:]:
      if get_distance(box_id_1, box_id_2) == 1:
        return box_id_1, box_id_2

def get_common(a, b):
  chars = []
  for a, b, in zip(a, b):
    if a == b:
      chars.append(a)
  return ''.join(chars)

if __name__ == '__main__':
  a, b = find_similar(get_box_ids())
  print get_common(a, b)