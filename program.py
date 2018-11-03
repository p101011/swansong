import pygame

import circulatory
import constants
import events
import mouse_handler
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
    frame_time = 0
    while not should_exit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                should_exit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                print(abs(pygame.mouse.get_pos()[0] - constants.RESET_COORDS[0]) <= constants.RESET_SIZE[0])
                print(abs(pygame.mouse.get_pos()[1] - constants.RESET_COORDS[1]) <= constants.RESET_SIZE[1])
                if abs(pygame.mouse.get_pos()[0] - constants.RESET_COORDS[0]) <= constants.RESET_SIZE[0] and\
                        abs(pygame.mouse.get_pos()[1] - constants.RESET_COORDS[1]) <= constants.RESET_SIZE[1]:
                        renderer.notify("Resetting Model", constants.NOTIFICATION_DURATION)
                        person.reset()
                else:
                    blood_source = mouse_handler.get_blood_source(pygame.mouse.get_pos(), person.circulatory_system.network)
                    if blood_source is not None:
                        person.circulatory_system.destroy_vessel(blood_source)

            if event.type == events.ORGANISM_BLEEDING:
                person.bleeding = True

            if event.type == events.ORGANISM_DEAD:
                person.kill()

        person.tick(frame_time)
        renderer.draw_frame()
        pygame.display.update()
        clock.tick(constants.FRAMERATE)
        frame_time = clock.get_time()
        # print(clock.get_fps())


main()
