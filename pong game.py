import pygame, random
from pygame.locals import *
pygame.init()

screen_width, screen_height = 1024, 768 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game") 
white = (255, 255, 255)

def start_screen():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
        screen.fill((0, 0, 0))
        pong_start = pygame.image.load("pong start screen.png")
        pong_play = pygame.image.load("pong play button.png")
        controls = pygame.image.load("controls.png")
        play_pos = Rect(screen_width/2 - 130, 384, 260, 70)
        mouse_pos = pygame.mouse.get_pos()
        play_pos.collidepoint(mouse_pos)
        play_pos = pong_play.get_rect()
        play_pos = play_pos.move(screen_width/2 - 130, 384)
        screen.blit(pong_start, (screen_width/2 - 260, 192))
        screen.blit(pong_play, (screen_width/2 - 130, 384))
        screen.blit(controls, (screen_width/2 - 201, 500))
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if play_pos.collidepoint(mouse_pos):
                start = False
        pygame.display.flip()

def background():
    screen.fill((0, 0, 0))
    for y in range(0, screen_height, 20):
        pygame.draw.line(screen, white, [screen_width/2, y], [screen_width/2, y], 5)
    pygame.time.Clock().tick(60)

def controls():
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if paddle1.top > 0:
            paddle1.y -= 15
    if key[pygame.K_s]:
        if paddle1.bottom < screen_height:
            paddle1.y += 15
    if key[pygame.K_UP]:
        if paddle2.top > 0:
            paddle2.y -= 15
    if key[pygame.K_DOWN]:
        if paddle2.bottom < screen_height:
            paddle2.y += 15
    if key[pygame.K_ESCAPE]:
        pygame.quit()

ball = pygame.Rect(screen_width/2, 0, 10,10)
paddle1 = pygame.Rect(50,screen_height/2 - 25, 10,75)
paddle2 = pygame.Rect(screen_width-50,screen_height/2 - 25, 10,75)

velocity_x = random.choice([random.uniform(-6,-8), random.randint(6,8)])
velocity_y = random.randint(6,9)
acceleration = 0.5
score1 = 0
score2 = 0

start_screen()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    background()
    myfont = pygame.font.SysFont("Arial", 100)
    label = myfont.render(str(score1), True, white)
    screen.blit(label, (screen_width/2 - 110, 50))
    myfont = pygame.font.SysFont("Arial", 100)
    label = myfont.render(str(score2), True, white)
    screen.blit(label, (screen_width/2 + 60, 50))
    ball.x += velocity_x
    ball.y += velocity_y
    pygame.draw.rect(screen, white, ball)
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)
    controls()
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        velocity_x *= -1
        if velocity_x > 0:
            velocity_x += acceleration
            velocity_y += acceleration
        else:
            velocity_x -= acceleration
            velocity_y -= acceleration
    if ball.top <= 0 or ball.bottom >= screen_height:
        velocity_y *= -1
    if ball.x > screen_width:
        score1 += 1
    if ball.x < 0:
        score2 += 1
    if ball.x > screen_width or ball.x < 0:
        ball.x = screen_width/2 - 3
        ball.y = random.choice([0,768])
        if ball.y == 0:
            velocity_x = random.choice([random.uniform(-6,-8), random.randint(6,8)])
            velocity_y = random.randint(6,8)
        if ball.y == 768:
            velocity_x = random.choice([random.uniform(-6,-8), random.randint(6,8)])
            velocity_y = random.uniform(-6,-8)
    
    pygame.display.flip()

pygame.quit()