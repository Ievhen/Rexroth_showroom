# This class describing the section of the transport conveyor
# Each section is defined by a stop gates
class Section:

    def __init__(self, num=1):
        self.MAX_PALLETS_NUM = num
        self.status = 'IDLE'
        self.counter = 0

    def counter_increase(self):
        self.counter += 1

    def counter_decrease(self):
        self.counter += 1

    def set_max_pallets_num(self, num):
        self.MAX_PALLETS_NUM = num

    def set_status(self, status):
        self.status = status

    def set_counter(self, counter):
        self.counter = counter

    def get_max_pallets_num(self):
        return self.MAX_PALLETS_NUM

    def get_status(self):
        return self.status

    def get_counter(self):
        return self.counter
