import unittest

from Demo_line.solver import Solver


class TestSolver(unittest.TestCase):

    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.solver = Solver()

    def test_get_section_number(self):
        self.assertEqual(self.solver.get_section_number(), 14)

    def test_set_section_number(self):
        self.solver.set_section_number(7)
        self.assertEqual(self.solver.SECTION_NUM, 7)

    # Executing the tests in the above test case class
    if __name__ == "__main__":
        unittest.main()
