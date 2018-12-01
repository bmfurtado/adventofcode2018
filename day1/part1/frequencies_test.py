import unittest
import frequencies


class TestFrequencyCalculator(unittest.TestCase):
  def test_case1(self):
    input = [1, 1, 1]
    expected = 3
    self.assertEqual(expected, frequencies.calculate_frequency(input))

  def test_case2(self):
    input = [1, 1, -2]
    expected = 0
    self.assertEqual(expected, frequencies.calculate_frequency(input))

  def test_case3(self):
    input = [-1, -2, -3]
    expected = -6
    self.assertEqual(expected, frequencies.calculate_frequency(input))

if __name__ == '__main__':
    unittest.main()