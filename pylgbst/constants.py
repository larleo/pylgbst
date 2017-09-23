import binascii
import struct
import sys

if sys.version_info[0] == 2:
    import Queue as queue
else:
    import queue as queue

queue = queue  # just to use it


def str2hex(data):
    return binascii.hexlify(data).decode("utf8")


def usbyte(seq, index):
    return struct.unpack("<B", seq[index:index + 1])[0]


def ushort(seq, index):
    return struct.unpack("<H", seq[index:index + 2])[0]


# GENERAL
MOVE_HUB_HARDWARE_HANDLE = 0x0E
MOVE_HUB_HARDWARE_UUID = '00001624-1212-efde-1623-785feabcd123'

PACKET_VER = 0x01

# PORTS
PORT_C = 0x01
PORT_D = 0x02
PORT_LED = 0x32
PORT_A = 0x37
PORT_B = 0x38
PORT_AB = 0x39
PORT_TILT_SENSOR = 0x3A
PORT_AMPERAGE = 0x3B
PORT_VOLTAGE = 0x3C

PORTS = {
    PORT_A: "A",
    PORT_B: "B",
    PORT_AB: "AB",
    PORT_C: "C",
    PORT_D: "D",
    PORT_LED: "LED",
    PORT_TILT_SENSOR: "TILT_SENSOR",
    PORT_AMPERAGE: "AMPERAGE",
    PORT_VOLTAGE: "VOLTAGE",
}

# PACKET TYPES
MSG_DEVICE_INFO = 0x01
# 0501010305 gives 090001030600000010
MSG_DEVICE_SHUTDOWN = 0x02  # sent when hub shuts down by button hold
MSG_PING_RESPONSE = 0x03
MSG_PORT_INFO = 0x04
MSG_PORT_CMD_ERROR = 0x05
MSG_SET_PORT_VAL = 0x81
MSG_PORT_STATUS = 0x82
MSG_SENSOR_SUBSCRIBE = 0x41
MSG_SENSOR_SOMETHING1 = 0x42  # it is seen close to sensor subscribe commands. Subscription options? Initial value?
MSG_SENSOR_DATA = 0x45
MSG_SENSOR_SUBSCRIBE_ACK = 0x47

# DEVICE TYPES
DEV_VOLTAGE = 0x14
DEV_AMPERAGE = 0x15
DEV_LED = 0x17
DEV_DCS = 0x25
DEV_IMOTOR = 0x26
DEV_MOTOR = 0x27
DEV_TILT_SENSOR = 0x28

DEVICE_TYPES = {
    DEV_DCS: "DISTANCE_COLOR_SENSOR",
    DEV_IMOTOR: "IMOTOR",
    DEV_MOTOR: "MOTOR",
    DEV_TILT_SENSOR: "TILT_SENSOR",
    DEV_LED: "LED",
    DEV_AMPERAGE: "AMPERAGE",
    DEV_VOLTAGE: "VOLTAGE",
}

# NOTIFICATIONS
STATUS_STARTED = 0x01
STATUS_CONFLICT = 0x05
STATUS_FINISHED = 0x0a

# COLORS
COLOR_BLACK = 0x00
COLOR_PINK = 0x01
COLOR_PURPLE = 0x02
COLOR_BLUE = 0x03
COLOR_LIGHTBLUE = 0x04
COLOR_CYAN = 0x05
COLOR_GREEN = 0x06
COLOR_YELLOW = 0x07
COLOR_ORANGE = 0x09
COLOR_RED = 0x09
COLOR_WHITE = 0x0a
COLOR_NONE = 0xFF
COLORS = {
    COLOR_BLACK: "BLACK",
    COLOR_PINK: "PINK",
    COLOR_PURPLE: "PURPLE",
    COLOR_BLUE: "BLUE",
    COLOR_LIGHTBLUE: "LIGHTBLUE",
    COLOR_CYAN: "CYAN",
    COLOR_GREEN: "GREEN",
    COLOR_YELLOW: "YELLOW",
    COLOR_ORANGE: "ORANGE",
    COLOR_RED: "RED",
    COLOR_WHITE: "WHITE",
    COLOR_NONE: "NONE"
}
