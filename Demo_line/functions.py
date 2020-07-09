# A set of functions
from Demo_line.sql_tools import *

# SQL requests


def check_status(section_id):
    pass


# transfer the signal to Master or/and DB
# we are using TIMER and COIL to serve the signal
def pass_unit(stop_gate):
    pass


def write_rfid():
    pass


def read_rfid():
    pass


# transfer the signal to Master or/and DB
# we are using local state machine on Slave
# program 0 - pop the box, 1 - push the box.
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


def get_nexo_button():
    pass

# Processes logic


# PORTAL
def process1(section, prog=0):
    while True:
        if section[0].get_status() == 'BUSY':
            break
        else:
            pass  # time.sleep(0.1) # 100ms
    write_rfid(1)
    run_portal(prog)


# Release pallet when conditions met
def check_and_pass(section, start, end):
    while True:
        if section[start].get_status() == 'DONE' and section[end].get_status() == 'IDLE':
            break
        else:
            pass
    section[end].set_status('WAIT')
    pass_unit(section[start].get_stop_gate())


# DELTA
def process2(section, prog=0):
    while True:
        if section[1].get_status() == 'BUSY':
            break
        else:
            pass
    read_rfid(2)
    run_delta(prog)


# BUFFER S3 before the APAS
def process3(section):
    while True:
        if section[2].get_status() == 'BUSY':
            break
        else:
            pass
    empty_prog()


# APAS
def process4(section, prog=0):
    while True:
        if section[3].get_status() == 'BUSY':
            break
        else:
            pass
    read_rfid(3)
    run_apas(prog)


# FEEDER
def process5(section, prog=0):
    while True:
        if section[4].get_status() == 'BUSY':
            break
        else:
            pass
    read_rfid(4)
    run_feeder(prog)


# EMC PRESS
def process6(section, prog=0):
    while True:
        if section[5].get_status() == 'BUSY':
            break
        else:
            pass
    read_rfid(5)
    run_emc(prog)


# RAILROAD SWITCH for lift L3
def lift_enter_switch(section, path):
    if path:
        section[6].set_satus('WAIT')
        be_ready_to_switch(True, 'L3')
    else:
        section[7].set_status('WAIT')
        be_ready_to_switch(False, 'L3')
    pass_unit('S6')


# RAILROAD SWITCH for lift L4
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
    while True:
        if section[6].get_status() == 'BUSY':
            break
        else:
            pass
    read_rfid(6)
    run_cartesian(prog)


# BUFFER S8 before the NEXO
def process8(section):
    while True:
        if section[7].get_status() == 'BUSY':
            break
        else:
            pass
    empty_prog()


# Check two-handed push-button system
def wait_nexo_button():
    while True:
        if get_nexo_button() == True:
            break
        else:
            pass


# NEXO
def process9(section, prog=0):
    while True:
        if section[8].get_status() == 'BUSY':
            break
        else:
            pass
    read_rfid(7)
    run_nexo(prog)


# BUFFER S10 after the NEXO
def process10(section):
    while True:
        if section[9].get_status() == 'BUSY':
            break
        else:
            pass
    empty_prog()


# BUFFER S11 after the NEXO
def process11(section):
    while True:
        if section[10].get_status() == 'BUSY':
            break
        else:
            pass
    empty_prog()


# ENGRAVER
def process12(section, prog=0):
    while True:
        if section[11].get_status() == 'BUSY':
            break
        else:
            pass
    read_rfid(8)
    run_engraver(prog)
    while True:
        if section[11].get_status() == 'DONE' and section[12].get_counter() < section[12].get_max_pallets_num():
            break
        else:
            pass
    section[12].counter_increase()
    pass_unit('S12')


# BIG BUFFER S13
def process13(section):
    while True:
        if section[12].get_counter() > 0 and section[13].get_status() == 'IDLE':
            break
        else:
            pass
    section[13].set_satus('WAIT')
    section[12].counter_decrease()
    pass_unit('S13')


# BUFFER S14 before the PORTAL
def process14(section):
    while True:
        if section[13].get_status() == 'BUSY':
            break
        else:
            pass
    empty_prog()
