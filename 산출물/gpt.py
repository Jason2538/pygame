import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 정의
white = (255, 255, 255)
red = (255, 0, 0)

# 시계 생성
clock = pygame.time.Clock()

# 플레이어 설정
player = pygame.Rect(400, 500, 40, 40)

# 스테이크 설정
steak_width = 40
steak_height = 40
steak_x = random.choice([0, screen_width - steak_width])  # 왼쪽 또는 오른쪽에서 무작위 선택
steak_y = random.randint(0, screen_height - steak_height)
steak = pygame.Rect(steak_x, steak_y, steak_width, steak_height)
steak_speed = 5
steak_direction = 1 if steak_x == 0 else -1  # 왼쪽에서 나오면 오른쪽으로, 오른쪽에서 나오면 왼쪽으로 이동

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # 스테이크 이동
    steak.x += steak_speed * steak_direction

    # 스테이크가 화면을 벗어나면 다시 나오도록 설정
    if steak.x > screen_width or steak.x < -steak_width:
        steak_x = random.choice([0, screen_width - steak_width])
        steak_y = random.randint(0, screen_height - steak_height)
        steak_direction = 1 if steak_x == 0 else -1
        steak.x = steak_x
        steak.y = steak_y

    # 충돌 검사
    if player.colliderect(steak):
        steak_x = random.choice([0, screen_width - steak_width])
        steak_y = random.randint(0, screen_height - steak_height)
        steak_direction = 1 if steak_x == 0 else -1
        steak.x = steak_x
        steak.y = steak_y

    # 화면 업데이트
    screen.fill(white)
    pygame.draw.rect(screen, red, player)
    pygame.draw.rect(screen, red, steak)
    pygame.display.update()

    # FPS 설정
    clock.tick(60)

pygame.quit()
