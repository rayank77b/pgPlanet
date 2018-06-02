#!/usr/bin/python
import pygame
from random import randint
import math

X_SCREEN=1024
Y_SCREEN=800
RASTER=1000
ACCEL=5000.0

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

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
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
    
    def _triangle(self, x,y):
        dx = (self.x-x)
        dy = (self.y-y)
        return math.sqrt(dx*dx+dy*dy)
    
    def calc_speed(self, masses):
        self.accel_x = 0.0
        self.accel_y = 0.0
        for m in masses:
            if((self.x!=m.x) and (self.y!=m.y)):
                delta = self._triangle(m.x, m.y)
                #print delta, 
                self.accel_x = self.accel_x + ACCEL*(1.0*self.d*m.d)*(m.x-self.x)/(delta*delta)
                self.accel_y = self.accel_y + ACCEL*(1.0*self.d*m.d)*(m.y-self.y)/(delta*delta)
        #print "xy ( %d | %d) v: ( %d | %d) acell: ( %f | %f ) "%(self.x,self.y, self.speed_x, self.speed_y,self.accel_x,self.accel_y)
        self.speed_x = self.speed_x + self.accel_x
        self.speed_y = self.speed_y + self.accel_y
    
    def draw_me(self, screen):
        # draw the object
        pygame.draw.circle(screen, BLUE, [int(self.x/RASTER), int(self.y/RASTER)], self.d)
        # draw the veloecity
        pygame.draw.line(screen, WHITE, [int(self.x/RASTER), int(self.y/RASTER)], [int(self.x/RASTER)+self.speed_x/10, int(self.y/RASTER)+self.speed_y/10], 1)
        # draw the acceleration
        pygame.draw.line(screen, RED, [int(self.x/RASTER), int(self.y/RASTER)], [int(self.x/RASTER)+self.accel_x*5, int(self.y/RASTER)+self.accel_y*5], 1)


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
    for i in range(50):
        x=randint(350*X_SCREEN, X_SCREEN*750)
        y=randint(350*Y_SCREEN, Y_SCREEN*750)
        radius = randint(2,5)
        xv = randint(-15,15)
        yv = randint(-15,15)
        print "( %d | %d ) r: %d   xv: %d  yv: %d"%(int(x/RASTER),int(y/RASTER), radius, xv, yv)
        m.append(Mass(x,y,radius, xv, yv,0,0))
    while running:
        #clock.tick(60) # frame rate 60 ticks
        screen.fill((0, 0, 0))
        running = key_events()
        for m1 in m:
            m1.calc_speed(m)
            m1.calc_xy()
            m1.draw_me(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()