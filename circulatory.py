import pygame

import circ_builder
import events
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

    def reset(self):
        self.circulatory_system.reset()


class CirculatorySystem:
    def __init__(self, parent):
        self.total_blood = 4.7
        self.parent = parent
        self.blood_loss = 0
        self.blood_loss_rate = 0
        self.network = circ_builder.build_network()
        self.calculate_flow(self.network["Heart"], True)

    def get_blood_pressure(self, blood_source):
        if type(blood_source) is organelles.Heart:
            return blood_source.total_output
        vessel_resistance = 1 / (blood_source.diameter ** 4)
        return self.network["Heart"].total_output * vessel_resistance

    def destroy_vessel(self, blood_vessel):
        if blood_vessel.broken:
            return
        self.blood_loss_rate += blood_vessel.destroy()
        self.calculate_flow(blood_vessel)

    def calculate_flow(self, source, initial=False):
        blood_seepage = 1
        pool = source.total_output
        total_diameter = sum([x.diameter for x in source.children])
        for branch in source.children:
            branch_allotment = branch.diameter / total_diameter * pool * blood_seepage
            branch.set_output(branch_allotment, initial)
            self.calculate_flow(branch, initial)

    def update_heartrate(self):
        current_heart_output = self.network["Heart"].total_output
        #  will eventually make this target a certain blood pressure - until then, arbitrary
        self.network["Heart"].rate += 50 * self.blood_loss_rate
        self.calculate_flow(self.network["Heart"])

    def reset(self):
        self.blood_loss = 0
        self.blood_loss_rate = 0
        self.calculate_flow(self.network["Heart"], True)

    def tick(self, frametime):
        temp = self.blood_loss
        self.blood_loss += (self.blood_loss_rate * frametime / 1000)
        if temp == 0 and self.blood_loss > 0:
            pygame.event.post(pygame.event.Event(events.ORGANISM_BLEEDING, {"bleeding": True}))
        if self.blood_loss >= self.total_blood:
            pygame.event.post(pygame.event.Event(events.ORGANISM_DEAD, {"dead": True}))

    def print_status(self):
        print("This system is losing %d mL of blood per second, and has %f L of blood remaining" %
              (self.blood_loss_rate * 1000, self.total_blood - self.blood_loss))


