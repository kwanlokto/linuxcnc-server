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
c.mode(linuxcnc.MODE_MDI)
c.wait_complete()
c.mdi("G0 X1 Y1 Z2")  # Move to coordinates
c.wait_complete()  # Wait for command to finish

# Poll status and print positions
s.poll()
print("Axis positions:", s.actual_position)  # X, Y, Z
print("Machine state:", print_state(s.task_state))
