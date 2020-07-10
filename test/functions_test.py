import unittest

from Demo_line.functions import *


class TestSection(unittest.TestCase):

    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.db = db_connect('localhost', 'root', 'shyrokoa', 'showroom_database')

    def test_check_status(self):
        self.assertEqual(check_status(self.db)[0], 'WAIT')
        self.assertEqual(check_status(self.db)[1], 'IDLE')
        self.assertEqual(check_status(self.db)[2], 'STOP')
        self.assertEqual(check_status(self.db)[3], 'ERROR')

    def test_pass_unit(self):
        pass_unit(self.db, 'SA9')
        req = 'SELECT * FROM showroom_database.ts_request WHERE pl_id=1'
        self.assertEqual(execute_request(self.db, req)[0][9], 1)

    # Executing the tests in the above test case class
    if __name__ == "__main__":
        unittest.main()
