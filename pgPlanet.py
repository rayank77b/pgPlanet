#!/usr/bin/python
import pygame
from random import randint
import math

X_SCREEN=1024
Y_SCREEN=800
RASTER=3001
ACCEL=0.01

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

class Mass:
    def __init__(self,x,y,d):
        self.x=x
        self.y=y
        self.d=d  # durchmesser, masse
        self.speed_x=0.0
        self.speed_y=0.0
        self.accel_x=0.0
        self.accel_y=0.0
    
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
                ma = (self.d*m.d)/(delta*delta)
                self.accel_x = self.accel_x + ACCEL*(m.x-self.x)*ma
                self.accel_y = self.accel_y + ACCEL*(m.y-self.y)*ma
        #print "xy ( %d | %d) v: ( %d | %d) acell: ( %f | %f ) "%(self.x,self.y, self.speed_x, self.speed_y,self.accel_x,self.accel_y)
        self.speed_x = self.speed_x + self.accel_x
        self.speed_y = self.speed_y + self.accel_y
    
    def get_radius(self):
        r = self.d/RASTER
        if r < 1 :
            return 1
        else:
            return int(r)
        
    def draw_me(self, screen, mx, my):
        x = int(self.x/RASTER)
        y = int(self.y/RASTER)
        minx = mx/RASTER - X_SCREEN/2
        miny = my/RASTER - Y_SCREEN/2
        maxx = mx/RASTER + X_SCREEN/2
        maxy = my/RASTER + Y_SCREEN/2
        if((x>minx)and(y>miny)and(x<maxx)and(y<maxy)): # no need to draw all objects
            # draw the object
            pygame.draw.circle(screen, BLUE, [int(x-minx), int(y-miny)], self.get_radius())
            # draw the veloecity
            #pygame.draw.line(screen, WHITE, [x, y], [x+self.speed_x/20, y+self.speed_y/20], 1)
            # draw the acceleration
            #pygame.draw.line(screen, RED, [x, y], [x+self.accel_x*2, y+self.accel_y*2], 1)

def get_mass_point(masses):
    x=0
    y=0
    sum_m=0
    for m in masses:
        x = x + m.x*m.d
        y = y + m.y*m.d
        sum_m = sum_m + m.d
    #print " (%d|%d, %d) "%(x,y,sum_m)
    x=x/sum_m
    y=y/sum_m
    return (x,y)

def key_events():
    global RASTER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            if event.key == pygame.K_f:
                if(RASTER>100):
                    RASTER = RASTER - 100
                    if(RASTER<1):
                        RASTER=1
            if event.key == pygame.K_g:
                RASTER = RASTER + 100
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

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    clock = pygame.time.Clock()
    running=True
    
    m=list()
    print "create random objects"
    for i in range(250):
        x=randint(0, X_SCREEN*RASTER)
        y=randint(0, Y_SCREEN*RASTER)
        radius = randint(100,10000)
        #print "( %d | %d ) r: %d   xv: %d  yv: %d"%(int(x/RASTER),int(y/RASTER), radius, xv, yv)
        m.append(Mass(x,y, radius))
    while running:
        #clock.tick(60) # frame rate 60 ticks
        screen.fill((0, 0, 0))
        min_x, min_y = get_mass_point(m)
        textsurface = myfont.render('Raster: %d (%d|%d)'%(RASTER, min_x, min_y), False, (255, 255, 255))
        screen.blit(textsurface,(0,0))
        running = key_events()
        for m1 in m:
            m1.calc_speed(m)
            m1.calc_xy()
            m1.draw_me(screen, min_x, min_y)
        pygame.draw.line(screen, GREEN, [X_SCREEN/2-20, Y_SCREEN/2], [X_SCREEN/2+20, Y_SCREEN/2], 1)
        pygame.draw.line(screen, GREEN, [X_SCREEN/2, Y_SCREEN/2-20], [X_SCREEN/2, Y_SCREEN/2+20], 1)
        pygame.display.flip()


if __name__ == '__main__':
    main()