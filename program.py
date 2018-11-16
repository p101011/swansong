import pygame

import circulatory
import constants
import render

def main():
    pygame.init()
    pygame.font.init()
    background = pygame.display.set_mode((constants.X_RES, constants.Y_RES))
    pygame.display.set_caption("Circulatory Diagram")
    clock = pygame.time.Clock()
    person = circulatory.Organism()
    renderer = render.Renderer(background, person)
    should_exit = False
    frame_time = 7  # TODO: this is a hack used for initial flow cycle
    frame = 0
    while not should_exit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                should_exit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                for renderable in [x for x in renderer.renderables if x.rect.collidepoint(pygame.mouse.get_pos())]:
                    if renderable.type == "button":
                        if renderable.data == "reset":
                            renderer.notify("Resetting Model", constants.NOTIFICATION_DURATION)
                            person.reset()
                        elif renderable.data == "heal":
                            renderer.notify("Healing", constants.NOTIFICATION_DURATION)
                            person.heal()
                    elif renderable.type == "bloodsource":
                        print(renderable.data)
                        if not renderable.data.broken:
                            person.bleeding = True
                            person.circulatory_system.destroy_vessel(renderable.data)

        person.tick(frame_time)
        renderer.draw_frame(frame)
        pygame.display.update()
        clock.tick(constants.FRAMERATE)
        frame_time = clock.get_time()
        frame += 1


main()
