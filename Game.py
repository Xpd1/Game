__author__ = 'Xpd'
back = "bg.jpg"
sh = "ship.png"
ali = "alien.png"
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
if pygame.image.get_extended() == 0:
    print("Error: SDL_image required. Exiting.")
elif pygame.image.get_extended() == 1:
    print("Working")

clock = pygame.time.Clock()
#Nigga
gameDisplay = pygame.display.set_mode((display_width,display_height), 0, 0)
pygame.display.set_caption('Invaders')
def Intro():
    Intro = True
    while Intro == True:
    while Intro is True:
        gameDisplay.fill(green)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Intro = False
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
def Images(pic,x,y ):
    picture = pygame.image.load(pic)
    gameDisplay.blit(picture, (x,y))

def GameLoop():
    gameExit = False
    gameOver = False
    prime_x = display_width/2
    block = 3
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


    while gameOver is True:
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
                    if bullet_y < 0:
                            bullet_y = 550
                    if bullet_y == 550:
                        bulletspeed = -bullet_size
                        bullet_x = prime_x
                        if bullet_y < 0:
                            bullet_y = 550




            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                    movement = 0

        if alien_x < bullet_x < alien_x + 50 or alien_x < bullet_size + bullet_x < alien_x + 50:
                if alien_y < bullet_y < alien_y + 50 or alien_y < bullet_size + bullet_y < alien_y + 50:
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
        pygame.draw.rect(gameDisplay, green,[alien_x,alien_y,50 ,50 ] )
        Images(back, 0, 0)
        Images(ali, alien_x, alien_y)
        Images(sh ,prime_x-22, 545)

        pygame.draw.rect(gameDisplay, red, [bullet_x, bullet_y,bullet_size, bullet_size])
        pygame.display.update()
        clock.tick(fps)


#Intro()
GameLoop()
pygame.quit()
sys.exit()