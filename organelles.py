import math

# standard units:
# L, s, kg, m


class BloodSource:
    def __init__(self, surface, coords=None):
        # this doesn't get modified on init
        self.total_output = 0
        self.nominal_output = 0
        self.broken = False
        self.children = []

        #  Renderer info
        self.coords = coords
        self.pulse = False

    def add_recipient(self, receiver):
        self.children.append(receiver)

    def set_output(self, lps, initial=False):
        self.total_output += lps
        if initial:
            self.nominal_output = lps

    def destroy(self):
        for vessel in self.children:
            vessel.destroy()
        temp, self.total_output = self.total_output, 0
        return temp

    def print_status(self, name):
        print("%s is giving %d mL to %d children" % (name, self.total_output * 1000, len(self.children)))

    def draw(self):
        pass

    def __str__(self):
        return ("%f feeds into " % self.total_output) + str(self.children)


class Heart(BloodSource):
    def __init__(self, coords=None):
        super().__init__(coords)
        self.volume = 0.280
        # store heart rate as bps
        self.rate = 1
        self.set_output(self.volume * self.rate, True)

    def set_rate(self, rate):
        self.rate = rate
        old_out = self.total_output
        new_out = self.volume * self.rate
        self.set_output(new_out - old_out)


class BloodVessel(BloodSource):
    def __init__(self, diameter, coords=None):
        super().__init__(coords)
        self.diameter = diameter
        self.velocity_mod = 1 / (math.pi * (self.diameter / 2) ** 2)