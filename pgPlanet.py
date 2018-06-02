#!/usr/bin/python
import pygame
from random import randint
import math

X_SCREEN=1024
Y_SCREEN=800

class Mass:
    def __init__(self,x,y,d,xv,yv, xa, ya):
        self.x=x
        self.y=y
        self.d=d  # durchmesser
        self.speed_x=xv
        self.speed_y=yv
        self.accel_x=xa
        self.accel_y=ya
    
    def calc_xy(self):
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
    
    def _triangle(self, x,y):
        dx = (self.x-x)
        dy = (self.y-y)
        return math.sqrt(dx*dx+dy*dy)
    
    def calc_speed(self, masses):
        for m in masses:
            if((self.x!=m.x) and (self.y!=m.y)):
                delta = self._triangle(m.x, m.y)
                c = (self.d*m.d)/(delta*delta)
                if(self.x<m.x):
                    self.accel_x = self.accel_x + c
                else:
                    self.accel_x = self.accel_x - c
                if(self.y<m.y):
                    self.accel_y = self.accel_y + c
                else:
                    self.accel_y = self.accel_y - c
        self.speed_x = self.speed_x + self.accel_x
        self.speed_y = self.speed_y + self.accel_y
    
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
    
    m=list()
    for i in range(2):
        m.append(Mass(randint(0,X_SCREEN),randint(0,Y_SCREEN),randint(2,10), randint(-5,5),randint(-5,5),0,0))
    while running:
        clock.tick(60) # frame rate 60 ticks
        screen.fill((0, 0, 0))
        running = key_events()
        for m1 in m:
            m1.calc_speed(m)
            m1.calc_xy()
            m1.draw_me(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()