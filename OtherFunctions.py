

from Classes import Ball,paddle
from SetValues import *
import pygame,math,time
pygame.init()

#Game Funcitons
def draw(win, paddles,ball):    #Function that changes colors of objects on screen
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)
    
    ball.draw(win)

    pygame.display.update()
    

def whichWayToMove(CheckLeftUp,CheckLeftDown,CheckRightUp,CheckRightDown,leftContact,rightContact):    #Function that moves ball in other directions
    if CheckLeftUp==True and leftContact==True:
        Ball.yMoveRate=-3 
    if CheckLeftDown==True and leftContact==True:
        Ball.yMoveRate=3
    
    if CheckRightUp==True and rightContact==True:
        Ball.yMoveRate=-3
    if CheckRightDown==True and rightContact==True:
        Ball.yMoveRate=3


def collisionDetection(ball, leftPaddle, rightPaddle):    #Function that checks if ball and paddle have made contact
    leftContactFunc=False
    rightContactFunc=False

    if (leftPaddle.x+25)==ball.x:
        if ball.y<leftPaddle.y:
            pass
        elif ball.y>leftPaddle.y+100:
            pass
        else:
            leftContactFunc=True
            Ball.xMoveRate=-5
    
    if (rightPaddle.x)==ball.x:
        if ball.y<rightPaddle.y:
            pass
        elif ball.y>rightPaddle.y+100:
            pass
        else:
            rightContactFunc=True
            Ball.xMoveRate=5
    
    if ball.y==1:
        Ball.yMoveRate=-Ball.yMoveRate
    if ball.y==499:
        Ball.yMoveRate=-Ball.yMoveRate
    
    return leftContactFunc, rightContactFunc


def ballReset(ball):    #Function that resets call to center
    if ball.x<0 or ball.x>700: 
        ball.x=350
        ball.y=250
        Ball.yMoveRate=0


def specWhichWayToMove(CheckLeftUp,CheckLeftDown,leftContact):    #Function that moves ball in other directions
    if CheckLeftUp==True and leftContact==True:
        Ball.yMoveRate=-3 
    if CheckLeftDown==True and leftContact==True:
        Ball.yMoveRate=3


#Loading Screen
def menuDraw(win,paddles,ball, check,paddleCheck,ballCheck):
    win.fill(BLACK)
    big=pygame.font.Font('Other\Montserrat-ExtraBold.ttf',70)
    small=pygame.font.Font('Other\Montserrat-ExtraBold.ttf',15)
    paddleColorChange=None
    ballColorChange=None
    for paddle in paddles:
        paddle.draw(win)
    
    ball.draw(win)

    keys=pygame.key.get_pressed()
    if keys[pygame.K_q]:
        check=1
        paddleCheck=1
    if keys[pygame.K_w]:
        check=1
        ballCheck=1
    if keys[pygame.K_BACKSPACE]:
        check=0
        paddleCheck=0
        ballCheck=0
    
    if paddleCheck==1:
        if keys[pygame.K_r]:
            paddleColorChange=RED
        if keys[pygame.K_g]:
            paddleColorChange=GREEN
        if keys[pygame.K_b]:
            paddleColorChange=BLUE

    if ballCheck==1:
        if keys[pygame.K_r]:
            ballColorChange=RED
        if keys[pygame.K_g]:
            ballColorChange=GREEN
        if keys[pygame.K_b]:
            ballColorChange=BLUE

    textTitle=big.render('Pong',False,GREY)
    win.blit(textTitle,(250,20 + (math.sin(time.time() * 10) * 5)))
    if check!=1:
        text1v1=small.render('Press 1 To Play 1v1',False,GREY)
        win.blit(text1v1,(40,400 + (math.sin(time.time() * 10) * 5)))
    if check!=1:
        text1vai=small.render('Press 2 To Play against AI',False,GREY)
        win.blit(text1vai,(40,450 + (math.sin(time.time() * 10) * 5)))
    if check!=1:
        textColorChangePaddle=small.render('Press q to change color of Paddle',False,GREY)
        win.blit(textColorChangePaddle,(380,400 + (math.sin(time.time() * 10) * 5)))
    if check!=1:
        textColorChangeBall=small.render('Press w to change color of ball',False,GREY)
        win.blit(textColorChangeBall,(380,450 + (math.sin(time.time() * 10) * 5)))
    
    textBack=small.render('press backspace to go back',False,GREY)
    win.blit(textBack,(480,480))
    
    textGreen=big.render('Green',False,GREY)
    textRed=big.render('Red',False,GREY)
    textBlue=big.render('Blue',False,GREY)
    textInstructions=small.render('press R, G,or B for desired color',False,GREY)

    if paddleCheck==1:
        win.blit(textInstructions,(230,450 + (math.sin(time.time() * 10) * 5)))
        win.blit(textGreen,(20,350 + (math.sin(time.time() * 10) * 5)))
        win.blit(textRed,(285,350 + (math.sin(time.time() * 10) * 5)))
        win.blit(textBlue,(480,350 + (math.sin(time.time() * 10) * 5)))
    
    if ballCheck==1:
        win.blit(textInstructions,(230,450 + (math.sin(time.time() * 10) * 5)))
        win.blit(textGreen,(20,350 + (math.sin(time.time() * 10) * 5)))
        win.blit(textRed,(285,350 + (math.sin(time.time() * 10) * 5)))
        win.blit(textBlue,(480,350 + (math.sin(time.time() * 10) * 5)))

    pygame.display.update()
    return check,paddleCheck,ballCheck,paddleColorChange,ballColorChange
