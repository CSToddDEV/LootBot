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

if __name__ == '__main__':
    unittest.main()
