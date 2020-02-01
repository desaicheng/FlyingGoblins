import pygame
import random
goblinImageLeft = pygame.image.load('images/L2E.png')
goblinImageRight = pygame.image.load('images/R2E.png')
class enemyGoblin():
    def __init__(self,winWidth, charY, goblinWidth, goblinHeight, charHeight):
        self.winWidth = winWidth
        self.floor = charY
        self.charHeight = charHeight
        self.goblinWidth = goblinWidth
        self.goblinHeight = goblinHeight
        self.x = random.uniform(0,self.winWidth - self.goblinWidth)
        self.y = 0
        self.slope = (random.uniform(0,self.winWidth - self.goblinWidth) - self.x)/(self.floor + self.charHeight - self.goblinHeight)
        self.left = False
        if self.slope < 0:
            self.left = True
        self.hitBox = (self.x + 22, self.y + 8, 30, 60)
    def update(self):
        self.x += self.slope * 8
        self.y += 8
        self.hitBox = (self.x + 22, self.y + 8, 30, 60)
    def draw(self,win):
        if self.left == True:
            win.blit(goblinImageLeft, (self.x, self.y))
        else:
            win.blit(goblinImageRight, (self.x, self.y))
