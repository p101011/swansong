import math

import constants


# standard units:
# L, s, kg, m


class BloodSource:
    def __init__(self, name, coords):

        self.name = name
        self.length = 0
        self.broken = False
        self.children = []

        # vessel contents state
        # each cell is 0.01 m long
        # and can hold 0.01 * radius L (m * m^2)
        # each tick crawls cells along by volume input (if get 3 cells of volume, cells move 3 places)
        # if input = 0, then 1 cell crawls
        # TODO: tick movement rate relates to blood pressure
        self.contents = []
        self.max_cell_volume = 0
        # the following are kept for debug, and shouldn't used in simulation
        self.current_volume = 0
        self.max_volume = 0

        self.render_radius = 1

        #  Renderer info
        self.coords = coords
        self.pulse_clock = 0

    def add_recipient(self, receiver):
        self.children.append(receiver)

    def give_blood(self, volume):
        #  note that breaks are modeled at root of artery (before it branches)
        if self.broken:
            volume = 0
        full_crawlers = int(max((1, volume // self.max_cell_volume)))
        partial_fill = volume - (full_crawlers * self.max_cell_volume)
        overflow = sum(self.contents[-full_crawlers:])
        for i in range(len(self.contents) - 1, full_crawlers - 1, -1):
            self.contents[i] = self.contents[i - full_crawlers]
        partial_index = full_crawlers
        while partial_fill > 0 and partial_index < len(self.contents):
            self.contents[partial_index] += partial_fill
            partial_fill = max((0, self.contents[partial_index] - self.max_cell_volume))
            if partial_fill > 0:
                self.contents[partial_index] = self.max_cell_volume
            partial_index += 1
        if partial_fill > 0:
            overflow += partial_fill
        for i in range(full_crawlers):
            if volume == 0:
                # special case
                # TODO: (blood pressure) model velocity of blood loss
                self.contents[i] = 0
            else:
                self.contents[i] = self.max_cell_volume
        self.current_volume += (volume - overflow)
        self.render_radius = min(max(int(self.current_volume * constants.SOURCE_RADIUS_FACTOR), 1), 30)
        return overflow

    def destroy(self):
        self.broken = True
        # TODO: (blood pressure) adjust max output when broken

    def repair_all(self):
        self.broken = False
        for child in self.children:
            child.repair_all()

    def __str__(self):
        return "%s has %f/%f mL remaining" % (self.name, self.current_volume, self.max_volume) + " with" +\
               str(self.contents)


class Heart(BloodSource):
    def __init__(self, name, coords):
        super().__init__(name, coords)
        self.current_volume = 0
        self.contents = [0.7] * 4
        self.max_cell_volume = 0.07
        self.current_volume += sum(self.contents)
        self.max_volume = self.max_cell_volume * len(self.contents)
        self.length = 1
        # store heart rate as bps
        self.rate = 1


class BloodVessel(BloodSource):
    def __init__(self, name, diameter, coords):
        # TODO: (URGENT) diameter >> max_volume, investigate units
        super().__init__(name, coords)
        self.length = 0
        # sum lengths of line segments in pixels
        for i in range(1, len(coords)):
            v1 = coords[i - 1]
            v2 = coords[i]
            self.length += ((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) ** .5
        self.length /= constants.PIXELS_PER_METER
        self.diameter = diameter
        self.max_cell_volume = constants.BLOOD_CELL_LENGTH * self.diameter
        # TODO: model partial cells (eg. cell volume < max_volume)
        self.contents = [0.0] * math.ceil(self.length / constants.BLOOD_CELL_LENGTH)
        self.current_volume = 0
        self.max_volume = self.max_cell_volume * len(self.contents)

        # TODO: (blood pressure) integrate this with blood pressure
        # self.velocity_mod = 1 / (math.pi * (diameter / 2) ** 2)

    def __str__(self):
        return super().__str__()
