# A set of functions
# from Demo_line.sql_tool


def check_status(section_id):
    pass


# transfer the signal to Master or/and DB
# WE are using TIMER and COIL to serve the signal
def pass_unit(stop_gate):
    pass


def write_rfid():
    pass


def read_rfid():
    pass


# transfer the signal to Master or/and DB
# WE are using local state machine on Slave
# Program 0 - pop the box, 1 - push the box.
def run_portal(prog):
    pass


def run_delta(prog):
    pass


def run_apas(prog):
    pass


def run_feeder(prog):
    pass


def run_emc(prog):
    pass


def run_cartesian(prog):
    pass


def run_nexo(prog):
    pass


def run_engraver(prog):
    pass


# change the status from 'BUSY' -> 'DONE'
def empty_prog():
    pass


def be_ready_to_switch(path, lift_id):
    if path:
        if lift_id == 'L3':
            pass  # go to cartesian
        elif lift_id == 'L4':
            pass  # go from cartesian
    else:
        if lift_id == 'L3':
            pass  # go to buffer before the Nexo
        elif lift_id == 'L4':
            pass  # go from buffer after the Nexo


# Processes logic


# PORTAL
def process1(section, prog=0):
    if section[0].get_status() == 'BUSY':
        write_rfid(1)
        run_portal(prog)


def check_and_pass(section, start, end):
    if section[start].get_status() == 'DONE' and section[end].get_status() == 'IDLE':
        section[end].set_status('WAIT')
        pass_unit(section[start].get_stop_gate())


# DELTA
def process2(section, prog=0):
    if section[1].get_status() == 'BUSY':
        read_rfid(2)
        run_delta(prog)


# BUFFER S3 before the APAS
def process3(section):
    if section[2].get_status() == 'BUSY':
        empty_prog()


# APAS
def process4(section, prog=0):
    if section[3].get_status() == 'BUSY':
        read_rfid(3)
        run_apas(prog)


# FEEDER
def process5(section, prog=0):
    if section[4].get_status() == 'BUSY':
        read_rfid(4)
        run_feeder(prog)


# EMC PRESS
def process6(section, prog=0):
    if section[5].get_status() == 'BUSY':
        read_rfid(5)
        run_emc(prog)


#
def lift_enter_switch(section, path):
    if path:
        section[6].set_satus('WAIT')
        be_ready_to_switch(True, 'L3')
    else:
        section[7].set_status('WAIT')
        be_ready_to_switch(False, 'L3')
    pass_unit('S6')


def lift_exit_switch(section, path):
    if path:
        section[10].set_satus('WAIT')
        be_ready_to_switch(True, 'L4')
        pass_unit('S7')
    else:
        section[11].set_status('WAIT')
        be_ready_to_switch(False, 'L4')
        pass_unit('S10')


# CARTESIAN
def process7(section, prog=0):
    if section[6].get_status() == 'BUSY':
        read_rfid(6)
        run_cartesian(prog)


# BUFFER S8 before the NEXO
def process8(section):
    if section[7].get_status() == 'BUSY':
        empty_prog()


def wait_nexo_button():
    pass
    # while get_nexo_button() == False:
    #    time.sleep(0.1) # 100ms


# NEXO
def process9(section, prog=0):
    if section[8].get_status() == 'BUSY':
        read_rfid(7)
        run_nexo(prog)


# BUFFER S10 after the NEXO
def process10(section):
    if section[9].get_status() == 'BUSY':
        empty_prog()


# BUFFER S11 after the NEXO
def process11(section):
    if section[10].get_status() == 'BUSY':
        empty_prog()


# ENGRAVER
def process12(section, prog=0):
    if section[11].get_status() == 'BUSY':
        read_rfid(8)
        run_engraver(prog)


# BIG BUFFER S13
def process13(section):
    if section[12].get_counter() > 0 and section[13].get_status() == 'IDLE':
        section[13].set_satus('WAIT')
        section[12].counter_decrease()
        pass_unit('S13')


# BUFFER S14 before the PORTAL
def process14(section):
    if section[13].get_status() == 'BUSY':
        empty_prog()
