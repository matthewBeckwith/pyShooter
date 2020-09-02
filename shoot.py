import random, pygame
from pygame.locals import *

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface([20,15])
        self.image.fill(color)

        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([20,20])
        self.image.fill(green)

        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([4,10])
        self.image.fill(blue)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 3
pygame.init()

screenWidth = 700
screenHeight = 400
screen = pygame.display.set_mode([screenWidth,screenHeight])

allSpritesList = pygame.sprite.Group()
enemiesList = pygame.sprite.Group()
bulletList = pygame.sprite.Group()

for i in range(10):
    e = Enemy(red)

    e.rect.x = random.randrange(screenWidth)
    e.rect.y = random.randrange(200)

    enemiesList.add(e)
    allSpritesList.add(e)

p = Player()
allSpritesList.add(p)

done = False

clock = pygame.time.Clock()

score = 0
p.rect.y = 370

myFont = pygame.font.SysFont("calibri", 15)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            b = Bullet()
            b.rect.x = p.rect.x + 5
            b.rect.y = p.rect.y

            allSpritesList.add(b)
            bulletList.add(b)
        
    allSpritesList.update()

    for b in bulletList:
        enemyHitList = pygame.sprite.spritecollide(b, enemiesList,True)

        for e in enemyHitList:
            bulletList.remove(b)
            allSpritesList.remove(b)
            score += 1
            print(score)

        if b.rect.y < -10:
            bulletList.remove(b)
            allSpritesList.remove(b)

    text = myFont.render("Score: " + str(score), 1, white)

    screen.fill(black)
    allSpritesList.draw(screen)
    screen.blit(text, (10,10))
    pygame.display.update()

    clock.tick(60)
        
pygame.quit()
