import linuxcnc

# Connect to LinuxCNC
c = linuxcnc.command()
s = linuxcnc.stat()

c.state(linuxcnc.STATE_ESTOP_RESET)
c.state(linuxcnc.STATE_ON)