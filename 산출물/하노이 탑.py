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
        pygame.draw.rect(screen, color, [(250 * n) - 230 + (20 * x), 500 - (30 * y), 260 - (40 * x), 30], 0)
    def draw(self, list, screen, n):
        s = 1
        for i in list:
            Ring().create(screen, n, i, s, RED)
            s += 1

def change_ring(l1, l2, l3, n1, n2, n3): #(자기 자신, 2번째 꺼, 3번쨰 꺼)
        global step
        global choise
        global change
        global count
        if step == 0:
            if len(l1) != 0:
                choise = n1
                step = 1
        else:
            change = n1
            if choise == n2:
                if len(l1) == 0:
                    l1.insert(len(l1), l2[-1])
                    del(l2[-1])
                elif l2[-1] > l1[-1]:
                    l1.insert(len(l1), l2[-1])
                    del(l2[-1])
            if choise == n3:
                if len(l1) == 0:
                    l1.insert(len(l1), l3[-1])
                    del(l3[-1])
                elif l3[-1] > l1[-1]:
                    l1.insert(len(l1), l3[-1])
                    del(l3[-1])
            step = 0
            count += 1
        return(l1, l2, l3)



def main():
    pygame.init()
    pygame.display.set_caption("Tower_of_Hanoi")
    screen = pygame.display.set_mode((sc_w, sc_h))
    clock = pygame.time.Clock()
    s1 = list(range(1, 6))
    s2 = []
    s3 = []
    global step
    global choise
    global change
    global count
    running = True
    while running:
        ring = Ring()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x = pygame.mouse.get_pos()[0]
                if mouse_x <= 270:
                    s1, s2, s3 = change_ring(s1, s2, s3, 1, 2, 3)
                elif mouse_x <= 530:
                    s2, s1, s3 = change_ring(s2, s1, s3, 2, 1, 3)
                else:
                    s3, s1, s2 = change_ring(s3, s1, s2, 3, 1, 2)
        if s3 == [1, 2, 3, 4, 5]:
            print("clear")
            print("Time: " + str(time) + "s")
            print("Count: " + str(count))
            pygame.quit()

        time = (pygame.time.get_ticks()) // 1000

        screen.fill(BACKGROUND)

        font = pygame.font.Font(None, 36)  
        timer_text = "Time: " + str(time) + "s"
        timer_surface = font.render(timer_text, True, (0, 0, 0))     
        screen.blit(timer_surface, (10 ,10))

        count_text = "Count: " + str(count)    
        count_surface = font.render(count_text, True, (0, 0, 0))     
        screen.blit(count_surface, (150, 10))
 
        min_text = "Min: " + str(2 ** 5 - 1)
        min_surface = font.render(min_text, True, (0, 0, 0))     
        screen.blit(min_surface, (300, 10))

        change_text = str(choise) + " => " + str(change)
        change_surface = font.render(change_text, True, (0, 0, 0))     
        screen.blit(change_surface, (420, 10)) 
        

        pygame.draw.rect(screen, BASE, [0, 500, 800, 600], 0)
        pygame.draw.rect(screen, BASE, [138, 240, 24, 300], 0)
        pygame.draw.rect(screen, BASE, [388, 240, 24, 300], 0)
        pygame.draw.rect(screen, BASE, [638, 240, 24, 300], 0)
        ring.draw(s1, screen, 1)
        ring.draw(s2, screen, 2)
        ring.draw(s3, screen, 3)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()