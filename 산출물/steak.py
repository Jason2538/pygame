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

start_time = None
success_count = 0

running = True
stopwatch = pygame.time.Clock()
elapsed_time = 0

while running:
    stopwatch.tick(60)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 종료 조건: 스테이크 갯수가 100개에 도달하면 종료
    if success_count >= 100:
        print("게임 종료")
        print("Your Score: " + str(success_count) + "/100")
        running = False

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

    elapsed_time = current_time - start_time

    # 타이머 출력
    font = pygame.font.Font(None, 36)
    timer_text = "Time: " + str(elapsed_time // 1000) + "s"
    timer_surface = font.render(timer_text, True, (0, 0, 0))
    screen.blit(timer_surface, (10, 10))

    pygame.display.flip()

pygame.quit()
