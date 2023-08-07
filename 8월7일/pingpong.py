import pygame
import os
import sys
import random

# 게임스크린 크기
sc_w = 480
sc_h = 640

# 색정의
white = (255, 255, 255)
black = (0, 0, 0)
blue = (20, 60, 120)
orange = (25, 170, 70)
red = (250, 0, 0)

current_path = os.path.dirname(__name__)
assets_path = os.path.join(current_path, "assets")

# 공 객체
class Ball(object):
    def __init__(self, bounce_sound):
        self.rect = pygame.Rect(int(sc_w / 2), int(sc_h / 2), 12, 12)
        self.bounce_sound = bounce_sound
        self.dx = 0
        self.dy = 5

    # 공 업데이트
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # 공이 게임 화면 왼쪽으로 넘어갈 때
        if self.rect.left < 0:
            self.dx *= -1
            self.rect.left = 0
            self.bounce_sound.play()
        # 공이 게임 화면 오른쪽으로 넘어갈 때
        elif self.rect.right > sc_h:
            self.dx *= -1
            self.rect.right = sc_w
            self.bounce_sound.play()

    # 공 리세
    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.dx = random.randint(-3, 3)
        self.dy = 5

    # 공 그리기
    def draw(self, screen):
        pygame.draw.rect(screen, orange, self.rect)


# 플레이어 객체
class Player(object):
    def __init__(self, ping_sound):
        self.rect = pygame.Rect(int(sc_w / 2), sc_h - 40, 50, 15)
        self.ping_sound = ping_sound
        self.dx = 0

    # 업데이트
    def update(self, ball):
        if self.rect.left <= 0 and self.dx < 0:
            self.dx = 0
        elif self.rect.right >= sc_w and self.dx > 0:
            self.dx = 0
        # 플레이어가 공이랑 충돌한 경우
        if self.rect.colliderect(ball.rect):
            ball.dx = random.randint(-5, 5)
            ball.dy *= -1
            ball.rect.bottom = self.rect.top
            self.ping_sound.play()

        self.rect.x += self.dx

    # 그리기
    def draw(self, screen):
        pygame.draw.rect(screen, red, self.rect)


# 적 객체
class Enemy(object):
    def __init__(self, pong_sound):
        self.rect = pygame.Rect(int(sc_w / 2), 25, 50, 15)
        self.pong_sound = pong_sound

    # 업데이트
    def update(self, ball):
        # 적보다 공이 왼쪽에 있을 때
        if self.rect.centerx > ball.rect.centerx:
            diff = self.rect.centerx - ball.rect.centerx
            if diff <= 4:
                self.rect.centerx = ball.rect.centerx
            else:
                self.rect.x -= 4
        # 적보다 공이 오른쪽에 있을 때
        elif self.rect.centerx < ball.rect.centerx:
            diff = ball.rect.centerx - self.rect.centerx
            if diff <= 4:
                self.rect.centerx = ball.rect.centerx
            else:
                self.rect.x += 4
        # 적이 공과 충돌한 경우
        if self.rect.colliderect(ball.rect):
            ball.dy *= -1
            ball.rect.top = self.rect.bottom
            self.pong_sound.play()

    # 그리기
    def draw(self, screen):
        pygame.draw.rect(screen, black, self.rect)


# 게임 객체
class Game(object):
    def __init__(self):
        bounce_sound = pygame.mixer.Sound(os.path.join(assets_path, "bounce.wav"))
        ping_sound = pygame.mixer.Sound(os.path.join(assets_path, "ping.wav"))
        pong_sound = pygame.mixer.Sound(os.path.join(assets_path, "pong.wav"))
        self.font = pygame.font.SysFont("맑은 고딕", 50, False, False)
        self.ball = Ball(bounce_sound)
        self.player = Player(ping_sound)
        self.enemy = Enemy(pong_sound)
        self.player_score = 0
        self.enemy_score = 0

    # 게임 이벤트 처리 및 조작
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.dx -= 5
                elif event.key == pygame.K_RIGHT:
                    self.player.dx += 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.dx = 0

        return False

    # 게임 로직 수행
    def run_logic(self):
        self.ball.update()
        self.player.update(self.ball)
        self.enemy.update(self.ball)

        # 공이 게임 화면 위로 넘어간 경우 (플레이어가 이긴 경우)
        if self.ball.rect.y < 0:
            self.player_score += 1
            self.ball.reset(self.player.rect.centerx, self.player.rect.centery)
        # 공이 게임 화면 아래로 넘어간 경우 (적이 이긴 경우)
        elif self.ball.rect.y > sc_h:
            self.enemy_score += 1
            self.ball.reset(self.enemy.rect.centerx, self.enemy.rect.centery)

    # 메시지 출력
    def display_message(self, screen, message, color):
        label = self.font.render(message, True, color)
        width = label.get_width()
        height = label.get_height()
        pos_x = int((sc_w / 2) - (width / 2))
        pos_y = int((sc_h / 2) - (height / 2))
        screen.blit(label, (pos_x, pos_y))
        pygame.display.update()

    # 게임 프레임 출력
    def display_frame(self, screen):
        screen.fill(blue)

        # 플레이어 점수가 10점일 경우
        if self.player_score == 10:
            self.display_message(screen, "승리!", white)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)
        # 적 점수가 10점일 경우
        elif self.enemy_score == 10:
            self.display_message(screen, "패배!", white)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)
        else:
            self.ball.draw(screen)
            self.player.draw(screen)
            self.enemy.draw(screen)
            # 게임 중앙 점선
            for x in range(0, sc_w, 24):
                pygame.draw.rect(screen, white, [x, sc_h // 2, 10, 10])
            # 적 점수 표시
            enemy_score_label = self.font.render(str(self.enemy_score), True, white)
            screen.blit(enemy_score_label, (10, 260))
            # 플레이어 점수 표시
            player_score_label = self.font.render(str(self.player_score), True, white)
            screen.blit(player_score_label, (10, 340))


# 게임 리소스 경로
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():
    pygame.init()
    screen = pygame.display.set_mode((sc_w, sc_h))
    pygame.display.set_caption("PingPong Game")
    clock = pygame.time.Clock()
    game = Game()

    running = True
    while not running:
        running = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
