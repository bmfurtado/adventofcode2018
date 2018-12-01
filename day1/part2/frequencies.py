from itertools import cycle

def get_changes():
  """Read the frequency changes from input file.

  Returns:
      List of ints representing the frequency changes.
  """
  with open('input') as f:
      return [int(x) for x in f.readlines()]


def first_repeated_frequency(changes):
  seen = set()
  frequency = 0
  for change in cycle(changes):
    seen.add(frequency)
    frequency = frequency + change
    if frequency in seen:
      return frequency


if __name__ == "__main__":
  print first_repeated_frequency(get_changes())