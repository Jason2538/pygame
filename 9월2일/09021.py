import pygame
import random

sc_h = 600
sc_w = 600

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("qhrtmq")
screen = pygame.display.set_mode((sc_w, sc_h))
clock = pygame.time.Clock()

x = sc_w //2
y = sc_h // 2
dx = random.randint(1, 10)
dy = random.randint(1, 10)
running = True

while running:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.draw.circle(screen, black, [sc_h // 2, sc_w // 2],30 ,0)
    x += dx
    y += dy
    if x>sc_w or x<0:
        dx *= -1
    if y>sc_h or y<0:
    # screen.blit(ball, [sc_w // 2, sc_h // 2])





pygame.display.flip()
clock.tick(120)
pygame.quit()
