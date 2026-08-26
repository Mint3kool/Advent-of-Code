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

    # CountClickZero
    def test_countclick_no_increment(self):
        self.assertEqual(functions.countClickZero([2], 3, 10), 0)
    def test_countclick_increment_once_greater_than_zero(self):
        self.assertEqual(functions.countClickZero([2], 13, 10), 1)
    def test_countclick_increment_once_less_than_zero(self):
        self.assertEqual(functions.countClickZero([2], -3, 10), 1)
    def test_countclick_increment_eq_to_zero(self):
        self.assertEqual(functions.countClickZero([2], -2, 10), 1)
    def test_countclick_increment_multiple_greater_than_max(self):
        self.assertEqual(functions.countClickZero([10], 2, 4), 2)
    def test_countclick_increment_start_from_zero(self):
        self.assertEqual(functions.countClickZero([95], 0, 99), 0)
    def test_countclick_loop_testing_1(self):
        self.assertEqual(functions.countClickZero([-4,-4,4,-4,4,4], 0, 3), 6)
    def test_countclick_loop_testing_1(self):
        self.assertEqual(functions.countClickZero([4,4,4,4,4,4], 0, 3), 6)
    def test_countclick_multiple_ops(self):
        self.assertEqual(functions.countClickZero([-68,-30,48,-5,60,-55,-1,-99,14,-82], 50, 99), 6)

    #clickZero
    def test_clickZero_1(self):
        self.assertEqual(functions.clickZero(1, -1, 3), 1)
    def test_clickZero_2(self):
        self.assertEqual(functions.clickZero(1, 1, 3), 0)
    def test_clickZero_3(self):
        self.assertEqual(functions.clickZero(1, 3, 3), 1)
    def test_clickZero_4(self):
        self.assertEqual(functions.clickZero(1, 5, 3), 1)
    def test_clickZero_5(self):
        self.assertEqual(functions.clickZero(1, 11, 3), 3)
if __name__ == "__main__":
    unittest.main()
