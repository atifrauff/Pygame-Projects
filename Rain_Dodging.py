import pygame
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 1000, 768

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain Dodging Game v1.2.0")

BG = pygame.transform.scale(pygame.image.load("Galaxy.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60

PLAYER_VEL = 15

FPS = 60


def draw(player):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, "white", player)

    pygame.display.update()


def main():
    run = True
    
    player = pygame.Rect(450, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    while run:

        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 520:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + PLAYER_HEIGHT - 10 <= HEIGHT:
            player.y += PLAYER_VEL


        draw(player)


if __name__ == "__main__":
    main()
