import linuxcnc
import time

# Connect to LinuxCNC
c = linuxcnc.command()
s = linuxcnc.stat()

# Make sure machine is ON
c.state(linuxcnc.STATE_ON)
time.sleep(1)

# Switch to MDI mode and send a command
c.mode(linuxcnc.MODE_MDI)
c.mdi("G0 X10 Y5 Z2")  # Move to coordinates
c.wait_complete()      # Wait for command to finish

# Poll status and print positions
s.poll()
print("Axis positions:", s.actual_position)  # X, Y, Z
print("Machine state:", s.task_state)
