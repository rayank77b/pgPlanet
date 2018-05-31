#!/usr/bin/python
import pygame
 
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    pygame.display.set_caption("Pygame-Tutorial: Grundlagen")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(30) # frame rate 30 ticks
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                print "keydown"
                if event.key == pygame.K_ESCAPE:
                    print "escape"
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
            pygame.display.flip()

if __name__ == '__main__':
    main()