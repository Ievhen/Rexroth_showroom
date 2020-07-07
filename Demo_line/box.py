# This class represents the product


class Box:

    def __init__(self, box_id, path):
        self.box_id = box_id
        self.path = path
        self.run()

    def run(self):
        self.process1(0)  # pop from portal
        self.process2()  # delta
        self.process3()  # bufor s3
        self.process4()  # APAS
        self.process5()  # feader
        self.process6()  # emc

        if self.path == 0:  # without NEXO
            self.lift_enter_switch()
            self.process7()  # cartesian
            self.lift_exit_switch()
        else:
            self.lift_enter_switch()
            self.process8()  # bufor s8
            self.wait_nexo_button()
            self.process9()  # NEXO
            self.wait_nexo_button()
            self.process10()  # bufor s10
            self.lift_exit_switch()
        self.process11()  # bufor s11
        self.process12()  # grawer
        self.process13()  # BIG bufor s13
        self.process14()  # buffor s14
        self.process1(1)

    def process1(self, path):
        if path == 0:
            pass
        elif path == 1:
            pass

    def process2(self):
        pass

    def process3(self):
        pass

    def process4(self):
        pass

    def process5(self):
        pass

    def process6(self):
        pass

    def process7(self):
        pass

    def process8(self):
        pass

    def process9(self):
        pass

    def process10(self):
        pass

    def process11(self):
        pass

    def process12(self):
        pass

    def process13(self):
        pass

    def process14(self):
        pass

    def lift_enter_switch(self):
        pass

    def lift_exit_switch(self):
        pass

    def wait_nexo_button(self):
        pass

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
