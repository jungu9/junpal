import pygame  # 1. pygame 선언

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (0, 0, 0)
size = [1024, 768]
screen = pygame.display.set_mode(size)


done = False
clock = pygame.time.Clock()

# pygame에 사용하도록 비행기 이미지를 호출
duck = pygame.image.load('images/duck.png')
duck = pygame.transform.scale(duck, (60, 60))


# 4. pygame 무한루프


def runGame():
    global done, duck
    x = 20
    y = 24

    while not done:
        clock.tick(60)
        screen.fill(WHITE)

        event = pygame.event.poll() #이벤트 처리
        if event.type == pygame.QUIT:
            done = True

        before_x = x
        before_y = y


        keys = pygame.key.get_pressed()

        # 방향키 입력에 대한 이벤트 처리
        if keys[pygame.K_UP] & keys[pygame.K_RIGHT]:
            x += 10
            y -= 10
        elif keys[pygame.K_UP] & keys[pygame.K_LEFT]:
            x -= 10
            y -= 10
        elif keys[pygame.K_DOWN] & keys[pygame.K_RIGHT]:
            x += 10
            y += 10
        elif keys[pygame.K_DOWN] & keys[pygame.K_LEFT]:
            x -= 10
            y += 10
        elif keys[pygame.K_UP]:
            y -= 10
        elif keys[pygame.K_DOWN]:
            y += 10
        elif keys [pygame.K_LEFT]:
            x -= 10
        elif keys[pygame.K_RIGHT]:
            x += 10

        # 부스터
        if keys[pygame.K_SPACE]:
            if keys[pygame.K_UP] & keys[pygame.K_RIGHT]:
                x += 30
                y -= 30
            elif keys[pygame.K_UP] & keys[pygame.K_LEFT]:
                x -= 30
                y -= 30
            elif keys[pygame.K_DOWN] & keys[pygame.K_RIGHT]:
                x += 30
                y += 30
            elif keys[pygame.K_DOWN] & keys[pygame.K_LEFT]:
                x -= 30
                y += 30
            elif keys[pygame.K_UP]:
                y -= 30
            elif keys[pygame.K_DOWN]:
                y += 30
            elif keys [pygame.K_LEFT]:
                x -= 30
            elif keys[pygame.K_RIGHT]:
                x += 30
        

        
        # X좌표 범위를 벗어나면 이동하지 않음
        if x <= 0:
            x = 0
        elif x >= screen.get_width() - duck.get_width():
            x = screen.get_width() - duck.get_width()

        # Y좌표 범위를 벗어나면 이동하지 않음
        if y <= 0:
            y = 0
        elif y >= screen.get_height() - duck.get_height():
            y = screen.get_height() - duck.get_height()

        screen.blit(duck, (x, y))
        pygame.display.update()


runGame()
pygame.quit()
