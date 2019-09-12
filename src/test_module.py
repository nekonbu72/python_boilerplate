import unittest
from module import add, hello


class TestModule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3), 4)

    def test_hello(self):
        self.assertEqual(hello("World"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
