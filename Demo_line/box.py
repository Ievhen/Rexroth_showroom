# This class represents the product


from Demo_line.functions import *


class Box:

    def __init__(self, box_id, path):
        self.box_id = box_id
        self.path = path

    def run(self, section):
        process1(section, 0)  # get the product out of supermarket
        check_and_pass(section, 0, 1)
        process2(section)  # delta
        check_and_pass(section, 1, 2)
        process3(section)  # buffer s3
        check_and_pass(section, 2, 3)
        process4(section)  # apas
        check_and_pass(section, 3, 4)
        process5(section)  # feeder
        check_and_pass(section, 4, 5)
        process6(section)  # emc press

        if self.path == 0:  # path to automatic workstation
            lift_enter_switch(section, self.path)
            process7(section)  # cartesian
            lift_exit_switch(section, self.path)
        else:  # path to manual workstation
            lift_enter_switch(section, self.path)
            process8(section)  # buffer s8
            check_and_pass(section, 3, 4)
            wait_nexo_button()
            check_and_pass(section, 7, 8)
            process9(section)  # nexo
            wait_nexo_button()
            check_and_pass(section, 8, 9)
            process10(section)  # buffer s10
            lift_exit_switch(section, self.path)

        process11(section)  # buffer s11
        check_and_pass(section, 10, 11)
        process12(section)  # engraver
        process13(section)  # big buffer s13
        process14(section)  # buffer s14
        check_and_pass(section, 13, 0)
        process1(section, 1)  # put the product in the supermarket

    # setters
    def set_box_id(self, id):
        self.box_id = id

    def set_path(self, path):
        self.path = path

    # getters
    def get_box_id(self):
        return self.box_id

    def get_path(self):
        return self.path
