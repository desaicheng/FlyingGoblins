import pygame
walkRight = [pygame.image.load('images/R1.png'),pygame.image.load('images/R2.png'),
pygame.image.load('images/R3.png'),pygame.image.load('images/R4.png'),pygame.image.load('images/R5.png'),pygame.image.load('images/R6.png'),
pygame.image.load('images/R7.png'),pygame.image.load('images/R8.png'),pygame.image.load('images/R9.png')]
walkLeft = [pygame.image.load('images/L1.png'),pygame.image.load('images/L2.png'),
pygame.image.load('images/L3.png'),pygame.image.load('images/L4.png'),pygame.image.load('images/L5.png'),pygame.image.load('images/L6.png'),
pygame.image.load('images/L7.png'),pygame.image.load('images/L8.png'),pygame.image.load('images/L9.png')]
class character():
    def __init__(self, x, y, width, height,vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.up = False
        self.walkCount = 0
        self.standing = True
        self.hitBox = (self.x+17, self.y+22,28,50)
    def draw(self,win):
        self.hitBox = (self.x + 17, self.y + 22, 28, 50)
        if self.walkCount == 26:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))