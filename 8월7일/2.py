import random
import pygame

sc_w = 800
sc_h = 600

BLACK = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0,255,0)


pygame.init()

pygame.display.set_caption("pygame")

screen = pygame.display.set_mode((sc_w, sc_h))

clock = pygame.time.Clock()

color = BLACK

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                color = random.choice([blue, red, green])
                print("나의 이쁜이 윤아로")

    screen.fill(white)
    rect2 = pygame.Rect(0, 0, 100, 100)
    rect2.center = (sc_w //2, sc_h//2)
    pygame.draw.rect(screen, color, rect2, 0)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()