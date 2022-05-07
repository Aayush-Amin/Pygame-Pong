from SetValues import *
from Classes import paddle, Ball,specLeft, aiPaddle
from OtherFunctions import draw,whichWayToMove,collisionDetection,ballReset,menuDraw,specWhichWayToMove
import pygame
pygame.init()

def loadingScreen(checkLoad):
    running=True
    FPS=pygame.time.Clock()
    
    leftPaddle=paddle(     10   , WIDTH/2-paddleHeight/2, paddleWidth, paddleHeight)    #Placing Paddle
    rightPaddle=paddle(HEIGHT-30, WIDTH/2-paddleHeight/2, paddleWidth, paddleHeight)    #Placing Paddle
    ball=Ball(HEIGHT/2 ,WIDTH/2 ,7)    #Placing Ball
    
    check=None
    ballCheck=None
    paddleCheck=None
    while running:    #Main Loop that runs the game
        FPS.tick(60)
        check,paddleCheck,ballCheck,paddleColorChange,ballColorChange=menuDraw(win, [leftPaddle,  rightPaddle], ball, check,paddleCheck,ballCheck)
        
        if paddleColorChange==None:
            pass
        else:
            paddle.color=paddleColorChange  
        if ballColorChange==None:
            pass
        else:
            Ball.color=ballColorChange

        for event in pygame.event.get():    #For Loop checking if window is closed
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()

        keys=pygame.key.get_pressed()
        if keys[pygame.K_1]:
            checkLoad=1
            return checkLoad
        if keys[pygame.K_2]:
            checkLoad=2
            return checkLoad


def oneVone():    
    running=True
    FPS=pygame.time.Clock()

    leftPaddle=paddle(     10   , WIDTH/2-paddleHeight/2, paddleWidth, paddleHeight)    #Placing Paddle
    rightPaddle=paddle(HEIGHT-30, WIDTH/2-paddleHeight/2, paddleWidth, paddleHeight)    #Placing Paddle
    ball=Ball(HEIGHT/2 ,WIDTH/2 ,7)    #Placing Ball
    

    while running:    #Main Loop that runs the game
        FPS.tick(60)
        draw(win, [leftPaddle,  rightPaddle], ball)
        for event in pygame.event.get():    #For Loop checking if window is closed
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()  
        
        ballReset(ball)    #calls function to reset ball
        
        pressedKey=pygame.key.get_pressed()    #Get key pressed value
        
        CheckLeftUp,CheckLeftDown,CheckRightUp,CheckRightDown=leftPaddle.move(pressedKey, leftPaddle, rightPaddle)    #Call function to move paddle
        CheckLeftUp,CheckLeftDown,CheckRightUp,CheckRightDown=rightPaddle.move(pressedKey, leftPaddle, rightPaddle)    #Call function to move paddle

        ball.move()    #call funtion to move ball

        leftContact,rightContact=collisionDetection(ball, leftPaddle, rightPaddle)    #call function to check collision        
        whichWayToMove(CheckLeftUp,CheckLeftDown,CheckRightUp,CheckRightDown, leftContact,rightContact)    #call function to move ball in other directions  


def oneVai():
    running=True
    FPS=pygame.time.Clock()

    leftPaddle=specLeft(     10   , WIDTH/2-paddleHeight/2, paddleWidth, paddleHeight)    #Placing Paddle
    rightPaddle=aiPaddle(HEIGHT-30, WIDTH/2-paddleHeight/2, paddleWidth, paddleHeight)    #Placing Paddle
    ball=Ball(HEIGHT/2 ,WIDTH/2 ,7)    #Placing Ball
    

    while running:    #Main Loop that runs the game
        FPS.tick(60)
        draw(win, [leftPaddle,  rightPaddle], ball)
        for event in pygame.event.get():    #For Loop checking if window is closed
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()

        ballReset(ball)    #calls function to reset ball
        
        pressedKey=pygame.key.get_pressed()    #Get key pressed value
        
        CheckLeftUp,CheckLeftDown=leftPaddle.move(pressedKey, leftPaddle)    #Call function to move paddle
        rightPaddle.move(ball)    #Call function to move paddle

        ball.move()    #call funtion to move ball
    
        leftContact,rightContactFunc=collisionDetection(ball, leftPaddle, rightPaddle)    #call function to check collision        
        specWhichWayToMove(CheckLeftUp,CheckLeftDown, leftContact)    #call function to move ball in other directions


checkLoad=True
while checkLoad==True:
    checkLoad=loadingScreen(checkLoad)
    if checkLoad==1:
        break
while checkLoad==1:
    oneVone()
while checkLoad==2:
    oneVai()
