import unittest

from Phase1.main import functions


class TestAdd(unittest.TestCase):

    # Additions
    def test_add_value_less_than_max(self):
        self.assertEqual(functions.add(1, 3, 7), 4)
    def test_add_value_equal_max(self):
        self.assertEqual(functions.add(1, 6, 7), 7)
    def test_add_value_greater_than_max_no_overflow(self):
        self.assertEqual(functions.add(1, 10, 7), 3)
    def test_add_value_greater_than_max_overflow(self):
        self.assertEqual(functions.add(1, 13, 5), 2)

    # Subtractions
    def test_add_value_greater_than_min(self):
        self.assertEqual(functions.add(5, -3, 7), 2)
    def test_add_value_equal_to_min(self):
        self.assertEqual(functions.add(5, -5, 7), 0)
    def test_add_value_less_than_min_no_overflow(self):
        self.assertEqual(functions.add(5, -9, 7), 4)
    def test_add_value_less_than_min_overflow(self):
        self.assertEqual(functions.add(1, -13, 5), 0)

if __name__ == "__main__":
    unittest.main()
