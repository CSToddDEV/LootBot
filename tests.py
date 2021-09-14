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

if __name__ == '__main__':
    unittest.main()
