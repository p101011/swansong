import collections
import events
import circ_builder


class Organism:
    def __init__(self):
        self.is_dead = False
        self.bleeding = False
        self.circulatory_system = CirculatorySystem(self)
        self.events = collections.deque()

    def tick(self):
        self.circulatory_system.tick()
        while len(self.events) > 0:
            event = self.events.pop()
            self.handle_event(event)

    def send_event(self, event):
        self.events.append(event)

    def handle_event(self, event):
        if type(event) == events.DeathEvent:
            self.is_dead = True
        elif type(event) == events.ChangeBleeding:
            self.bleeding = event.args[0]
            self.circulatory_system.update_heartrate()


class CirculatorySystem:
    def __init__(self, parent):
        self.total_blood = 4.7
        self.parent = parent
        self.blood_loss = 0
        self.blood_loss_rate = 0
        self.network = circ_builder.build_network()
        self.calculate_flow(self.network["Heart"])

    def get_blood_pressure(self, blood_source):
        if type(blood_source) is Heart:
            return blood_source.total_output
        vessel_resistance = 1 / (blood_source.diameter ** 4)
        return self.network["Heart"].total_output * vessel_resistance

    def destroy_vessel(self, blood_vessel):
        if blood_vessel.broken:
            return
        self.blood_loss_rate += blood_vessel.destroy()
        self.calculate_flow(blood_vessel)
        self.parent.send_event(events.ChangeBleeding([True]))

    def calculate_flow(self, source):
        blood_seepage = 1
        pool = source.total_output
        total_diameter = sum([x.diameter for x in source.children])
        for branch in source.children:
            branch_allotment = branch.diameter / total_diameter * pool * blood_seepage
            branch.set_output(branch_allotment, True)
            self.calculate_flow(branch)

    def update_heartrate(self):
        current_heart_output = self.network["Heart"].total_output
        #  will eventually make this target a certain blood pressure - until then, arbitrary
        self.network["Heart"].rate += 50 * self.blood_loss_rate
        self.calculate_flow(self.network["Heart"])

    def tick(self):
        self.blood_loss += self.blood_loss_rate
        if self.blood_loss >= self.total_blood:
            self.blood_loss_rate = 0
            self.blood_loss = self.total_blood
            self.parent.send_event(events.DeathEvent(None))

    def print_status(self):
        print("This system is losing %d mL of blood per second, and has %f L of blood remaining" %
              (self.blood_loss_rate * 1000, self.total_blood - self.blood_loss))


