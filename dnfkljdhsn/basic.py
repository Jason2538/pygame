import pygame

# 창 크기
screen_width = 800
screen_height = 600

# 색깔
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 게임 초기화
pygame.init()

# 창 이름
pygame.display.set_caption("안지호 죽이기^^")

# 창 정의
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 여부
done = False  #게임이 진행 중인지 확인 하는 변수
# done인 True라면 게임이 계속 진행 중이라는 의미

# 게임 반복 구간
while not done: #게임이 진행되는 동안 계속 반복 작업 하는 while 루프
    # 이벤트 반복 구간
    for event in pygame.event.get():
        # 어떤 이벤트가 발생 하였는지 확인
        if event.type == pygame.QUIT:
            # QUIT는 윈도우 창을 닫을 떄 발생하는 이벤트
            # 창이 닫히는 이벤트가 발생했다면
            done = True #반복을 중단시켜 게임 종료
    # 게임 로직 구간

    # 화면 삭제 구간

    # 스크린 채우기
    screen.fill(blue)

    # 화면 그리기 구간

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()
