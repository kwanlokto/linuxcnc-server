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
c.mode(linuxcnc.MODE_MANUAL)
c.wait_complete()
c.teleop_enable(False)
c.wait_complete()
c.home(0)  # Home X axis
c.home(1)  # Home Y axis
c.home(2)  # Home Z axis
