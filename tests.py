import unittest
import lb


class MyTestCase(unittest.TestCase):
    def test_lb_1(self):
        """
        Test lb.py 1 -
        This test asserts that the .env variable DISCORD_TOKEN is not returning default (meaning the token has not been
        retrieved)
        """
        test_bot = lb.LootBot()

        self.assertNotEqual(test_bot.get_disc_token(), None)


if __name__ == '__main__':
    unittest.main()
