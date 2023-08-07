
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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    pygame.draw.rect(screen, BLACK, [50,  50, 100, 100],0)
    rect2 = pygame.Rect(0, 0, 50, 50)
    rect2.center = (sc_w //2, sc_h//2)
    pygame.draw.rect(screen, blue, rect2, 0)
    rect4 = pygame.Rect(200,200,40,40)
    # rect4.center = (sc_w //2, sc_h//2)
    pygame.draw.rect(screen, green, rect4, 0)
    rect3 = pygame.Rect(200, 200, 20, 20)
    pygame.draw.rect(screen, red, rect3 , 0)
    print(rect3.center)
    # rect5 = pygame.Rect(180,180,60,60)
    # rect5.center = (sc_w//2,sc_h//2)
    # pygame.draw.rect(screen, red,)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()