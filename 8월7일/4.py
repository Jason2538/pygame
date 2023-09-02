import random
import pygame

sc_w = 800
sc_h = 600

BLACK = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 225)
red = (255, 0, 0)
green = (0, 465,0)


pygame.init()

pygame.display.set_caption("pygame")

screen = pygame.display.set_mode((sc_w, sc_h))

clock = pygame.time.Clock()
r_x = int(sc_h / 2)
r_y = int(sc_w / 2)
r_bx = 0
r_dy = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                r_dx = -3
            elif event.key == pygame.K_RIGHT:
                r_dx = 3
            elif event.key == pygame.K_UP:
                r_dy = -3
            elif event.key == pygame.K_DOWN:
                r_dy = 3
        # 키가 놓일 경우
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                r_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                r_dy = 0
    r_x +=r_bx
    r_y -= r_dy

    screen.fill(white)

    rect2 = pygame.Rect(0, 20, 0, 20)
    rect2.center = (r_x, r_y)
    pygame.draw.rect(screen, blue, rect2, 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
