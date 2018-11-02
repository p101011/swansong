import pygame
import circulatory
import render


def main():
    pygame.init()
    game_display = pygame.display.set_mode((405, 1000))
    pygame.display.set_caption("Circulatory Diagram")
    background_image = pygame.image.load('model\\circ_system.jpg')
    clock = pygame.time.Clock()
    person = circulatory.Organism()
    should_exit = False
    while not should_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_exit = True

        render.draw_frame(game_display, person, background_image)
        pygame.display.update()
        clock.tick(60)


main()
