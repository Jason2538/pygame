import pygame
import random
import os
import sys

# 게임 화면 크기 설정
WIDTH = 800
HEIGHT = 600

# 색깔 정의 (RGB)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")


# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("steak game")

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
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player.rect.x >0:
                player.rect.x -=15
        
        if keys[pygame.K_RIGHT]:
            if player.rect.x < WIDTH-50:
                player.rect.x +=15
        
        if keys[pygame.K_UP]:
            if player.rect.y >0:
                player.rect.y -=15
        
        if keys[pygame.K_DOWN]:
            if player.rect.y < HEIGHT-50:
                player.rect.y +=15

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()

# 스테이크 객체 생성 및 그룹에 추가
for _ in range(10):
    steak = Steak()
    all_sprites.add(steak)

player=Player() # 플레이어 객체 생성 
player_sprite.add(player) # 플레이어 객체를 그룹에 추가 

start_time= None 
success_count=0 


running=True 
while running:
    clock.tick(120) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    

    
    current_time=pygame.time.get_ticks() 
    
     # 시작 시간 초기화 및 성공 카운트 리셋 
    if start_time is None:  
        start_time=current_time  
        success_count=0
    
    elapsed_time=current_time-start_time  
    
    


    if elapsed_time<=60000:
        screen.fill(WHITE)  
      
        all_sprites.update()
        player_sprite.update()
        all_sprites.draw(screen)
        player_sprite.draw(screen)  
    
        # 충돌 감지 
        collisions=pygame.sprite.spritecollide(player , all_sprites , True )   
        for collision in collisions:   
            success_count+=1 
        
            steak=Steak()    
            all_sprites.add(steak)   
        
            # 여기에 사운드 재생 코드를 추가하세요.
       
        time = (pygame.time.get_ticks()) // 1000
     
        # 타이머 출력 
        font = pygame.font.Font(None, 36)  
        timer_text = "Time: " + str(time) + "s"
        timer_surface = font.render(timer_text, True, (0, 0, 0))     
        screen.blit(timer_surface, (10 ,10))

        # 점수 출력 
        score_text="Score: "+str(success_count)+"/100" 
        score_surface=font.render(score_text,True ,(0 ,0 ,0 ))    
        screen.blit(score_surface,(10 ,60 ))
     
    else:
                
        font_end_score_info=pygame.font.Font(None ,48 )     
        end_score_info="Your Score: "+str(success_count)+"/1000"   
        end_score_info_surface=font_end_score_info.render(end_score_info,True ,(255 ,
                                                165 ,
                                                40 ))    
        screen.blit(end_score_info_surface,(WIDTH//2 -150   ,
                                                HEIGHT//2 +20 ))

    pygame.display.flip()


if success_count >= 100:
    print("승리")
    print("Time: " + str(time) + "s")
    pygame.QUIT()


pygame.quit()