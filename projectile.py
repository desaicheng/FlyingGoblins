import math
import pygame
class projectile():
    def __init__(self,x,y,radius,color,facing,up,standing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.standing = standing
        self.vel = 8 * facing
        self.up = up
    def draw(self,win):
        pygame.draw.circle(win,self.color, (self.x, self.y), self.radius)
    def update(self):
        if self.up == False:
            self.x +=  self.vel
        elif self.up == True and self.standing == True:
            self.y -= abs(self.vel)
        else:
            self.x += math.floor(self.vel / math.sqrt(2))
            self.y -= math.floor(self.vel * self.facing/math.sqrt(2))