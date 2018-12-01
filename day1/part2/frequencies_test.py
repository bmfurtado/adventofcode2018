import unittest
import frequencies


class TestRepeatedFrequencyFinder(unittest.TestCase):
  def test_case1(self):
    input = [+1, -1]
    expected = 0
    self.assertEqual(expected, frequencies.first_repeated_frequency(input))

  def test_case2(self):
    input = [+3, +3, +4, -2, -4]
    expected = 10
    self.assertEqual(expected, frequencies.first_repeated_frequency(input))

  def test_case3(self):
    input = [-6, +3, +8, +5, -6]
    expected = 5
    self.assertEqual(expected, frequencies.first_repeated_frequency(input))

  def test_case4(self):
    input = [+7, +7, -2, -7, -4]
    expected = 14
    self.assertEqual(expected, frequencies.first_repeated_frequency(input))

if __name__ == '__main__':
    unittest.main()