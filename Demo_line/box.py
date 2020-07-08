# This class represents the product


from Demo_line.functions import *

class Box:

    def __init__(self, box_id, path):
        self.box_id = box_id
        self.path = path

    def run(self, section):
        process1(section)  # pop from portal
        check_and_pass(section)
        process2()  # delta
        process3()  # bufor s3
        process4()  # APAS
        process5()  # feader
        process6()  # emc

        if self.path == 0:  # without NEXO
            lift_enter_switch()
            process7()  # cartesian
            lift_exit_switch()
        else:
            lift_enter_switch()
            process8()  # bufor s8
            wait_nexo_button()
            process9()  # NEXO
            wait_nexo_button()
            process10()  # bufor s10
            lift_exit_switch()
        process11()  # bufor s11
        process12()  # grawer
        process13()  # BIG bufor s13
        process14()  # buffor s14
        process1(1)

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
