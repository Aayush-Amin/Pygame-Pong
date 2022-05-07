import pygame
pygame.init()

HEIGHT,WIDTH=700,500    #Loading Window
win=pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption('pong')

WHITE=(255,255,255)    #Defining colors
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
DARKGREY=(100,100,100)
GREY=(180,180,180)

paddleWidth,paddleHeight=20,100    #Paddle Dimentions
ballWidth,ballHeight=10,10    #Ball Dimentions

runTest=0

#All My Text
font=pygame.font.Font('C:\Windows\Fonts\segoeprb.ttf',50)
pong=font.render('Pong',True,GREEN)
pressSpace=font.render('Press Space To Start',True,GREEN)

