import unittest
import lb
import dimensions


class MyTestCase(unittest.TestCase):
    def test_lb_1(self):
        """
        Test lb.py 1 -
        This test asserts that the .env variable DISCORD_TOKEN is not returning default (meaning the token has not been
        retrieved)
        """
        test_bot = lb.LootBot()

        self.assertNotEqual(test_bot.get_disc_token(), None)

    # Tests for dimensions.py
    def test_dimensions_1(self):
        """
        Test dimensions.py 1 -
        This test asserts that the function split_coord is returning the right data
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.split_coord('B22'), (['B'], '22'))

    def test_dimensions_2(self):
        """
        Test dimensions.py 2 -
        This test asserts that the function split_coord is returning the right data
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.split_coord('ABC2255'), (['A', 'B', 'C'], '2255'))

    def test_dimensions_3(self):
        """
        Test dimensions.py 3 -
        This test asserts that the function increase_row_number is returning the right number
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_row_number('5', 10), '15')

    def test_dimensions_4(self):
        """
        Test dimensions.py 4 -
        This test asserts that the function increase_row_number is returning the right number
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_row_number('100', 0), '100')

    def test_dimensions_5(self):
        """
        Test dimensions.py 5 -
        This test asserts that the function increase_row_number is returning the right number
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_row_number('69', -4), '65')

    def test_dimensions_6(self):
        """
        Test dimensions.py 6 -
        This test asserts that the function increase_column_letter is returning the right number
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_column_letter(['A']), ['B'])

    def test_dimensions_7(self):
        """
        Test dimensions.py 7 -
        This test asserts that the function increase_column_letter is returning the right number
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_column_letter(['Z']), ['A', 'A'])

    def test_dimensions_8(self):
        """
        Test dimensions.py 8 -
        This test asserts that the function increase_column_letter is returning the right number
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_column_letter(['C', 'Z', 'Z']), ['D', 'A', 'A'])

    def test_dimensions_9(self):
        """
        Test dimensions.py 9 -
        This test asserts that the function increase_column_letter is returning the right number
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_column_letter(['C', 'Z', 'H']), ['C', 'Z', 'I'])

    def test_dimensions_10(self):
        """
        Test dimensions.py 10 -
        This test asserts that the function increase_column_letter_times is returning the right number
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_column_letter_times(['C', 'Z', 'H'], 2), ['C', 'Z', 'J'])

    def test_dimensions_11(self):
        """
        Test dimensions.py 11 -
        This test asserts that the function combine_coord is returning the right coordinate
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.combine_coord(['C', 'Z', 'H'], '55'), 'CZH55')

    def test_dimensions_12(self):
        """
        Test dimensions.py 12 -
        This test asserts that the function combine_coord is returning the right coordinate
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.combine_coord(['A'], '5'), 'A5')

    def test_dimensions_13(self):
        """
        Test dimensions.py 13 -
        This test asserts that the function increase_coord is returning the right coordinate
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_coord('A5', 1, 0), 'B5')

    def test_dimensions_14(self):
        """
        Test dimensions.py 14 -
        This test asserts that the function increase_coord is returning the right coordinate
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_coord('A5', 0, 1), 'A6')

    def test_dimensions_15(self):
        """
        Test dimensions.py 15 -
        This test asserts that the function increase_coord is returning the right coordinate
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_coord('A5', 1, 1), 'B6')

    def test_dimensions_16(self):
        """
        Test dimensions.py 16 -
        This test asserts that the function increase_coord is returning the right coordinate
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_coord('A5', 0, 0), 'A5')

    def test_dimensions_17(self):
        """
        Test dimensions.py 17 -
        This test asserts that the function increase_coord is returning the right coordinate
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.increase_coord('A5', 100, 100), 'CW105')

    def test_dimensions_18(self):
        """
        Test dimensions.py 18 -
        This test asserts that the function convert_coord_to_int is returning the right integers
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.convert_coord_to_int('A5'), (0, 5))

    def test_dimensions_19(self):
        """
        Test dimensions.py 19 -
        This test asserts that the function convert_coord_to_int is returning the right integers
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.convert_coord_to_int('BB10'), (53, 10))

    def test_dimensions_20(self):
        """
        Test dimensions.py 20 -
        This test asserts that the function convert_coord_to_int is returning the right integers
        """
        test_dimensions = dimensions.Dimensions(None)

        self.assertEqual(test_dimensions.convert_coord_to_int('ABC69'), (730, 69))

if __name__ == '__main__':
    unittest.main()
