import circ_builder
import constants
import organelles


class Organism:
    def __init__(self):
        self.is_dead = False
        self.bleeding = False
        self.circulatory_system = CirculatorySystem(self)

    def tick(self, frametime):
        self.circulatory_system.tick(frametime)

    def kill(self):
        self.is_dead = True
        self.bleeding = False
        self.circulatory_system.blood_loss_rate = 0
        self.circulatory_system.blood_loss = self.circulatory_system.total_blood

    def heal(self):
        self.bleeding = False
        self.circulatory_system.heal()

    def reset(self):
        self.is_dead = False
        self.bleeding = False
        self.circulatory_system.reset()


# TODO: (blood pressure) Implement effects of blood loss (eg. unconciousness when blood pressure too low)
class CirculatorySystem:
    def __init__(self, parent):
        self.total_blood = 4.7
        self.parent = parent
        self.blood_loss = 0
        self.network = circ_builder.build_network()

    def get_blood_pressure(self, blood_source):
        if type(blood_source) is organelles.Heart:
            return blood_source.total_output
        vessel_resistance = 1 / (blood_source.diameter ** 4)
        return self.network["Heart"].total_output * vessel_resistance

    def destroy_vessel(self, blood_vessel):
        blood_vessel.broken = True

    def heal(self):
        self.network["Heart"].repair_all()

    def flow_cycle(self, source, blood_input):
        overflow = source.give_blood(blood_input)
        if source.broken:
            # TODO: bleed out is VERY fast, not double-counting arteries
            # aortic arch bleeds out faster than arch (!?)
            self.blood_loss += blood_input
        total_diameter = sum([x.diameter for x in source.children])
        for branch in source.children:
            branch_allotment = branch.diameter / total_diameter * overflow * constants.BLOOD_FLOW_FACTOR
            self.flow_cycle(branch, branch_allotment)

    # TODO: (blood pressure) implement heartrate
    # def update_heartrate(self):
    #     current_heart_output = self.network["Heart"].total_output
    #     #  will eventually make this target a certain blood pressure - until then, arbitrary
    #     self.network["Heart"].rate += 50 * self.blood_loss_rate
    #     # self.calculate_flow(self.network["Heart"])

    def reset(self):
        self.blood_loss = 0
        self.heal()

    def tick(self, frametime):
        # TODO: hook up heart to system so heart input depends on other network
        frametime = 7
        heart_input = min(self.total_blood - self.blood_loss, 0.28) * frametime / 1000
        self.flow_cycle(self.network["Heart"], heart_input)
        if self.blood_loss >= self.total_blood:
            self.blood_loss = self.total_blood
