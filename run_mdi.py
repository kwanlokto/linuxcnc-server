import linuxcnc
import time
from definitions import state_names

def print_state(task_state):
    return state_names.get(task_state, "UNKNOWN_STATE")

# Connect to LinuxCNC
c = linuxcnc.command()
s = linuxcnc.stat()

# Make sure machine is ON
c.state(linuxcnc.STATE_ON)
time.sleep(1)

# Switch to MDI mode and send a command
def ok_for_mdi():
    s.poll()
    return not s.estop and s.enabled and (s.homed.count(1) == s.joints) and (s.interp_state == linuxcnc.INTERP_IDLE)

if ok_for_mdi():
    c.mode(linuxcnc.MODE_AUTO)
    # Load and run a test program
    c.program_open('test.ngc')
    c.auto()
c.wait_complete()  # Wait for command to finish

# Poll status and print positions
s.poll()
print("Axis positions:", s.actual_position)  # X, Y, Z
print("Machine state:", print_state(s.task_state))
