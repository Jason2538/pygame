import pygame
import os


sc_w = 800
sc_h = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BASE = (153, 102, 0)
BACKGROUND = (153, 153, 153)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
GREEN = (50, 200, 50)

pygame.init()
pygame.display.set_caption("Tower_of_Hanoi")
screen = pygame.display.set_mode((sc_w, sc_h))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
effect_image = pygame.image.load(os.path.join(assets_path, 'click_effect.png'))

step = 0
choise = 0
change = 0
s1 = []
s2 = []
s3 = []
count = 0

class Ring():
    def __init__(self):
        pass
    def create(self, screen, n, x, y, color):
        pygame.draw.rect(screen, color, [(250 * n) - 250 + (14 * x), 500 - (30 * y), 300 - (28 * x), 30], 0)
    def draw(self, list, screen, n):
        s = 1
        for i in list:
            Ring().create(screen, n, 10 - i, s, RED)
            s += 1

def change_ring(l1, l2, l3, n1, n2, n3):
        global step
        global choise
        global change
        global count
        if step == 0:
            if len(l1) != 0:
                choise = n1
                change = 0
                step = 1
        else:
            if choise == n2:
                if len(l1) == 0:
                    change = n1
                    l1.insert(len(l1), l2[-1])
                    del(l2[-1])
                    count += 1
                elif l2[-1] < l1[-1]:
                    change = n1
                    l1.insert(len(l1), l2[-1])
                    del(l2[-1])
                    count += 1
            if choise == n3:
                if len(l1) == 0:
                    change = n1
                    l1.insert(len(l1), l3[-1])
                    del(l3[-1])
                    count += 1
                elif l3[-1] < l1[-1]:
                    change = n1
                    l1.insert(len(l1), l3[-1])
                    del(l3[-1])
                    count += 1
            step = 0
        
        return(l1, l2, l3)

time = 0
time_m = 0
end = 0
r = True
running = True

def game(s1, s2, s3, m):
    global step
    global choise
    global change
    global count
    global time
    global end
    global time_m
    effect = 0
    count = 0
    choise = 0
    change = 0
    global running
    global r
    r = False
    running = True
    
    while running:
        time = (pygame.time.get_ticks()) // 1000 - time_m
        if end == 0:
            screen.fill(BACKGROUND)
            ring = Ring()
            pygame.draw.rect(screen, BASE, [0, 500, 800, 600], 0)
            pygame.draw.rect(screen, BASE, [138, 200, 24, 300], 0)
            pygame.draw.rect(screen, BASE, [388, 200, 24, 300], 0)
            pygame.draw.rect(screen, BASE, [638, 200, 24, 300], 0)
            ring.draw(s1, screen, 1)
            ring.draw(s2, screen, 2)
            ring.draw(s3, screen, 3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    r = False
                    running = False
                    
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x = pygame.mouse.get_pos()[0]
                    effect_image.get_rect()
                    size = effect_image.get_width() // 2
                    screen.blit(effect_image, (pygame.mouse.get_pos()[0] - size, pygame.mouse.get_pos()[1] - size))
                    effect = 1
                    if mouse_x <= 270:
                        s1, s2, s3 = change_ring(s1, s2, s3, 1, 2, 3)
                    elif mouse_x <= 530:
                        s2, s1, s3 = change_ring(s2, s1, s3, 2, 1, 3)
                    else:
                        s3, s1, s2 = change_ring(s3, s1, s2, 3, 1, 2)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()

            if effect == 1:
                effect_image.get_rect()
                size = effect_image.get_width() // 2
                screen.blit(effect_image, (pygame.mouse.get_pos()[0] - size, pygame.mouse.get_pos()[1] - size))
                effect = 0
            s_c = list(range(1, m))
            s_c.reverse()
            if s3 == s_c:   
                end = 1

            font = pygame.font.Font(None, 36)  
            timer_text = "Time: " + str(time) + "s"
            timer_surface = font.render(timer_text, True, (0, 0, 0))
            screen.blit(timer_surface, (10 ,10))

            count_text = "Count: " + str(count)    
            count_surface = font.render(count_text, True, (0, 0, 0))
            screen.blit(count_surface, (150, 10))
    
            min_text = "Min: " + str(2 ** (m - 1) - 1)
            min_surface = font.render(min_text, True, (0, 0, 0))
            screen.blit(min_surface, (300, 10))

            change_text = str(choise) + " => " + str(change)
            change_surface = font.render(change_text, True, (0, 0, 0))
            screen.blit(change_surface, (420, 10)) 

        else:
            screen.fill(BACKGROUND)
            font = pygame.font.Font(None, 72)
            surface = font.render("GAME OVER!", True, (0, 0, 0))
            screen.blit(surface, (250 ,200))
            surface = font.render("YOU WIN!", True, (0, 0, 0))  
            screen.blit(surface, (280 ,260))
            font = pygame.font.Font(None, 36)
            surface = font.render("Time: " + str(time) + "s", True, (0, 0, 0)) 
            screen.blit(surface, (330 ,330))
            surface = font.render("Count: " + str(count), True, (0, 0, 0))
            screen.blit(surface, (330 ,370))
            surface = font.render("Min: " + str(2 ** (m - 1) - 1), True, (0, 0, 0))
            screen.blit(surface, (330 ,410))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

def main():
    global r
    global running
    global time
    global time_m
    r = True
    running = False
    m = 6
    while True:
        if r:
            time = (pygame.time.get_ticks()) // 1000
            screen.fill(BACKGROUND)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    r = False
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        m = 4
                    elif event.key == pygame.K_4:
                        m = 5
                    elif event.key == pygame.K_5:
                        m = 6
                    elif event.key == pygame.K_6:
                        m = 7
                    elif event.key == pygame.K_7:
                        m = 8
                    elif event.key == pygame.K_8:
                        m = 9
                    elif event.key == pygame.K_9:
                        m = 10
                    elif event.key == pygame.K_SPACE:
                        time_m = time
                        game(s1, s2, s3, m)
                        

            s1 = list(range(1, m))
            s1.reverse()
            s2 = []
            s3 = []       
            pygame.display.flip()
            clock.tick(60)
        else:
            break
    pygame.quit()
            
main()