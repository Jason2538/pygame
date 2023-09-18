import pygame
import random
import os

# 게임 화면 크기 설정
WIDTH = 1200
HEIGHT = 720

# 색깔 정의 (RGB)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


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
        self.image = pygame.image.load(os.path.join(assets_path, "steak5.jpg"))
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


all_sprites=pygame.sprite.Group()   
player_sprite=Player()   

for _ in range(10):   
    steak=Steak()   
    all_sprites.add(steak)  

start_time=None  
success_count=0  

running=True  
while running:  
    clock.tick(60)  

    current_time=pygame.time.get_ticks()  

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

       
        collisions=pygame.sprite.spritecollide(player_sprite , all_sprites , True )   
        
       
        for collision in collisions:   
            success_count+=1 

            steak=Steak()    
            all_sprites.add(steak)   

        
            # 여기에 사운드 재생 코드를 추가하세요.
       

    
    else:
            
        

    

    
      
    

    
    
    

# 게임 루프 종료 후 Pygame 종료
if success_count >= 100:
   print("승리")
   print("Time: " + str(time) + "s") 

for event in pygame.event.get():
   if event.type == pygame.QUIT:
       running=False

pygame.quit()
