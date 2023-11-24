import unittest
from golife.patterns import Pattern, get_pattern


class PatternTestCase(unittest.TestCase):
    def test_load_single_pattern(self):
        """should load the blinker pattern"""

        actual_pattern = get_pattern("Blinker")
        expected_pattern = Pattern("Blinker", {(2, 1), (2, 2), (2, 3)})

        self.assertEqual(expected_pattern, actual_pattern)


if __name__ == "__main__":
    unittest.main()
