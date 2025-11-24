import linuxcnc

s = linuxcnc.stat()


mill_state_switcher = {
    linuxcnc.RCS_DONE: "RCS_DONE",
    linuxcnc.RCS_EXEC: "RCS_EXEC",
    linuxcnc.RCS_ERROR: "RCS_ERROR",
}
task_mode = s.task_state

if task_mode is linuxcnc.STATE_ESTOP:
    mill_state_str = "STATE_ESTOP"
elif task_mode is linuxcnc.STATE_ESTOP_RESET:
    mill_state_str = "STATE_ESTOP_RESET"
elif self.atc.hal["atc-hal-busy"] or self.atc.hal["atc-tray-status"]:
    mill_state_str = "TOOL_CHANGE"
elif task_mode is linuxcnc.STATE_ON:
    mill_state_str = mill_state_switcher[mill_state]
elif task_mode is linuxcnc.STATE_OFF:
    mill_state_str = "STATE_OFF"

resp = {
    "state": mill_state_str,
    "scanner_state": self.is_usbio_relay_on(0),
    "scanner_cover_state": self.is_usbio_relay_on(1),
    "chip_blower_state": self.is_usbio_relay_on(2),
    "is_door_locked": self.door_locked_status,
    "is_door_open": self.door_open_status,
    "is_door_switch_enabled": self.settings.door_sw_enabled,
    # Pressure sensor == true, means not enough pressure in atc
    "is_enough_air_pressure": not self.hal["atc-pressure-status"],
    # True means all axis are referenced otherwise not referenced yet
    "are_axis_referenced": (
        s.homed[0] == 1 and
        s.homed[1] == 1 and
        s.homed[2] == 1 and
        s.homed[3] == 1
    ),
    "tool_in_spindle": s.tool_in_spindle,
}