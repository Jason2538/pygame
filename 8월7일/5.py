import pygame
# 게임 스크린 크기
screen_w = 800
screen_h = 600

# 색정의
whit()

# pygame 초기화
pygame.init()

# 창 이름
pygame.display.set_caption("안지호 죽으렴 ^^")

# 스크린 정의
screen = pygame.display.set_mode((screen_w, screen_h))

#게임 화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로설정
current_p = os.path.dirname(__file__)
assets_p = os. path.join(current_p, 'assets')

# 키보드 이미지 초기 설정
keyboard_image = pygame.image.load(os.path.join(assets_p, 'keyboard.png'))
key_x = int(screen_w / 2)
key_y = int(screen_h / 2)
key_dx = 0
key_dy = 0

# 게임 종료 전 까지 반복
done = False

# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # 키가 눌릴 경우
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                key_dx = -10
            elif event.key == pygame.K_RIGHT:
                key_dx = 10
            elif event.key == pygame.K_UP:
                key_dy = -10
            elif event.key == pygame.K_DOWN:
                key_dy = 10
        # 키가 놓일 경우
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                key_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                key_dy = 0
    
    # 게임 로직 구간
    # 키보드 이미지의 위치 변화
    key_x += key_dx
    key_y += key_dy

    # 스크린 채우기
    screen.fill(gray)

    # 화면 그리기 구간

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()