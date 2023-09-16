import pygame
import random

# 게임 화면 크기 설정
WIDTH = 800
HEIGHT = 600

# 색깔 정의 (RGB)
WHITE = (255, 255, 255)

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Rain Game")

clock = pygame.time.Clock()

# 비 클래스 정의
class Rain(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 10)
        self.rect.y = -30

    def update(self):
        # 비가 아래로 움직이도록 처리
        self.rect.y += 5

# 플레이어 클래스 정의
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
    
    def update(self):
      # 키보드 입력 처리
      keys=pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
          if player.rect.x >0:
              player.rect.x -=5
      
      if keys[pygame.K_RIGHT]:
          if player.rect.x < WIDTH-50:
              player.rect.x +=5
      
      if keys[pygame.K_UP]:
          if player.rect.y >0:
              player.rect.y -=5
      
      if keys[pygame.K_DOWN]:
          if player.rect.y < HEIGHT-50:
              player.rect.y +=5

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()

# 비 객체 생성 및 그룹에 추가
for _ in range(10):
    rain = Rain()
    all_sprites.add(rain)

player=Player() # 플레이어 객체 생성 
all_sprites.add(player) # 플레이어 객체를 그룹에 추가 

running=True 
while running:
    clock.tick(30) 
    
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running=False
    
    screen.fill((0, 0, 0))  
    
    all_sprites.update()  
    all_sprites.draw(screen)  
    
     # 충돌 감지 
     collisions=pygame.sprite.spritecollide(player , all_sprites , False )   
      
     for collision in collisions:   
         # 비와 충돌 시 게임 종료 처리
         running = False

     pygame.display.flip()

# 게임 루프 종료 후 Pygame 종료
pygame.quit()
