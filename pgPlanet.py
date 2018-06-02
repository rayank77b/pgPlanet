#!/usr/bin/python
import pygame
from random import randint

X_SCREEN=800
Y_SCREEN=600

class Mass:
    def __init__(self,x,y,d,xv,yv):
        self.x=x
        self.y=y
        self.d=d  # durchmesser
        self.speed_x=xv
        self.speed_y=yv

    def calc(self):
        if(self.x>(X_SCREEN-self.d)):
            self.speed_x=-1*self.speed_x
        if(self.x<0):
            self.speed_x=-1*self.speed_x
        if(self.y>(Y_SCREEN-self.d)):
            self.speed_y=-1*self.speed_y
        if(self.y<0):
            self.speed_y=-1*self.speed_y
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
    
    def draw_me(self, screen):
        pygame.draw.rect(screen, (0, 128+self.d, 255), pygame.Rect(self.x, self.y, self.d, self.d))

def key_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def randdirect():
    if(randint(0,10)%2):
        return 1
    return -1

def main():
    pygame.init()
    screen = pygame.display.set_mode((X_SCREEN, Y_SCREEN))
    
    pygame.display.set_caption("pgPlanet Version 0.01")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    clock = pygame.time.Clock()
    running=True
    clock.tick(30) # frame rate 30 ticks
    m=list()
    for i in range(50):
        m.append(Mass(randint(0,X_SCREEN),randint(0,Y_SCREEN),randint(2,10), randint(-30,30)/30.0,randint(-30,30)/30.0))
    while running:
        screen.fill((0, 0, 0))
        running = key_events()
        for m1 in m:
            m1.calc()
            m1.draw_me(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()