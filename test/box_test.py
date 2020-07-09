import unittest

from Demo_line.box import Box


class TestBox(unittest.TestCase):

    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.box = Box(123, 1)

    def test_set_box_id(self):
        self.box.set_box_id(3)
        self.assertEqual(self.box.box_id, 3)

    # Executing the tests in the above test case class
    if __name__ == "__main__":
        unittest.main()
