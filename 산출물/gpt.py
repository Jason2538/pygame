import pygame
import random
import os

# 게임 화면 크기 설정
WIDTH = 800
HEIGHT = 600

# 색깔 정의 (RGB)
WHITE = (255, 255, 255)

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("맛있는 60계 갈비")

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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(assets_path, "people.png"))
        self.rect = self.image.get_rect()
        
    def update(self):
       keys=pygame.key.get_pressed() 
       if keys[pygame.K_LEFT]: 
           if player_sprite.rect.x >0: 
               player_sprite.rect.x -=15 

       if keys[pygame.K_RIGHT]: 
           if player_sprite.rect.x < WIDTH-50: 
               player_sprite.rect.x +=15 

       if keys[pygame.K_UP]: 
           if player_sprite.rect.y >0: 
               player_sprite.rect.y -=15 

       if keys[pygame.K_DOWN]:  
           if player_sprite.rect.y < HEIGHT-50:  
               player_sprite.rect.y +=15 


all_sprites=pygame.sprite.Group()   
player=Player()   

for _ in range(10):   
    steak=Steak()   
    all_sprites.add(steak)  

start_time=None  
success_count=0  

running=True  
while running and success_count<100:
    
    clock.tick(60)  
    
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running=False
    
     current_time=pygame.time.get_ticks()  
    
     # 시작 시간 초기화 및 성공 카운트 리셋 
     if start_time is None:   
         start_time=current_time   
    
     elapsed_time=current_time-start_time  
    
    

     screen.fill(WHITE)   

    
     all_sprites.update() 
    
      
     collisions=pygame.sprite.spritecollide(player , all_sprites , True )   
    
      for collision in collisions:    
          success_count+=1  
    
          steak=Steak()     
          all_sprites.add(steak)   
    
      time_elapsed=(elapsed_time//1000)%60   # 경과 시간 계산
    
      font_timer_info=font.render("Time:"+str(time_elapsed)+"s",True ,(BLACK))   # 경과 시간 출력 텍스트 생성
     
      screen.blit(font_timer_info,(10 ,10 ))   # 경과 시간 출력
      
    
       
      font_score_info=font.render("Score:"+str(success_count)+"/100",True ,(BLACK))   # 점수 정보 출력 텍스트 생성
     
      screen.blit(font_score_info,(10 ,40 ))   # 점수 정보 출력

    pygame.display.flip()

pygame.quit()

if success_count >= 100:
    print("승리")
    print("Time: " + str(time_elapsed) + "s") 
