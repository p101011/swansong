import math

import constants


# standard units:
# L, s, kg, m


class BloodSource:
    def __init__(self, coords):
        self.total_output = 0
        self.nominal_output = 0
        self.current_volume = 0
        self.broken = False
        self.children = []
        self.render_radius = 1

        #  Renderer info
        self.coords = coords
        self.pulse_clock = 0

    def add_recipient(self, receiver):
        self.children.append(receiver)

    def set_output(self, lps, initial=False):
        self.total_output = lps
        if initial:
            self.nominal_output = lps
            self.render_radius = max(int(self.total_output * constants.SOURCE_RADIUS_FACTOR), 1)

    def destroy(self):
        temp, self.total_output = self.total_output, 0
        self.broken = True
        return temp

    def repair_all(self):
        self.broken = False
        self.total_output = self.nominal_output
        for child in self.children:
            child.repair_all()

    def print_status(self, name):
        print("%s is giving %d mL to %d children" % (name, self.total_output * 1000, len(self.children)))

    # def __str__(self):
    #     return "%f mL\s blood loss" % (self.nominal_output - self.total_output)


class Heart(BloodSource):
    def __init__(self, coords):
        super().__init__(coords)
        self.volume = 0.280
        # store heart rate as bps
        self.rate = 1
        self.set_output(self.volume * self.rate, True)


class BloodVessel(BloodSource):
    def __init__(self, diameter, coords):
        super().__init__(coords)
        self.diameter = diameter
        self.velocity_mod = 1 / (math.pi * (self.diameter / 2) ** 2)

    def __str__(self):
        return super().__str__() + " with %f diameter" % self.diameter
