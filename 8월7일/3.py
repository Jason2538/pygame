
import pygame

sc_w = 800
sc_h = 600

BLACK = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)


pygame.init()

pygame.display.set_caption("pygame")

screen = pygame.display.set_mode((sc_w, sc_h))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    pygame.draw.rect(screen, BLACK, [50,  50, 100, 100],0)
    pygame.draw.rect(screen, blue, [sc_w // 2 -25, sc_h // 2 -25, 50, 50],0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()