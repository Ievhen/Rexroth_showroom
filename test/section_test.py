import unittest

from Demo_line.section import Section


class TestSection(unittest.TestCase):

    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.section = Section('S1', 2)

    def test_counter_increase(self):
        self.section.counter_increase()
        self.assertEqual(self.section.counter, 1)

    def test_counter_decrease(self):
        self.section.counter_increase()
        self.section.counter_decrease()
        self.assertEqual(self.section.counter, 0)

    def test_set_max_pallets_num(self):
        self.section.set_max_pallets_num(7)
        self.assertEqual(self.section.max_pallets_num, 7)

    def test_set_status(self):
        self.section.set_status('OK')
        self.assertEqual(self.section.status, 'OK')

    def test_set_counter(self):
        self.section.set_counter(7)
        self.assertEqual(self.section.counter, 7)

    def test_get_max_pallets_num(self):
        self.assertEqual(self.section.get_max_pallets_num(), 2)

    def test_get_status(self):
        self.assertEqual(self.section.get_status(), 'IDLE')

    def test_get_counter(self):
        self.section.set_counter(7)
        self.assertEqual(self.section.get_counter(), 7)

    def test_get_stop_gate(self):
        self.assertEqual(self.section.get_stop_gate(), 'S1')

    # Executing the tests in the above test case class
    if __name__ == "__main__":
        unittest.main()
