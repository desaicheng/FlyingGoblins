import pygame
import math
from character import character
from goblin import enemyGoblin
from projectile import projectile

pygame.init()
bg = pygame.image.load('images/bg.jpg')
gameOver = False
char = pygame.image.load('images/standing.png')
goblinImageLeft = pygame.image.load('images/L2E.png')
goblinImageRight = pygame.image.load('images/R2E.png')
facing = 1
lastgoblin = 0
goblinTimer = 5000
score = 0
charHeight = 64
windowWidth = 700
windowHeight = 450
charY = windowHeight - 80
projectileRadius = 10
projectileColor = (0,0,0)
lastShot = 0
win = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("Flying goblins")
clock = pygame.time.Clock()
projectiles = []
goblins = []
mainChar = character(50,charY,64,charHeight,6)
bgMusic = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
hitSound = pygame.mixer.Sound('hit.wav')
gameOverSound = pygame.mixer.Sound('gameOver.wav')

def redrawWindow():
    win.blit(bg,(0,0))
    for proj in projectiles:
        proj.draw(win)
    for goblin in goblins:
        goblin.draw(win)
    mainChar.draw(win)
    text = font.render('Score: ' + str(score), 1, (0,255,0))
    win.blit(text,(windowWidth - 130, 50))
    pygame.display.update()

font = pygame.font.SysFont('comicsans', 30, True)
finalFont = pygame.font.SysFont('comicsans', 60, True)
def addGoblin():
    goblins.append(enemyGoblin(windowWidth, charY, 64, 64, charHeight))
def updateGoblinTimer():
    goblinTimer = 5000
    if pygame.time.get_ticks() > 300000:
        goblinTimer = 200
    elif pygame.time.get_ticks() > 240000:
        goblinTimer = 1000
    elif pygame.time.get_ticks() > 180000:
        goblinTimer = 2000
    elif pygame.time.get_ticks() > 120000:
        goblinTimer = 3000
    return goblinTimer
def gameOverScreen():
    win.blit(bg, (0, 0))
    text = finalFont.render('Final Score: ' + str(score), 1, (0, 120, 135))
    win.blit(text, (windowWidth // 2 - 150, windowHeight // 2 - 50))
    pygame.display.update()
def shoot(mainChar):
    if mainChar.left:
        facing = -1
    else:
        facing = 1
    projectiles.append(projectile(round(mainChar.x + mainChar.width // 2), round(mainChar.y + mainChar.height // 2), projectileRadius, projectileColor, facing, mainChar.up, mainChar.standing))
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if gameOver:
        gameOverScreen()
        continue
    keys = pygame.key.get_pressed()

    if lastShot > 0:
        lastShot += 1
    if lastShot > 3:
        lastShot = 0

    if keys[pygame.K_UP]:
        mainChar.up = True
    else:
        mainChar.up = False

    if keys[pygame.K_LEFT]:
        mainChar.standing = False
        if mainChar.left:
            mainChar.x -= mainChar.vel
            mainChar.x = max(0,mainChar.x)
        mainChar.left = True
        mainChar.right = False
    elif keys[pygame.K_RIGHT]:
        mainChar.standing = False
        if mainChar.right:
            mainChar.x += mainChar.vel
            mainChar.x = min(mainChar.x,windowWidth-mainChar.width)
        mainChar.right = True
        mainChar.left = False
    else:
        mainChar.standing = True
        walkCount = 0

    if not mainChar.isJump:
        if keys[pygame.K_z]:
            mainChar.isJump = True
    else:
        if mainChar.jumpCount == 0:
            mainChar.jumpCount -= 1
        elif mainChar.jumpCount >= -10:
            mainChar.y -= (mainChar.jumpCount ** 2) / 3 * mainChar.jumpCount/abs(mainChar.jumpCount)
            mainChar.jumpCount -= 1
        else:
            mainChar.isJump = False
            mainChar.jumpCount = 10

    if pygame.time.get_ticks() - lastgoblin >= goblinTimer:
        lastgoblin = pygame.time.get_ticks()
        addGoblin()
    goblinTimer = updateGoblinTimer()

    for proj in projectiles:
        for goblin in goblins:
            if math.sqrt(((proj.x - (goblin.x + goblin.hitBox[2]/2))**2 + (proj.y - (goblin.y + goblin.hitBox[3]/2))**2)) < proj.radius + math.sqrt((goblin.hitBox[2]/2)**2 + (goblin.hitBox[3]/2)**2):
                projectiles.pop(projectiles.index(proj))
                goblins.pop(goblins.index(goblin))
                hitSound.play()
                score += 1
        if proj.x < windowWidth and proj.x > 0 and proj.y > 0:
            proj.update()
        else:
            projectiles.pop(projectiles.index(proj))

    for goblin in goblins:
        if goblin.hitBox[1] + goblin.hitBox[3] >= mainChar.hitBox[1] and (
        not goblin.hitBox[0] + goblin.hitBox[2] < mainChar.hitBox[0]) and (
        not goblin.hitBox[0] > mainChar.hitBox[0] + mainChar.hitBox[2]):
            gameOver = True
            pygame.mixer.music.stop()
            gameOverSound.play()
            pygame.time.delay(3000)
            break
        if goblin.y < goblin.floor + goblin.charHeight - goblin.goblinHeight:
            goblin.update()
        else:
            goblins.pop(goblins.index(goblin))

    redrawWindow()

    if keys[pygame.K_SPACE] and lastShot == 0:
        if len(projectiles) < 20:
            lastShot = 1
            shoot(mainChar)

pygame.quit()