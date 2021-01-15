import random

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Untitled RPG")


class player:
    def __init__(self):
        self.playerImg = pygame.image.load('assets/sprites/cell1.png')
        self.playerX = 400
        self.playerY = 300
        self.playerRect = pygame.rect.Rect(self.playerX, self.playerY, 32, 32)
        self.playerSpeed = 1

    def movement(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            self.playerRect.move_ip(-self.playerSpeed, 0)
        if pressed_key[pygame.K_RIGHT]:
            self.playerRect.move_ip(self.playerSpeed, 0)
        if pressed_key[pygame.K_UP]:
            self.playerRect.move_ip(0, -self.playerSpeed)
        if pressed_key[pygame.K_DOWN]:
            self.playerRect.move_ip(0, self.playerSpeed)

    def draw(self, surface):
        screen.blit(self.playerImg, self.playerRect)

    def checkBounds(self):
        if self.playerRect.x <= 0:
            self.playerRect.x = 0
        elif self.playerRect.x >= 736:
            self.playerRect.x = 736

        if self.playerRect.y <= 0:
            self.playerRect.y = 0
        elif self.playerRect.y >= 535:
            self.playerRect.y = 535

    def collision(self, sprite):
        return self.playerRect.colliderect(sprite.rect)

class enemy:
    def __init__(self):
        self.enemyHealth = round (random.random(), 2)
        self.enemyX = random.randrange(0, 800)
        self.enemyY = random.randrange(0, 600)
        self.enemyImg = pygame.image.load('assets/sprites/enemyCell.png')
        self.rect = pygame.rect.Rect(self.enemyX, self.enemyY, 32, 32)


    def spawn(self):
        screen.blit(self.enemyImg, self.rect)


#Player
mainPlayer = player()
clock = pygame.time.Clock()

#Enemy
badCell = enemy()
screen.fill((0, 0, 255))
badCell.spawn()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255))
    clock.tick(60)
    mainPlayer.draw(screen)
    mainPlayer.movement()

    mainPlayer.checkBounds()
    pygame.display.update()
