import pygame

import circulatory
import mouse_handler
import render


def main():
    pygame.init()
    game_display = pygame.display.set_mode((405, 1000))
    pygame.display.set_caption("Circulatory Diagram")
    background_image = pygame.image.load('model\\circ_system.jpg')
    clock = pygame.time.Clock()
    person = circulatory.Organism()
    renderer = render.Renderer(game_display, person, background_image)
    should_exit = False
    while not should_exit:

        for event in pygame.event.get():

            # reset button would be cool

            if event.type == pygame.QUIT:
                should_exit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                blood_source = mouse_handler.get_blood_source(pygame.mouse.get_pos(), person.circulatory_system.network)
                if blood_source is not None:
                    print(blood_source)
                    person.circulatory_system.destroy_vessel(blood_source)

        person.tick()

        renderer.draw_frame()
        pygame.display.update()
        clock.tick(30)
        print(clock.get_fps())


main()
