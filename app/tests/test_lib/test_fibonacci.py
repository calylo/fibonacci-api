import unittest
import app.lib.fibonacci.main as fibonacciLib


class TestFibonnaciLib(unittest.TestCase):

    def test_is_fibonacci_number(self):
        valid_fibonacci_numbers = [0, 1, 2, 3, 5, 8, 13, 21, 34]
        invalid_fibonacci_numbers = [4, 6, 7, 9, 511, 5555, 5858]
        for n in valid_fibonacci_numbers:
            is_valid = fibonacciLib.is_fibonacci_number(n)
            self.assertTrue(is_valid)
        for n in invalid_fibonacci_numbers:
            is_valid = fibonacciLib.is_fibonacci_number(n)
            self.assertFalse(is_valid)

    def test_get_nth_number(self):
        sequence_offset_150 = [
            9969216677189303386214405760200,
            16130531424904581415797907386349,
            26099748102093884802012313146549,
            42230279526998466217810220532898,
            68330027629092351019822533679447,
        ]

        for i in range(5):
            number = fibonacciLib.get_nth_number(150 + i)
            self.assertEqual(number, sequence_offset_150[i])


if __name__ == '__main__':
    unittest.main()
