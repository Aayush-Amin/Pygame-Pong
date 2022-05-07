from SetValues import *
import pygame
pygame.init()

class paddle:
    color=WHITE

    def __init__(self,x,y,width,height):    #Paddle Setup
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    
    def draw(self, win):    #Displaying paddle
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move(self,key,leftPaddle,rightPaddle):
        checkLeftUp=False
        checkLeftDown=False
        checkRightUp=False
        checkRightDown=False
        if key[pygame.K_w] and leftPaddle.y!=0:
            leftPaddle.y-=2
            checkLeftUp=True
        if key[pygame.K_s] and leftPaddle.y!=400:
            leftPaddle.y+=2
            checkLeftDown=True

        if key[pygame.K_UP] and rightPaddle.y!=0:
            rightPaddle.y-=2
            checkRightUp=True     
        if key[pygame.K_DOWN] and rightPaddle.y!=400:
            rightPaddle.y+=2 
            checkRightDown=True

        return checkLeftUp,checkLeftDown,checkRightUp,checkRightDown


class Ball:
    color=WHITE
    xMoveRate=5
    yMoveRate=0

    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
    
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x-=self.xMoveRate
        self.y+=self.yMoveRate


class specLeft:
    color=WHITE

    def __init__(self,x,y,width,height):    #Paddle Setup
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    
    def draw(self, win):    #Displaying paddle
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move(self,key,leftPaddle):
        checkLeftUp=False
        checkLeftDown=False
        if key[pygame.K_w] and leftPaddle.y!=0:
            leftPaddle.y-=4
            checkLeftUp=True
        if key[pygame.K_s] and leftPaddle.y!=400:
            leftPaddle.y+=4
            checkLeftDown=True

        return checkLeftUp,checkLeftDown


class aiPaddle:
    color=WHITE

    def __init__(self,x,y,width,height):    #Paddle Setup
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    
    def draw(self, win):    #Displaying paddle
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


    def move(self,ball):
        if ball.y>45 and ball.y<450:
            self.y=ball.y-50 
