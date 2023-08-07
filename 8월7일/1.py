import pygame

w_w = 800
W_H = 600

white = (255, 255, 255)

pygame.init()

pygame.display.set_caption("pygame")

screen = pygame.display.set_mode((w_w, W_H))
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done = True
    screen.fill(white)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()