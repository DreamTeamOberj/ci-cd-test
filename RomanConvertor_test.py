import unittest
from RomanConvertor import RomanConvertor

class TestRomanConvertor(unittest.TestCase):

    def test_one_is_one(self):
        convertor = RomanConvertor()

        oneRoman = convertor.convert(1)

        self.assertEqual(oneRoman,"II")

    def test_two_is_two(self):
        convertor = RomanConvertor()

        twoRoman = convertor.convert(2)

        self.assertEqual(twoRoman, "II")

    def test_three_is_three(self):
        convertor = RomanConvertor()

        threeRoman = convertor.convert(3)

        self.assertEqual(threeRoman, "III")

    def test_four_is_four(self):
        convertor = RomanConvertor()

        fourRoman = convertor.convert(4)

        self.assertEqual(fourRoman,"IV")

    def test_five_is_five(self):
        convertor = RomanConvertor()

        fiveRoman = convertor.convert(5)

        self.assertEqual(fiveRoman, "V")

    def test_six_is_six(self):
        convertor = RomanConvertor()

        sixRoman = convertor.convert(6)

        self.assertEqual(sixRoman, "VI")

    def test_seven_is_seven(self):
        convertor = RomanConvertor()

        sevenRoman = convertor.convert(7)

        self.assertEqual(sevenRoman,"VII")

    def test_eight_is_eight(self):
        convertor = RomanConvertor()

        eightRoman = convertor.convert(8)

        self.assertEqual(eightRoman, "VIII")

    def test_nine_is_nine(self):
        convertor = RomanConvertor()

        nineRoman = convertor.convert(9)

        self.assertEqual(nineRoman, "IX")

    def test_ten_is_ten(self):
        convertor = RomanConvertor()

        tenRoman = convertor.convert(10)

        self.assertEqual(tenRoman,"X")

    def test_eleven_is_eleven(self):
        convertor = RomanConvertor()

        elevenRoman = convertor.convert(11)

        self.assertEqual(elevenRoman, "XI")

    def test_twelve_is_twelve(self):
        convertor = RomanConvertor()

        twelveRoman = convertor.convert(12)

        self.assertEqual(twelveRoman, "XII")

    def test_thirteen_is_thirteen(self):
        convertor = RomanConvertor()

        thirteenRoman = convertor.convert(13)

        self.assertEqual(thirteenRoman,"XIII")

    def test_fourteen_is_fourteen(self):
        convertor = RomanConvertor()

        fourteenRoman = convertor.convert(14)

        self.assertEqual(fourteenRoman, "XIV")

    def test_fifteen_is_fifteen(self):
        convertor = RomanConvertor()

        fifteenRoman = convertor.convert(15)

        self.assertEqual(fifteenRoman, "XV")

    def test_sixteen_is_sixteen(self):
        convertor = RomanConvertor()

        sixteenRoman = convertor.convert(16)

        self.assertEqual(sixteenRoman,"XVI")

    def test_seventeen_is_seventeen(self):
        convertor = RomanConvertor()

        seventeenRoman = convertor.convert(17)

        self.assertEqual(seventeenRoman, "XVII")

    def test_eighteen_is_eighteen(self):
        convertor = RomanConvertor()

        eighteenRoman = convertor.convert(18)

        self.assertEqual(eighteenRoman, "XVIII")

    def test_nineteen_is_nineteen(self):
        convertor = RomanConvertor()

        nineteenRoman = convertor.convert(19)

        self.assertEqual(nineteenRoman,"XIX")

    def test_twenty_is_twenty(self):
        convertor = RomanConvertor()

        twentyRoman = convertor.convert(20)

        self.assertEqual(twentyRoman, "XX")

    def test_twentyone_is_twentyone(self):
        convertor = RomanConvertor()

        twentyoneRoman = convertor.convert(21)

        self.assertEqual(twentyoneRoman, "XXI")

    def test_twentytwo_is_twentytwo(self):
        convertor = RomanConvertor()

        twentytwoRoman = convertor.convert(22)

        self.assertEqual(twentytwoRoman,"XXII")

    def test_twentythree_is_twentythree(self):
        convertor = RomanConvertor()

        twentythreeRoman = convertor.convert(23)

        self.assertEqual(twentythreeRoman, "XXIII")

    def test_twentyfour_is_twentyfour(self):
        convertor = RomanConvertor()

        twentyfourRoman = convertor.convert(24)

        self.assertEqual(twentyfourRoman, "XXIV")

    def test_twentyfive_is_twentyfive(self):
        convertor = RomanConvertor()

        twentyfiveRoman = convertor.convert(25)

        self.assertEqual(twentyfiveRoman, "XXV")

    def test_twentysix_is_twentysix(self):
        convertor = RomanConvertor()

        twentysixRoman = convertor.convert(26)

        self.assertEqual(twentysixRoman,"XXVI")

    def test_twentyseven_is_twentyseven(self):
        convertor = RomanConvertor()

        twentysevenRoman = convertor.convert(27)

        self.assertEqual(twentysevenRoman, "XXVII")

    def test_twentyeight_is_twentyeight(self):
        convertor = RomanConvertor()

        twentyeightRoman = convertor.convert(28)

        self.assertEqual(twentyeightRoman, "XXVIII")

    def test_twentynine_is_twentynine(self):
        convertor = RomanConvertor()

        twentynineRoman = convertor.convert(29)

        self.assertEqual(twentynineRoman,"XXIX")

    def test_thirteen_is_thireteen(self):
        convertor = RomanConvertor()

        thirteenRoman = convertor.convert(30)

        self.assertEqual(thirteenRoman, "XXX")

if __name__ == '__main__':
    unittest.main()
