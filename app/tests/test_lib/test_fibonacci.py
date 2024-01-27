import unittest
import app.lib.fibonacci.main as fibonacciLib

class TestFibonnaciLib(unittest.TestCase):

    def test_isFibonacciNumber(self):
        validFibonacciNumbers = [0, 1, 2, 3, 5, 8, 13, 21, 34]
        for n in validFibonacciNumbers:
            isValid = fibonacciLib.isFibonacciNumber(n)
            self.assertTrue(isValid)


    def test_isNotFibonacciNumber(self):
        validFibonacciNumbers = [4, 6, 7, 9, 511, 5555, 5858]
        for n in validFibonacciNumbers:
            isValid = fibonacciLib.isFibonacciNumber(n)
            self.assertFalse(isValid)


if __name__ == '__main__':
    unittest.main()
