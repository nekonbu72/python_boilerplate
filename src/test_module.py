import unittest

from module import add, even, hello


class TestModule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3), 4)

    def test_even(self):
        self.assertEqual(even(range(5)), [0, 2, 4])

    def test_hello(self):
        self.assertEqual(hello("World"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
