# Startup script
from Demo_line.section import Section
from Demo_line.sql_tools import *


class Solver:

    def __init__(self):
        # TODO
        self.db = db_connect('localhost', 'root', 'shyrokoa', 'showroom_database')
        self.SECTION_NUM = 14
        self.section = []
        self.run()
        # close(self.db)

    def run(self):
        for i in range(self.SECTION_NUM):
            self.section.append(Section(f'S{i + 1}'))
        self.section[12].set_max_pallets_num(4)
        # print(self.section[12].get_max_pallets_num())

    def get_section_number(self):
        return self.SECTION_NUM

    def set_section_number(self, num):
        self.SECTION_NUM = num

    def get_section(self):
        return self.section


# Main
solver = Solver()
