import unittest

from fizz_buzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizz_buzz = FizzBuzz()

    def test_number_1_should_be_1(self):
        expected = 1
        result = self.fizz_buzz.get(1)
        self.assertEqual(expected, result)

    def test_number_2_should_be_2(self):
        expected = 2
        result = self.fizz_buzz.get(2)
        self.assertEqual(expected,result)

    def test_number_3_should_be_fizz(self):
        expected = 'Fizz'
        result = self.fizz_buzz.get(3)
        self.assertEqual(expected, result)

    def test_number_5_should_be_buzz(self):
        expected = 'Buzz'
        result = self.fizz_buzz.get(5)
        self.assertEqual(expected, result)

    def test_number_6_should_be_fizz(self):
        expected = 'Fizz'
        result = self.fizz_buzz.get(6)
        self.assertEqual(expected, result)

    def test_number_10_should_be_buzz(self):
        expected = "Buzz"
        result = self.fizz_buzz.get(10)
        self.assertEqual(expected, result)

    def test_number_15_should_be_fizzbuzz(self):
        expected = "FizzBuzz"
        result = self.fizz_buzz.get(15)
        self.assertEqual(expected, result)

    def test_number_13_should_be_fizz(self):
        expected = "Fizz"
        result = self.fizz_buzz.get(13)
        self.assertEqual(expected, result)

    def test_number_23_should_be_fizz(self):
        expected = "Fizz"
        result = self.fizz_buzz.get(23)
        self.assertEqual(expected, result)

    def test_number_56_should_be_buzz(self):
        expected = "Buzz"
        result = self.fizz_buzz.get(56)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
