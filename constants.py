# RENDERER CONSTANTS #

HEALTHY_ARTERY_COLOR = (255, 0, 0)
FLASH_COLOR = (255, 96, 96)
EMPTY_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
NOTIFICATION_TEXT_COLOR = (20, 20, 20)
DEBUG_COLOR = (255, 20, 144)

PIECHART_BLOOD_COLOR = (0, 200, 0)
PIECHART_COORDS = (75, 68)
PIECHART_RADIUS = 60
PIE_START_ANGLE = -90

BLEED_ICON_COORDS = (140, 40)
HEAL_ICON_COORDS = (180, 40)

RESET_SIZE = (100, 56)
RESET_COORDS = (70, 750)

NOTIFICATION_COORDS = (120, 500)
NOTIFICATION_DURATION = 1
SOURCE_RADIUS_FACTOR = 1200  # scalar for blood vessel radius on render
PULSE_DELAY = 60  # number of frames between flashes of destroyed blood sources
X_RES = 338 * 2
MODEL_OFFSET = (338, 0)
Y_RES = 1000

# SIMULATION CONSTANTS #

MODEL_HEIGHT = 1.6
NOMINAL_BLOOD_PRESSURE = 100  # average of systolic and diastolic (120 / 80), since we don't model pumps (yet)
PIXELS_PER_METER = Y_RES / MODEL_HEIGHT
FRAMERATE = 144
BLOOD_FLOW_FACTOR = 1  # percent of blood which is pushed from artery; 1 for complete blood transfer
BLOOD_CELL_LENGTH = 0.01  # length of each distinct cell in a blood vessel in m
PRECISION_TOLERANCE = 0.00001
CELL_DRAIN_RATE = 1  # cells drained per second
