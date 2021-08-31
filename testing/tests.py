import unittest
from null import lb


class MyTestCase(unittest.TestCase):
    def test_global_1(self):
        """
        Test global 1 -
        Asserts that True equals True
        """
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
