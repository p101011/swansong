import pygame

SOURCE_DIAMETER_FACTOR = 60
HEALTHY_COLOR = (255, 0, 0)
FLASH_COLOR = (255, 96, 96)
EMPTY_COLOR = (0, 0, 0)


def draw_frame(surface, model, background_image):
    surface.blit(background_image, (0, 0))
    for blood_source_key in model.circulatory_system.network:
        source = model.circulatory_system.network[blood_source_key]
        if source.coords is not None and len(source.coords) != 0:
            radius = max(int(source.total_output * SOURCE_DIAMETER_FACTOR), 1)
            if source.pulse:
                    source_color = FLASH_COLOR
            else:
                source_loss = (source.nominal_output - source.total_output) / source.nominal_output
                r_delta = int((HEALTHY_COLOR[0] - EMPTY_COLOR[0]) * (1 - source_loss))
                g_delta = int((HEALTHY_COLOR[1] - EMPTY_COLOR[1]) * (1 - source_loss))
                b_delta = int((HEALTHY_COLOR[2] - EMPTY_COLOR[2]) * (1 - source_loss))
                source_color = (r_delta, g_delta, b_delta)
            if source.broken:
                source.pulse = not source.pulse
            pygame.draw.circle(surface, source_color, source.coords[0], radius)
