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

    def test_getNthNumber(self):
        sequenceOffset150 = [
            9969216677189303386214405760200,
            16130531424904581415797907386349,
            26099748102093884802012313146549,
            42230279526998466217810220532898,
            68330027629092351019822533679447,
        ]

        for i in range(5):
            number = fibonacciLib.getNthNumber(150 + i)
            self.assertEqual(number, sequenceOffset150[i])



if __name__ == '__main__':
    unittest.main()
