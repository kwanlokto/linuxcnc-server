import linuxcnc
import time

# Connect to LinuxCNC
c = linuxcnc.command()
s = linuxcnc.stat()

def wait_homed(joint):
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


# Make sure machine is ON
c.state(linuxcnc.STATE_ON)
time.sleep(1)

# Switch to MDI mode and send a command
c.mode(linuxcnc.MODE_MANUAL)
c.wait_complete()
c.teleop_enable(False)
c.wait_complete()
c.unhome(0)
c.home(0)  # Home X axis
wait_homed(0)
c.unhome(1)
c.home(1)  # Home Y axis
wait_homed(1)
c.unhome(2)
c.home(2)  # Home Z axis
wait_homed(2)
# c.home(3)  # Home Y axis
# wait_homed(3)

