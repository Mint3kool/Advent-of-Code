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

    #repeatedNumber
    def test_isRepeatedNumber_20(self):
            self.assertFalse(functions.isRepeatedNumber(20))
    def test_isRepeatedNumber_101(self):
        self.assertFalse(functions.isRepeatedNumber(101))
    def test_isRepeatedNumber_11111(self):
        self.assertTrue(functions.isRepeatedNumber(11111))
    def test_isRepeatedNumber_1212121212(self):
        self.assertTrue(functions.isRepeatedNumber(1212121212))
    def test_isRepeatedNumber_824824824(self):
            self.assertTrue(functions.isRepeatedNumber(824824824))
    def test_isRepeatedNumber_1010101010(self):
            self.assertTrue(functions.isRepeatedNumber(1010101010))
    def test_isRepeatedNumber_1000010000100001000010000(self):
            self.assertTrue(functions.isRepeatedNumber(1000010000100001000010000))

    #verifyRepeatedNumber
    def test_verifyRepeatedNumber_11111(self):
         self.assertTrue(functions.verifyRepeatedNumber(1111,1,0))
    def test_verifyRepeatedNumber_121111(self):
        self.assertFalse(functions.verifyRepeatedNumber(12111,1,0))
    def test_verifyRepeatedNumber_10000001(self):
        self.assertFalse(functions.verifyRepeatedNumber(1000000,1,0))

    # maxVoltage
    def test_maxVoltage(self):
        self.assertEqual(functions.maxVoltage([99,11,33]), 143)
    def test_maxVoltage_larger_batts(self):
        self.assertEqual(functions.maxVoltage([987654321111111,811111111111119,234234234234278,818181911112111]), 357)

    # getBatteryVoltage
    def test_getBatteryVoltage_99(self):
        self.assertEqual(functions.getBatteryVoltage(99), 99)
    def test_getBatteryVoltage_119911(self):
        self.assertEqual(functions.getBatteryVoltage(119911), 99)
    def test_getBatteryVoltage_123456(self):
        self.assertEqual(functions.getBatteryVoltage(123456), 56)
    def test_getBatteryVoltage_654321(self):
        self.assertEqual(functions.getBatteryVoltage(654321), 65)

    def test_getBatteryVoltage_654321_len4(self):
        self.assertEqual(functions.getBatteryVoltage(654321, 4), 6543)
    def test_getBatteryVoltage_123456789_len4(self):
        self.assertEqual(functions.getBatteryVoltage(123456789, 7), 3456789)
    def test_getBatteryVoltage_1111111111111111_len4(self):
        self.assertEqual(functions.getBatteryVoltage(1111111111111111, 4), 1111)
    def test_getBatteryVoltage_987654321111111_len12(self):
        self.assertEqual(functions.getBatteryVoltage(987654321111111, 12), 987654321111)
    def test_getBatteryVoltage_234234234234278_len12(self):
        self.assertEqual(functions.getBatteryVoltage(234234234234278, 12), 434234234278)

    def test_countAccessibleRolls_noCenterRolls(self):
        self.assertEqual(functions.countAccessibleRolls([".@.","...","@@@"]), 0)
    def test_countAccessibleRolls_allCenterRolls(self):
        self.assertEqual(functions.countAccessibleRolls([".@.","@@@","..@"]), 2)
if __name__ == "__main__":
    unittest.main()
3