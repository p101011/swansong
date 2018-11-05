import math

import constants


# standard units:
# L, s, kg, m


class BloodSource:
    def __init__(self, name, coords):

        self.name = name
        self.length = 0
        self.current_volume = 0
        self.max_volume = 0
        self.max_output = 0
        self.broken = False
        self.children = []
        self.render_radius = 1

        #  Renderer info
        self.coords = coords
        self.pulse_clock = 0

    def add_recipient(self, receiver):
        self.children.append(receiver)

    def give_blood(self, volume):
        #  note that breaks are modeled at root of artery (before it branches)
        #  for the first pass, special handling
        #  TODO: (bloodsource second pass) blood will ALWAYS leave artery, no special case
        if self.broken:
            overflow = self.current_volume / 4
        else:
            self.current_volume += volume
            overflow = max(0, self.current_volume - self.max_volume)
            # TODO: (blood pressure) handle overflow > max output
            # if overflow > self.max_output:
            #     pass
        self.current_volume -= overflow
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
        return "%s has %f/%f mL remaining" % (self.name, self.current_volume, self.max_volume)


class Heart(BloodSource):
    def __init__(self, name, coords):
        super().__init__(name, coords)
        self.current_volume = 0.280
        self.max_volume = 0.280
        self.max_output = 0.280
        self.length = 1
        # store heart rate as bps
        self.rate = 1


class BloodVessel(BloodSource):
    def __init__(self, name, diameter, length, coords):
        # TODO: (URGENT) diameter >> max_volume, investigate units
        super().__init__(name, coords)
        self.length = length
        self.current_volume = 0
        self.max_volume = diameter * length
        self.max_output = diameter
        self.diameter = diameter
        self.velocity_mod = 1 / (math.pi * (diameter / 2) ** 2)

    def __str__(self):
        return super().__str__() + " with %f diameter" % self.diameter
