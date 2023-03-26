import pygame # 1. pygame 선언
 
pygame.init() # 2. pygame 초기화
 
# 3. pygame에 사용되는 전역변수 선언
WHITE = (0,0,0)
size = [1024, 768]
screen = pygame.display.set_mode(size)

 
done= False
clock= pygame.time.Clock()
 
# pygame에 사용하도록 비행기 이미지를 호출
duck = pygame.image.load('images/duck.png')
duck = pygame.transform.scale(duck, (60, 60))
 
# 4. pygame 무한루프
def runGame():
    global done, duck
    x = 20
    y = 24
 
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
 
            # 방향키 입력에 대한 이벤트 처리
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 30
                elif event.key == pygame.K_DOWN:
                    y += 30
                elif event.key == pygame.K_LEFT:
                    x -= 30
                elif event.key == pygame.K_RIGHT:
                    x += 30
    
        if x <= 0:
            x = 0
        elif x >= 1024:
            x = 1024
        
        if y<= 0:
            y = 0
        elif y >= 768:
            y = 768


        screen.blit(duck, (x, y))
        pygame.display.update()
 
runGame()
pygame.quit()
