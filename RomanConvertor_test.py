import unittest

from RomanConvertor import RomanConvertor
class TestRomanConvertor(unittest.TestCase):

    def test_one_is_one(self):
        convertor = RomanConvertor()

        oneRoman = convertor.convert(1)

        self.assertEqual(oneRoman,"I")

    def test_two_is_two(self):
        convertor = RomanConvertor()

        twoRoman = convertor.convert(2)

        self.assertEqual(twoRoman, "II")

    def test_three_is_three(self):
        convertor = RomanConvertor()

        threeRoman = convertor.convert(3)

        self.assertEqual(threeRoman, "III")


if __name__ == '__main__':
    unittest.main()
