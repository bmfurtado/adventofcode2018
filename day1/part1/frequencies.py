def get_changes():
  """Read the frequency changes from input file.

  Returns:
      List of ints representing the frequency changes.
  """
  with open('input') as f:
      return [int(x) for x in f.readlines()]


def calculate_frequency(changes):
  frequency = 0
  for line in changes:
    frequency = frequency + line
  return frequency


if __name__ == "__main__":
  print calculate_frequency(get_changes())