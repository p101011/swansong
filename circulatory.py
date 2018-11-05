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


# TODO: Implement effects of blood loss (eg. unconciousness when blood pressure too low)
class CirculatorySystem:
    def __init__(self, parent):
        self.total_blood = 4.7
        self.parent = parent
        self.blood_loss = 0
        self.blood_loss_rate = 0
        self.network = circ_builder.build_network()
        self.calculate_flow(self.network["Heart"], 1000, True)

    def get_blood_pressure(self, blood_source):
        if type(blood_source) is organelles.Heart:
            return blood_source.total_output
        vessel_resistance = 1 / (blood_source.diameter ** 4)
        return self.network["Heart"].total_output * vessel_resistance

    def destroy_vessel(self, blood_vessel, frametime):
        if blood_vessel.broken:
            return
        self.blood_loss_rate += blood_vessel.destroy()
        self.calculate_flow(blood_vessel, frametime)

    def heal(self):
        self.blood_loss_rate = 0
        self.network["Heart"].repair_all()

    def calculate_flow(self, source, frametime, initial=False):
        pool = source.total_output
        total_diameter = sum([x.diameter for x in source.children])
        for branch in source.children:
            branch_allotment = branch.diameter / total_diameter * pool * constants.BLOOD_FLOW_FACTOR * frametime / 1000
            # TODO: decouple vessels and update blood I/O frame-by-frame
            # Goal is to properly model the cascade of blood leaving arteries - eg, once the heart breaks, the
            # dorsalis pedis does NOT immediately break as well
            # should hopefully make it easier to implement effects of blood loss
            # every frame should recieve allotment
            branch.set_output(branch_allotment, initial)
            self.calculate_flow(branch, frametime, initial)

    def update_heartrate(self):
        # TODO: Implement Me
        current_heart_output = self.network["Heart"].total_output
        #  will eventually make this target a certain blood pressure - until then, arbitrary
        self.network["Heart"].rate += 50 * self.blood_loss_rate
        # self.calculate_flow(self.network["Heart"])

    def reset(self):
        self.blood_loss = 0
        self.heal()

    def tick(self, frametime):
        self.calculate_flow(self.network["Heart"], frametime)
        self.blood_loss += (self.blood_loss_rate * frametime / 1000)
        if self.blood_loss >= self.total_blood:
            self.blood_loss_rate = 0
            self.blood_loss = self.total_blood

    def print_status(self):
        print("This system is losing %d mL of blood per second, and has %f L of blood remaining" %
              (self.blood_loss_rate * 1000, self.total_blood - self.blood_loss))
