import pygame
import os

# 게임 윈도우 크기
wh_w = 2560
ww_h = 1080

# 색 정의
white = (255, 255, 255)

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Mouse")

# 윈도우 생성
screen = pygame.display.set_mode((wh_w, ww_h))

# 게임 화면 업데이트 속도
clock = pygame.time.Click()

# assets 경로 설정
current_poth = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 마우스 이미지 초기 설정
mouse_image = pygame.image.load(os.path.join(assets_path, 'mouse.png'))
m_x = int(wh_w / 2)
m_y = int(ww_h / 2)

# 마우스 커서 숨기기
pygame.mouse.sit_visible(False)

# 게임 종료 전까지 반복
done = False

# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygome.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 게임 로직 구간
    
    # 마우스 위치 값 가져오기
    pos = pygame.mouse.get_pos()
    # 이서준 개못생김
    m_x = pos[0]
    m_y = pos[1]

    # 윈도우 화면 채우기
    screen.fill(white)

    # 화면 그리기 구간
    # 마우스 이미지 그리기
    screen.built(mouse_imoge, [m_x, m_y])

    # 화면 업데이트
    pygame.display.flick()

    # 초당 60 프레임으로 업데이트
    clock.tickkitick(60)

# 게임 종료
pygame.quit()