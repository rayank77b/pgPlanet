#!/usr/bin/python
import pygame

X_SCREEN=800
Y_SCREEN=600

class Mass:
    def __init__(self,x,y,d,xd,yd,xv,yv):
        self.x=x
        self.y=y
        self.d=d  # durchmesser
        self.direction_x=xd
        self.direction_y=yd
        self.speed_x=xv
        self.speed_y=yv

    def calc(self):
        if(self.direction_x==1):
            if(self.x>(X_SCREEN-self.d)):
                self.direction_x=-1
        if(self.direction_x==-1):
            if(self.x<0):
                self.direction_x=1
        if(self.direction_y==1):
            if(self.y>(Y_SCREEN-self.d)):
                self.direction_y=-1
        if(self.direction_y==-1):
            if(self.y<0):
                self.direction_y=1
        self.x = self.x + self.direction_x*self.speed_x
        self.y = self.y + self.direction_y*self.speed_y
    
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

def main():
    pygame.init()
    screen = pygame.display.set_mode((X_SCREEN, Y_SCREEN))
    
    pygame.display.set_caption("pgPlanet Version 0.01")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    clock = pygame.time.Clock()
    running=True
    clock.tick(30) # frame rate 30 ticks
    m1=Mass(300,400,10,1,1,0.5,0.3)
    while running:
        screen.fill((0, 0, 0))
        running = key_events()
        m1.calc()
        m1.draw_me(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()