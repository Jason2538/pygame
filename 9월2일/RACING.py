import pygame
import os
import sys
import random
from time import sleep

# 게임 스크린 전역변수
sc_w = 480
sc_h = 800

# 색상 전역변수
black = (0, 0, 0)
white = (255,255,255)
gray = (150, 150,150)
red = (200, 0, 0)

# 게임 전역 변수 
car_c = 3
lane_c = 5
speed = 10

class Lane():
    def __init_(self):
        self.color = white
        self.w = 10
        self.h = 80
        self.gap = 20
        self.space= (sc_h - (self.w*lane_c)) / (lane_c -1)
        self.count = 10
        self.x = 0
        self.y = - self.height

# # 자동차 객체
# class Car():
#     def __init__(self, x=0, y=0, dx=0, dy=0)
#         self.x =x
#         self.y =y




def main():
    pygame.init()
    pygame.display.set_caption("부릉")
    screen = pygame.display.set_mode((sc_w, sc_h))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(gray)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
main()