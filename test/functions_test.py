import unittest

from Demo_line.functions import *


class TestSection(unittest.TestCase):

    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.db = db_connect('localhost', 'root', 'shyrokoa', 'showroom_database')

    def test_check_status(self):
        self.assertEqual(check_status(self.db, 1)[0], 'WAIT')
        self.assertEqual(check_status(self.db, 1)[1], 'IDLE')
        self.assertEqual(check_status(self.db, 1)[2], 'STOP')
        self.assertEqual(check_status(self.db, 1)[3], 'ERROR')

    # Executing the tests in the above test case class
    if __name__ == "__main__":
        unittest.main()
