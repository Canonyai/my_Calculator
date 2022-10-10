from calculator import *
# import calculator
import unittest


# python -m unittest test
class TestSum(unittest.TestCase):

    def test_addition(self):
        self.assertEquals(multiples("12435*34569"), "429865515", "should be 429865515")

    def test_subtraction(self):
        self.assertEquals(operation("34569-12435", 34569, 12435), 22134)
        self.assertEquals(operation("12435-34569", 12435, 34569), -22134)

    def test_multiply(self):
        self.assertEquals(operation("34569*12435", 12435, 34569) == 429865515)

    def test_negative_values(self):
        self.assertEquals(operation("12435-34569", 12435, 34569) == -22134)

    def test_str_build(self):
        self.assertEquals(num_append("12435-34569") == 12435)

    def test_operator(self):
        self.assertEquals(num_append("-") == True)

    def test_number(self):
        self.assertEquals(num_append("8") == True)

    def complete_test(self):
        self.assertEquals(multiples("12435+34569-12345*10+50"), "-76396")


if __name__ == '__main__':
    unittest.main()