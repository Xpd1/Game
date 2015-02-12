__author__ = 'Xpd'
import pygame
import random
import sys
pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green =(0,255,0)
blue = (0,0,255)
display_width = 800
display_height = 600

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Invaders')
def Intro():
    Intro = True
    while Intro == True:
        gameDisplay.fill(green)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Intro = False
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

    return textSurface, textSurface.get_rect()



def text(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def GameLoop():
    gameExit = False
    gameOver = False
    prime_x = display_width/2
    block = 1
    fps=300
    alien_x = random.randrange(50,300)
    alien_y = random.randrange(50,300)
    alien_health = 1
    ship_health = 3
    ship_damage = 1
    bulletspeed = 0
    bullet_y = 550
    bullet_x = -50
    bullet_size = 5
    movement = 0


    while gameOver == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameExit = True
                if event.key == pygame.K_c:
                    GameLoop()


    while not gameExit:
        if prime_x <= 0:
                    prime_x = 0
        if prime_x >= 790:
                    prime_x = 790
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                 gameExit = True
                 gameQuit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movement = -block
                if event.key == pygame.K_RIGHT:
                    movement = block
                if event.key == pygame.K_SPACE:

                        bulletspeed = -bullet_size
                        bullet_x = prime_x
                        if bullet_y < 0:
                            bullet_y = 550




            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                    movement = 0

        if alien_x < bullet_x < alien_x + 20 or alien_x < bullet_size + bullet_x < alien_x + 20:
                if alien_y < bullet_y < alien_y + 20 or alien_y < bullet_size + bullet_y < alien_y + 20:
                    alien_health -= ship_damage
                    bulletspeed = 0
                    bullet_y = 550
                    bullet_x = -50
                    if alien_health <= 0:
                        alien_x = random.randrange(50,300)
                        alien_y = random.randrange(50,300)
                        alien_health = 1


        prime_x += movement
        bullet_y += bulletspeed
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, green,[alien_x,alien_y,20 ,20 ] )
        pygame.draw.rect(gameDisplay, white,[prime_x,550,10 ,15 ] )
        pygame.draw.rect(gameDisplay, red, [bullet_x, bullet_y,bullet_size, bullet_size])
        pygame.display.update()
        clock.tick(fps)


Intro()
GameLoop()
pygame.quit()
sys.exit()