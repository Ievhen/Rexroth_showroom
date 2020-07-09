import unittest

from Demo_line.box import Box


class TestBox(unittest.TestCase):

    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.box = Box(123, 1)

    def test_set_box_id(self):
        self.box.set_box_id(3)
        self.assertEqual(self.box.box_id, 3)

    def test_set_path(self):
        self.box.set_path(0)
        self.assertEqual(self.box.path, 0)

    def test_get_box_id(self):
        self.box.set_box_id(6)
        self.assertEqual(self.box.get_box_id(), 6)

    def test_get_path(self):
        self.box.set_path(7)
        self.assertEqual(self.box.get_path(), 7)

    # Executing the tests in the above test case class
    if __name__ == "__main__":
        unittest.main()
