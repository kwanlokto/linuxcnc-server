import linuxcnc
import time

# Connect to LinuxCNC
c = linuxcnc.command()
s = linuxcnc.stat()

def wait_homed(joint):
    """Wait until the specified joint is homed."""
    s = linuxcnc.stat()
    s.poll()
    t = 0.0
    i = 0
    homed = s.joint[joint]["homed"]
    while not homed:
        time.sleep(0.1)
        t = t + 0.1
        i = i + 1
        s.poll()
        homed = s.joint[joint]["homed"]
        if i == 10:
            i = 0
            print(f"Time: {t}. Joint {joint}. Homed: {homed}")


# Come out of E-stop, turn the machine on, home, and switch to Auto mode.
c.state(linuxcnc.STATE_ESTOP_RESET)
c.state(linuxcnc.STATE_ON)
time.sleep(1)

c.mode(linuxcnc.MODE_MANUAL)
c.wait_complete()
c.teleop_enable(False)
c.wait_complete()

# Home each axis individually
c.unhome(2)
c.home(2)  # Home Z axis
wait_homed(2)
c.unhome(0)
c.home(0)  # Home X axis
wait_homed(0)
c.unhome(1)
c.home(1)  # Home Y axis
wait_homed(1)

c.mode(linuxcnc.MODE_AUTO)
