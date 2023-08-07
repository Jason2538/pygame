import pygame
import os
import sys
import random
from time import sleep

# 게임 스크린 전역 변수
sc_w = 800
sc_h = 600

# 게임 화면 전역 변수
gr_s = 20
gr_w = sc_w / gr_s
gr_h = sc_h / gr_s  

# 방향 전역 변수
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

# 색상 전역 변수
white = (255, 255, 255)
orange = (250, 150, 0)
gray = (100, 100, 100)

# 뱀 객체
class Snake():
    def __init__(self):
        self.create()

    # 뱀 생성
    def create(self):
        self.length = 2 
        self.positions = [(int(sc_w / 2), int(sc_h / 2))]
        self.direction = random.choice([up, down, left, right])
    
    # 뱀 방향 조정
    def control(self, xy):
        if (xy[0] * -1, xy[1] * -1 )== self.direction:
            return
        else:
            self.direction =xy
    # 뱀 이동
    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (cur[0] + (x * gr_s)), (cur[1] + (y * gr_s))

        # 뱀이 자기 몸통에 닿았을 경우 뱀 처음 부터 다시 생성
        if new in self.positions[2:]:
            sleep(1)
            self.create()
        # 뱀이 게임 회면을 넘어갈 경우 뱁 처음부터 다시 생성
        elif new[0] < 0 or new[0] >= sc_w or \
        new [1] < 0 or new[1]>= sc_h:
            sleep(1)
            self.create()
        # 뱀이 정상적으로 이동하는 경우
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    # 뱀이 먹이를 먹을 때 호출
    def eat(self):
        self.length += 1

    # 뱀 그리기
    def draw(self, screen):
        red, green ,blue = 50 / (self.length - 1), 150, 150 / (self.length - 1)
        for i, p in enumerate(self.positions):
            color = (100 + red * i, green, blue * i)
            rect = pygame.Rect((p[0], p[1]), (gr_s, gr_s))
            pygame.draw.rect(screen, color, rect)

        # 먹이 객체
class Feed():
    def __init__(self):
        self.position = (0, 0)
        self.color = orange
        self.create()

    # 먹이 생성
    def create(self):
        x = random.randint(0, gr_w -1)
        y = random.randint(0, gr_h -1)
        self.position = x * gr_s, y * gr_s

    # 먹이 그리기
    def draw(self, screen):
        rect = pygame.Rect((self.position[0], self.position[1]), (gr_s, gr_s))
        pygame.draw.rect(screen, self.color, rect)

# 게임 객체
class Game():
    def __init__(self):
        self.snake = Snake()
        self.feed = Feed()
        self.speed = 20

    # 게임 이벤트 처리 및 조작
    def process_events(self):               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.control(up)
                elif event.key == pygame.K_DOWN:
                    self.snake.control(down)
                elif event.key == pygame.K_LEFT:
                    self.snake.control(left)
                elif event.key == pygame.K_RIGHT:
                    self.snake.control(right)
        return False

    # 게임 로직 수행
    def run_logic(self):
        self.snake.move()
        self.check_eat(self.snake, self.feed)
        self.speed = (20 + self.snake.length) / 8

    # 뱀이 먹이를 먹었는지 체크
    def check_eat(self, snake, feed):
        if snake.positions[0] == feed.position:
            snake.eat()
            feed.create()


    # 게임 정보 출력
    def draw_info(self, length, speed, screen):
        info = "Length: " + str(length) + " " + "Speed: " + str(round(speed, 2))
        font = pygame.font.SysFont('FixedSys', 30, False, False)
        text_obj = font.render(info, True, gray)
        text_rect= text_obj.get_rect()
        text_rect.x, text_rect.y = 10, 10
        screen.blit(text_obj, text_rect)

    # 게임 프레임 처리
    def display_frame(self, screen):
        screen.fill(white)
        self.draw_info(self.snake.length, self.speed, screen)
        self.snake.draw(screen)
        self.feed.draw(screen)
        screen.blit(screen, (0, 0))

def main():
    # 게임 초기화 및 환경 설정
    pygame.init()
    pygame.display.set_caption('Snake Game')
    screen = pygame.display.set_mode((sc_w, sc_h))
    clock = pygame.time.Clock()
    game = Game()

    done = False
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(game.speed)

    pygame.quit()

if __name__ == '__main__':
    main()