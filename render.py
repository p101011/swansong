import math
import time
import pygame
import constants


class Renderer:

    # TODO: https://stackoverflow.com/questions/49014660/tinting-an-image-in-pygame
    # TODO: Use above to tint arteries, rather than circles

    def __init__(self, core_surface, model):
        self.surface = core_surface
        self.model = model
        self.circ_system = model.circulatory_system
        self.bleed_icon = pygame.image.load('res\\bleed.jpg')
        self.heal_icon = pygame.image.load('res\\heal.jpg')
        self.background_image = pygame.image.load('res\\scaled_system.jpg')
        self.reset_image = pygame.image.load('res\\reset.jpg')
        self.notification_end = 0
        self.status_text = ""
        self.text_font = pygame.font.SysFont('Courier New', 30)
        self.renderables = []

    def draw_frame(self, frame):
        self.surface.fill(constants.BACKGROUND_COLOR)
        self.surface.blit(self.background_image, constants.MODEL_OFFSET)
        self.surface.blit(self.reset_image, constants.RESET_COORDS)
        self.renderables = [Renderable(pygame.Rect(constants.RESET_COORDS, constants.RESET_SIZE), "button", "reset")]
        for blood_source_key in self.model.circulatory_system.network:
            source = self.model.circulatory_system.network[blood_source_key]
            if source.coords is not None and len(source.coords) != 0:
                if source.pulse_clock == constants.PULSE_DELAY:
                    source_color = constants.FLASH_COLOR
                    source.pulse_clock = 0
                elif source.broken:
                    source.pulse_clock += 1
                    source_color = constants.EMPTY_COLOR
                else:
                    # TODO: reimplement this logic
                    # source_loss = (source.nominal_output - source.total_output) / source.nominal_output
                    # r_delta = int(abs((constants.HEALTHY_ARTERY_COLOR[0] - constants.EMPTY_COLOR[0])) * (1 - source_loss))
                    # g_delta = int(abs((constants.HEALTHY_ARTERY_COLOR[1] - constants.EMPTY_COLOR[1])) * (1 - source_loss))
                    # b_delta = int(abs((constants.HEALTHY_ARTERY_COLOR[2] - constants.EMPTY_COLOR[2])) * (1 - source_loss))
                    # source_color = (r_delta, g_delta, b_delta)
                    if 0 < source.current_volume < source.max_volume - constants.PRECISION_TOLERANCE:
                        source_color = constants.DEBUG_COLOR
                    elif source.current_volume < source.max_volume - constants.PRECISION_TOLERANCE:
                        source_color = constants.EMPTY_COLOR
                    else:
                        source_color = constants.HEALTHY_ARTERY_COLOR
                if len(source.coords) == 1:
                    vessel_rect = pygame.draw.circle(self.surface, source_color, source.coords[0], source.render_radius)
                elif source.render_fill:
                    vessel_rect = pygame.draw.polygon(self.surface, source_color, source.coords, source.render_radius)
                else:
                    vessel_rect = pygame.draw.lines(self.surface, source_color, False, source.coords,
                                                    source.render_radius)
                # TODO: This won't work with line segments, need different logic
                self.renderables.append(Renderable(vessel_rect, "bloodsource", source))
        self.draw_stats()
        x = time.time()
        if self.notification_end > time.time():
            self.draw_text(self.status_text)
        elif self.notification_end != 0:
            self.notification_end = 0

    def draw_stats(self):
        self.draw_bloodloss()
        self.draw_bleed()
        self.print_heartrate()

    def draw_bloodloss(self):
        normalized_blood_volume = (self.circ_system.total_blood - self.circ_system.blood_loss) \
                                  / self.circ_system.total_blood
        # TODO: optimize pie chart drawing?
        # if normalized_blood_volume > 0.5:  # more blood then not, so quicker to draw missing arc
        end_angle = constants.PIE_START_ANGLE + int(360 * (1 - normalized_blood_volume))
        poly_color = constants.EMPTY_COLOR
        circle_color = constants.PIECHART_BLOOD_COLOR
        # else:  # otherwise quicker to draw remaining blood (smaller pie slice)
        #     end_angle = constants.PIE_START_ANGLE + int(360 * normalized_blood_volume)
        #     poly_color = constants.PIECHART_BLOOD_COLOR
        #     circle_color = constants.EMPTY_COLOR
        poly_points = [constants.PIECHART_COORDS]
        for dt in range(constants.PIE_START_ANGLE, end_angle):
            x = (constants.PIECHART_COORDS[0] + int(constants.PIECHART_RADIUS * math.cos(dt * math.pi / 180)))
            y = constants.PIECHART_COORDS[1] + int(constants.PIECHART_RADIUS * math.sin(dt * math.pi / 180))
            poly_points.append((x, y))
        poly_points.append(constants.PIECHART_COORDS)
        pygame.draw.circle(self.surface, circle_color, constants.PIECHART_COORDS, constants.PIECHART_RADIUS)
        if len(poly_points) > 2:
            pygame.draw.polygon(self.surface, poly_color, poly_points)

    def print_heartrate(self):
        pass

    def draw_bleed(self):
        if self.model.bleeding:
            self.surface.blit(self.bleed_icon, constants.BLEED_ICON_COORDS)
            self.surface.blit(self.heal_icon, constants.HEAL_ICON_COORDS)
            self.renderables.append(Renderable(pygame.Rect(constants.HEAL_ICON_COORDS, (49, 49)), "button", "heal"))

    def draw_text(self, string):
        text_surf = self.text_font.render(string, False, constants.NOTIFICATION_TEXT_COLOR)
        self.surface.blit(text_surf, constants.NOTIFICATION_COORDS)

    def notify(self, string, duration):
        self.status_text = string
        self.notification_end = time.time() + duration


class Renderable:
    def __init__(self, rect, archetype, data):
        self.rect = rect
        self.type = archetype
        self.data = data
