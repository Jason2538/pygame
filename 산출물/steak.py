import pygame
import random
import os

# 게임 화면 크기 설정
WIDTH = 800
HEIGHT = 600

# 색상 정의 (RGB)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Steak Game")

clock = pygame.time.Clock()

class Steak(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(assets_path, "steak4 (1) (1).png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(100, WIDTH - 100)
        self.rect.centery = random.randint(100, HEIGHT - 100)

    def update(self):
        pass

# 플레이어 클래스 정의
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(assets_path, "people.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(300, WIDTH - 100)
        self.rect.centery = random.randint(300, HEIGHT - 100)

    def update(self):
        # 키보드 입력 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player.rect.x > 0:
                player.rect.x -= 15

        if keys[pygame.K_RIGHT]:
            if player.rect.x < WIDTH - 50:
                player.rect.x += 15

        if keys[pygame.K_UP]:
            if player.rect.y > 0:
                player.rect.y -= 15

        if keys[pygame.K_DOWN]:
            if player.rect.y < HEIGHT - 50:
                player.rect.y += 15

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()

# 초기 스테이크 갯수
steak_count = 10

# 스테이크 객체 생성 및 그룹에 추가
for _ in range(steak_count):
    steak = Steak()
    all_sprites.add(steak)

player = Player()  # 플레이어 객체 생성
player_sprite.add(player)  # 플레이어 객체를 그룹에 추가

start_time = pygame.time.get_ticks()  # 게임 시작 시간
end_time = None  # 게임 종료 시간 초기화
success_count = 0

running = True

# 게임 루프
while running:
    clock.tick(60)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 종료 조건: 스테이크 갯수가 100개에 도달하면 종료
    if success_count >= 100:
        running = False
        end_time = pygame.time.get_ticks()  # 게임 종료 시간 기록
        elapsed_time = (end_time - start_time) // 1000  # ms를 초로 변환

    screen.fill(WHITE)

    all_sprites.update()
    player_sprite.update()
    all_sprites.draw(screen)
    player_sprite.draw(screen)

    # 충돌 감지
    collisions = pygame.sprite.spritecollide(player, all_sprites, True)
    for collision in collisions:
        success_count += 1

        steak = Steak()
        all_sprites.add(steak)

    # 현재 스코어 출력
    font = pygame.font.Font(None, 36)
    score_text = "Score: " + str(success_count) + "/100"
    score_surface = font.render(score_text, True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))

    # 스톱워치 출력
    if end_time is None:
        elapsed_time = (current_time - start_time) // 1000  # ms를 초로 변환
    else:
        elapsed_time = (end_time - start_time) // 1000  # 게임 종료 시간을 기준으로 계산

    timer_text = "Elapsed Time: " + str(elapsed_time) + "s"
    timer_surface = font.render(timer_text, True, (0, 0, 0))
    screen.blit(timer_surface, (10, 50))

    pygame.display.flip()

# 게임 종료 후 결과 화면
screen.fill(WHITE)
font = pygame.font.Font(None, 72)
result_text = "Game Over"
result_surface = font.render(result_text, True, (255, 0, 0))
screen.blit(result_surface, ((WIDTH - result_surface.get_width()) // 2, (HEIGHT - result_surface.get_height()) // 2))

score_text = "Your Score: " + str(success_count) + "/100"
score_surface = font.render(score_text, True, (0, 0, 0))
screen.blit(score_surface, ((WIDTH - score_surface.get_width()) // 2, ((HEIGHT - score_surface.get_height()) // 2) + 100))

elapsed_time_text = "Elapsed Time: " + str(elapsed_time) + "s"
elapsed_time_surface = font.render(elapsed_time_text, True, (0, 0, 0))
screen.blit(elapsed_time_surface, ((WIDTH - elapsed_time_surface.get_width()) // 2, ((HEIGHT - elapsed_time_surface.get_height()) // 2) + 200))

pygame.display.flip()

# 게임 종료 대기
pygame.time.wait(5000)  # 5초 동안 결과 화면을 보여줌

pygame.quit()
