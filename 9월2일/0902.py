import pygame
import os
import sys

# 스크린 크기
sc_w = 2560
sc_h = 1080


# 색정의
white = (255, 255, 255)
black = (0,0,0)
green = (0,255,0)
skyblue = (0, 209, 255)
red = (255, 0, 0)

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")

x=0

# 초기화
pygame.init()
pygame.display.set_caption("qhrtmq")
screen = pygame.display.set_mode((sc_w, sc_h))
clock = pygame.time.Clock()
# 게임 종료 전 까지 반복

key_x = int(sc_w / 2)
key_y = int(sc_h / 2)
key_dx = 0
key_dy = 0


done = False



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
    

    key_x += key_dx
    key_y += key_dy
    

    screen.fill(white)



    pygame.draw.line(screen, red, [50, 50], [300, 300], 10)
    pygame.draw.line(screen, red, [300, 50], [50, 300], 10)
    pygame.draw.rect(screen, green, [200, 200, 50, 50], 0)
    pygame.draw.circle(screen, black, [300, 300],10 ,3)


    image = pygame.image.load(os.path.join(assets_path, "fish.png"))
    font = pygame.font.SysFont("Malgun Gothic", 30, False, False)
    foont = pygame.font.SysFont("Malgun Gothic", 20, False, False)
    tetxt = font.render("안녕 호박빈대떡 오락아.", True, black)
    text = foont.render("9월2일 토요일", True, black)
    screen.blit(image, [key_x, key_y])
    screen.blit(tetxt, [10,10])
    screen.blit(text, [10, 40])

    # if x <= 730:
    #         x+=5





    pygame.display.flip()
    clock.tick(120)
pygame.quit()