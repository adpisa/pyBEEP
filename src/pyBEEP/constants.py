# Constants
POINT_INTERVAL_POT = 0.00036
POINT_INTERVAL_GAL = 0.0192
REG_READ_ADDR = 0x100
REG_WRITE_ADDR_PID = 0x4F00
REG_WRITE_ADDR_POT = 0x200

# Command Dictionary
CMD = {
    "SENSOR_ZERO": 0xE0,
    "RESET": 0xE1,
    "LOADDFLT": 0xE2,
    "SET_TIA_GAIN": 0xE3,
    "SET_SWITCH": 0xE4,
    "FIFO_START": 0xE5,
    "PID_START": 0xE6,
    "TEST_STOP": 0xE7,
    "CLEAR_FIFO": 0xE8,
    "CFG_SAVE": 0xF0,
}

# Gain Dictionary
GAIN = {
    '1K': 0,
    '10K':1,
    '100K':2,
    '1M':3,
    '10M':4,
}   