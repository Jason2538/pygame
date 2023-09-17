import pygame
import os
import sys
import random
from time import sleep

# 게임 스크린 전역변수
sc_w = 480
sc_h = 800

# 색상 전역변수
black = (0, 0, 0)
white = (255,255,255)
gray = (150, 150,150)
red = (200, 0, 0)

# 게임 전역 변수 
car_c = 3
lane_c = 5
speed = 10

class Lane():
    def __init__(self):
        self.color = white
        self.w = 10
        self.h = 80
        self.gap = 20
        self.space= (sc_w - (self.w*lane_c)) / (lane_c -1)
        self.count = 10
        self.x = 0
        self.y = - self.h

    def move(self, speed, screen):
        self.y += speed
        if self.y > 0:
            self.y = -self.h
        self.draw(screen)
    def draw(self,screen):
        next_lane = self.y
        for i in range(self.count):
            pygame.draw.rect(screen, self.color, (self.x, next_lane, self.w, self.h))
            next_lane += self.h + self.gap


# 자동차 객체
class Car():
    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.x =x
        self.y =y
        self.dx = dx
        self.dy = dy

        c_i_p = resource_path('assets/car')
        i_f_l = os.listdir(c_i_p)
        self.i_f_l = [os.path.join(c_i_p, file)for file in i_f_l if file.endswith(".png")]


        cr_i_p = resource_path('assets/crash.png')
        cr_s_p = resource_path('assets/crash.wav')
        self.crash_sound = pygame.mixer.Sound(cr_s_p)
        coll_s_p = resource_path('assts/collision.wav')
        self.coll_s = pygame.mixer.Sound(coll_s_p)
        en_s_p = resource_path('assets/engine.wav')
        self.en_s_p = pygame.mixer.Sound(en_s_p)

    def load_image(self):
        c_c_p = random.choice(self.i_p_l)
        self.image = pygame.image.load(c_c_p)
        self.w = self.image.get_rect().width
        self.h = self.image.get_rect().height
    
    def load(self):
        self.load_image()
        self.x = int(sc_w / 2)
        self.y = sc_h - self.h
        self.dx = 0
        self.dy = 0
        self.en_s_p

    def load_random(self):
        self.load_image()
        self.x = random.randrange(0, sc_w - self.w)
        self.y = -self.h
        self.dx = 0
        self.dy = random.randint(1, 20)

    def move(self):
        self.x += self.dx
        self.y += self.dy
    
    def o_f_s(self):
        if self.x + self.w > sc_w or self.x < 0:
            self.x -= self.dx
        if self.y + self.h > sc_h or self.y < 0:
            self.y -= self.dy
    
    def check_crash(self, car):
        crash_sound_path = resource_path('assets/crash.wav')
        if (self.x + self.w > car.x) and (self.x < car.x + car.w) and (self.y < car.y + car.h) and (self.y + self.h > car.y):
            return True
        else:
            return False
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def draw_crash(self, screen):
        width = self.crash_image.get_rect().width
        height = self.crash_image.get_rect().height
        draw_x = self.x + int(self.width / 2) - int(width / 2)
        draw_y = self.y + int(self.height / 2) - int(height / 2)
        screen.blit(self.crash_image, [draw_x, draw_y])
        pygame.display.update()


class Game():
    def __init__(self):
            m_i_p = resource_path('assets\menu_car.png')
            self.image_intro = pygame.image.load(m_i_p)
            pygame.mixer.music.load(resource_path('assets/race.wav'))
            font_path = pygame.font.SysFont("Malgun Gothic", 40)
            front_path = pygame.font.SysFont("Malgun Gothic",30)


            self.lanes = []
            for i in range(lane_c):
                lane = Lane()
                lane.x = i * int(lane.space + lane.w)
                self.lanes.append(lane)  # Moved inside the loop

            self.cars = []
            for i in range(car_c):
                car = Car()
                car.load_random()  # You may want to load random image when initializing cars
                self.cars.append(car)  # Moved inside the loop

            self.player = Car()
            self.score = 0

            self.menu_on = True
    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            
            if self.menu_on:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.play(-1)
                        pygame.mouse.set_visible(False)
                        self.score = 0
                        self.menu_on = False
                        self.player.load()

                        for car in self.cars:
                            car.load_random()
                        sleep(4)

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.dy -= 5
                    elif event.key == pygame.K_DOWN:
                        self.player.dy += 5
                    elif event.key == pygame.K_LEFT:
                        self.player.dx -= 5
                    elif event.key == pygame.K_RIGHT:
                        self.player.dx += 5
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.player.dx = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.player.dy = 0

        return True
    def run_logic(self, screen):

        for car in self.cars:
            
            if car.y > sc_h:
                self.score += 10
                car.load_random()
            if self.player.check_crash(car):
                self.menu_on = True
                pygame.mixer.music.stop()
                self.player.crash_sound.play()
                self.player.draw_crash(screen)
                car.draw_crash(screen)
                sleep(1)
                pygame.mouse.set_visible(True)
            for com in self.cars:
                if car == com:
                    None
                elif car.check_crash(com):
                    self.score += 10
                    car.collision_sound.play()
                    car.draw_crash(screen)
                    car.load_random()
                    com.draw_crash(screen)
                    com.load_random()

    def draw_text(self, screen, text, font, x, y, main_color):
        text_obj = font.render(text, True, main_color)
        text_rect = text_obj.get_rect()
        text_rect.center = x, y
        screen.blit(text_obj, text_rect)

    def display_menu(self, screen):
        screen.fill(gray)
        screen.blit(self.image_intro, [40, 150])
        draw_x = int(sc_w / 2)
        draw_y = int(sc_h / 2)
        self.draw_text(screen, "레.이.싱.게.임.",
                       self.font, draw_x, draw_y + 50, black)
        self.draw_text(screen, "점수: " + str(self.score),
                       self.font, draw_x, draw_y + 150, white)
        self.draw_text(screen, "스페이스키를 눌러 실행하시오.",
                       self.front, draw_x, draw_y + 200, red)
        
    def display_frame(self, screen):
        screen.fill(gray) 
        for lane in self.lanes:
            lane.move(speed, screen)

        self.player.draw(screen)
        self.player.move()
        self.player.o_U_S()
        for car in self.cars:
            car.draw(screen)
            car.move()

        self.draw_text(screen, "Score: " + str(self.score),
                       self.font_30, 80, 20, black)

def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)


def main():
    pygame.init()
    pygame.display.set_caption("racing")
    screen = pygame.display.set_mode((sc_w, sc_h))
    clock = pygame.time.Clock()
    game = Game()

    running = True
    while running:
        running = game.process_events()
        if game.menu_on:
            game.display_menu(screen)
        else:
            game.run_logic(screen)
            game.display_frame(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()