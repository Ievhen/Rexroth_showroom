# A set of functions
from Demo_line.sql_tools import *


# function returns the list of current sections status for certain product line
def check_status(db):
    req = request('SELECT', '*', 'section_status', where_arg=f'pl_id={1}')
    return execute_request(db, req)[0][1:]


# transfer the signal to Master or/and DB
# we are using TIMER and COIL to serve the signal

# function sets the specific ts_request bit on 1
def pass_unit(db, stop_gate):
    sql = f"UPDATE showroom_database.ts_request SET {stop_gate} = 1 where pl_id = 1"
    update_request(db, sql)


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
    if path == 'TRUE':
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
        write_rfid()
        run_portal(prog)


def check_and_pass(section, start, end):
    if section[start].get_status() == 'DONE' and section[end].get_status() == 'IDLE':
        section[end].set_status('WAIT')
        pass_unit(section[start].get_stop_gate())


def process2():
    pass


def process3():
    pass


def process4():
    pass


def process5():
    pass


def process6():
    pass


def lift_enter_switch():
    pass


def lift_exit_switch():
    pass


def process7():
    pass


def process8():
    pass


def wait_nexo_button():
    pass


def process9():
    pass


def process10():
    pass


def process11():
    pass


def process12():
    pass


def process13():
    pass


def process14():
    pass
