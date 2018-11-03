import math

import pygame

import constants


class Renderer:

    def __init__(self, surface, model, background_image):
        self.surface = surface
        self.model = model
        self.circ_system = model.circulatory_system
        self.background = background_image

    def draw_frame(self):
        self.surface.blit(self.background, (0, 0))
        for blood_source_key in self.model.circulatory_system.network:
            source = self.model.circulatory_system.network[blood_source_key]
            if source.coords is not None and len(source.coords) != 0:
                if source.pulse_clock == constants.PULSE_DELAY:
                        source_color = constants.FLASH_COLOR
                        source.pulse_clock = 0
                else:
                    if source.nominal_output == 0:
                        print("shit")
                    source_loss = (source.nominal_output - source.total_output) / source.nominal_output
                    r_delta = int(abs((constants.HEALTHY_ARTERY_COLOR[0] - constants.EMPTY_COLOR[0])) * (1 - source_loss))
                    g_delta = int(abs((constants.HEALTHY_ARTERY_COLOR[1] - constants.EMPTY_COLOR[1])) * (1 - source_loss))
                    b_delta = int(abs((constants.HEALTHY_ARTERY_COLOR[2] - constants.EMPTY_COLOR[2])) * (1 - source_loss))
                    source_color = (r_delta, g_delta, b_delta)
                if source.broken:
                    source.pulse_clock += 1
                pygame.draw.circle(self.surface, source_color, source.coords[0], source.render_radius)
        self.draw_stats()

    def draw_stats(self):
        self.draw_bloodloss()
        self.print_heartrate()

    def draw_bloodloss(self):
        normalized_blood_volume = (self.circ_system.total_blood - self.circ_system.blood_loss)\
                                  / self.circ_system.total_blood
        if normalized_blood_volume > 0.5:  # more blood then not, so quicker to draw missing arc
            start_angle = 180
            end_angle = start_angle + int(360 * (1 - normalized_blood_volume))
            poly_color = constants.EMPTY_COLOR
            circle_color = constants.PIECHART_BLOOD_COLOR
        else:  # otherwise quicker to draw remaining blood (smaller pie slice)
            start_angle = 0
            end_angle = start_angle + int(360 * normalized_blood_volume)
            poly_color = constants.PIECHART_BLOOD_COLOR
            circle_color = constants.EMPTY_COLOR
        poly_points = [constants.PIECHART_COORDS]
        for dt in range(start_angle, end_angle):
            x = constants.PIECHART_COORDS[0] + int(constants.PIECHART_RADIUS * math.cos(dt * math.pi / 180))
            y = constants.PIECHART_COORDS[1] + int(constants.PIECHART_RADIUS * math.sin(dt * math.pi / 180))
            poly_points.append((x, y))
        poly_points.append(constants.PIECHART_COORDS)
        pygame.draw.circle(self.surface, circle_color, constants.PIECHART_COORDS, constants.PIECHART_RADIUS)
        if len(poly_points) > 2:
            pygame.draw.polygon(self.surface, poly_color, poly_points)

    def print_heartrate(self):
        pass
