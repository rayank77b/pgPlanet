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
    x=600
    y=400
    direction_x=1
    direction_y=1
    speed_x=5
    speed_y=5

    while running:
        clock.tick(30) # frame rate 30 ticks
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x,y, 20, 20))
        if(direction_x==1):
            if(x>770):
                direction_x=-1
        if(direction_x==-1):
            if(x<0):
                direction_x=1
        if(direction_y==1):
            if(y>570):
                direction_y=-1
        if(direction_y==-1):
            if(y<0):
                direction_y=1
        x=x+direction_x*speed_x
        y=y+direction_y*speed_y
        pygame.display.flip()

if __name__ == '__main__':
    main()