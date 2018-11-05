# RENDERER CONSTANTS #

HEALTHY_ARTERY_COLOR = (255, 0, 0)
FLASH_COLOR = (255, 96, 96)
EMPTY_COLOR = (0, 0, 0)
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
# TODO: switch duration to s rather than frames
NOTIFICATION_DURATION = 30

SOURCE_RADIUS_FACTOR = 900  # scalar for blood vessel radius on render
BLOOD_FLOW_FACTOR = 1  # percent of blood which is pushed from artery; 1 for complete blood transfer
PULSE_DELAY = 60  # number of frames between flashes of destroyed blood sources
FRAMERATE = 144
X_RES = 405
Y_RES = 1000
