import pygame
import os
import sys
import random

# 게임 스크린 크기
sc_w = 900
sc_h = 700

# 색정의
white = (255, 255, 255)
sea = (80, 180, 220)
ground = (140, 120, 40)
dark_ground = (70, 60, 20)

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")

# 물고기 객체
class Fish():
    def __init__(self):
        self.image = pygame.image.load(os.path.join(assets_path, "fish.png"))
        self.sound = pygame.mixer.Sound(os.path.join(assets_path, "swim.wav"))

        self.rect = self.image.get_rect()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.reset()

    # 위치 초기화
    def reset(self):
        self.rect.x = 250
        self.rect.y = 250
        self.dx = 0
        self.dy = 0

    # 헤엄치기
    def swim(self):
        self.dy = -10
        self.sound.play()

    # 물고기 업데이트
    def update(self):
        self.dy += 0.5
        self.rect.y += self.dy
        # 물고기가 게임화면 위로 넘어갈때
        if self.rect.y <= 0:
            self.rect.y = 0
        # 물고기가 게임 화면 아래로 넘어 갈때
        if self.rect.y + self.height > sc_h:
            self.rect.y = sc_h - self.height
            self.dy = 0
        if self.dy > 20:
            self.dy = 20
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# 파이프 객체
class Pipe():
    def __init__(self):
        self.lpipe = pygame.image.load(os.path.join(assets_path, "pipe01.png"))
        self.lpipe_rect = self.lpipe.get_rect()
        self.lpipe_width = self.lpipe.get_rect().width
        self.lpipe_height = self.lpipe.get_rect().height

        spipes = ["pipe02.png", "pipe03.png", "pipe04.png", "pipe05.png", "pipe06.png"]

        self.spipe = pygame.image.load(os.path.join(assets_path, random.choice(spipes)))
        self.spipe_rect = self.spipe.get_rect()
        self.spipe_width = self.spipe.get_rect().width
        self.spipe_height = self.spipe.get_rect().height

        self.set_pos()

    def set_pos(self):
        self.random_pipe = random.randint(0, 1)
        if self.random_pipe == 1:
            self.lpipe_rect.x = sc_w
            self.lpipe_rect.y = -2
            self.spipe_rect.x = sc_w
            self.spipe_rect.y = sc_h - self.spipe_height + 2 
        else:
            self.spipe_rect.x = sc_w
            self.spipe_rect.y = -2
            self.lpipe_rect.x = sc_w
            self.lpipe_rect.y = sc_h - self.lpipe_height + 2

    def update(self):
        self.lpipe_rect.x -= 4
        self.spipe_rect.x -= 4

    def out_of_screen(self):
        if self.spipe_rect.x + self.spipe_width <= 0:
            return True
        return False
    
    def check_crash(self, fish):
        if self.lpipe_rect.colliderect(fish.rect):
            return True
        elif self.spipe_rect.colliderect(fish.rect):
            return True
        else:
            return False
    def draw(self, screen):
        screen.blit(self.lpipe, self.lpipe_rect)
        screen.blit(self.spipe, self.spipe_rect)

class Game():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(assets_path, "bgm.mp3"))
        self.font = pygame.font.SysFont("arial", 24, True, False)
        self.fish = Fish()
        self.pipes = []
        self.pipes.append(Pipe())
        self.pipe_pos = 0
        self.score = 0
        self.menu_on = True

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if self.menu_on:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.play(-1)
                        self.score = 0
                        self.menu_on = False
                        self.fish.reset()
                        self.pipes = []
                        self.pipes.append(Pipe())
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.fish.swim()
        return True

    def run_logic(self):
        if not self.menu_on:
            self.fish.update()

            for pipe in self.pipes:
                pipe.update()
                if pipe.spipe_rect.x == self.pipe_pos:
                    self.pipes.append(Pipe())
                    self.score += 1
                if pipe.out_of_screen():
                    del self.pipes[0]
                    self.pipe_pos = random.randrange(200, 400, 4)
                if pipe.check_crash(self.fish):
                    pygame.mixer.music.stop()
                    self.menu_on = True

    def draw_text(self, screen, text, font, x, y, main_color):
        text_obj = font.render(text, True, main_color)
        text_rect = text_obj.get_rect()
        text_rect.center = x, y
        screen.blit(text_obj, text_rect)

    def display_menu(self, screen):
        center_x = (sc_w // 2)
        center_y = (sc_h // 2)
        rect = (center_x -220, center_y -50, 440, 100)
        pygame.draw.rect(screen, ground, rect)
        pygame.draw.rect(screen, dark_ground, rect, 4)
        self.draw_text(screen, "Press Space Key To Play", self.font, center_x, center_y, dark_ground)

    def display_frame(self, screen):
        screen.fill(sea)
        pygame.draw.rect(screen, ground,(0, sc_h -50, sc_w, 50))
        pygame.draw.line(screen, dark_ground, (0, sc_h -50), (sc_w, sc_h -50), 4)
        self.fish.draw(screen)
        for pipe in self.pipes:
            pipe.draw(screen)
        self.draw_text(screen, "score:" + str(self.score), self.font, 100, 50, white)

def main():
    # 게임 설정
    pygame.init()
    screen = pygame.display.set_mode((sc_w, sc_h))
    pygame.display.set_caption("Fish Game")
    clock = pygame.time.Clock()

    game = Game()
    running = True
    while running:
        running = game.process_events()
        game.run_logic()
        if game.menu_on:    # 게임 메뉴 처리
            game.display_menu(screen)
        else:       # 게임 화면 처리
            game.display_frame(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
