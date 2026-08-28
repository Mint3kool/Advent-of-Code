import unittest

from Advent.main import functions


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
    def test_countclick_loop_testing_1(self):
        self.assertEqual(functions.countClickZero([-4,-4,4,-4,4,4], 0, 3), 6)
    def test_countclick_loop_testing_2(self):
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

    #doubleNumber
    def test_isDoubleNumber_11(self):
        self.assertEqual(functions.isDoubleNumber(11), True)
    def test_isDoubleNumber_12(self):
        self.assertEqual(functions.isDoubleNumber(12), False)
    def test_isDoubleNumber_100999(self):
            self.assertEqual(functions.isDoubleNumber(100999), False)
    def test_isDoubleNumber_100100(self):
        self.assertEqual(functions.isDoubleNumber(100100), True)
    def test_isDoubleNumber_100102100102(self):
            self.assertEqual(functions.isDoubleNumber(100102100102), True)
    def test_isDoubleNumber_100101(self):
        self.assertEqual(functions.isDoubleNumber(100101), False)
    def test_isDoubleNumber_11011(self):
            self.assertEqual(functions.isDoubleNumber(11011), False)
    def test_isDoubleNumber_set(self):
        list = [11,22,99,1010,1188511885,222222,446446,38593859]
        for value in list:
            self.assertEqual(functions.isDoubleNumber(value), True)
if __name__ == "__main__":
    unittest.main()
