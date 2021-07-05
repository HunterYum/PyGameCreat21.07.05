import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Quiz")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\YuMinYeong\\Desktop\\파이썬 기록\\21.07.01\\PyGameCreat21.07.01\\background.png")

char = pygame.image.load("C:\\Users\\YuMinYeong\\Desktop\\파이썬 기록\\21.07.01\\PyGameCreat21.07.03\\char.png")
char_size = char.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x_pos = (screen_width /2) - (char_width / 2)
char_y_pos = screen_height - char_height

ddong = pygame.image.load("C:\\Users\\YuMinYeong\\Desktop\\파이썬 기록\\21.07.01\\PyGameCreat21.07.03\\enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10

to_x = 0
char_speed = 10

running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -=char_speed
            elif event.key == pygame.K_RIGHT:
                to_x += char_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    char_x_pos += to_x

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)

    if char_x_pos < 0:
        char_x_pos = 0
    elif char_x_pos > screen_width - char_width:
        char_x_pos = screen_width - char_width

    ddong_y_pos += ddong_speed

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    char_rect = char.get_rect()
    char_rect.left = char_x_pos
    char_rect.top = char_y_pos

    if char_rect.colliderect(ddong_rect):
        print("Bump")
        running = False

    screen.blit(background, (0, 0))
    screen.blit(char, (char_x_pos, char_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    pygame.display.update()

pygame.quit()