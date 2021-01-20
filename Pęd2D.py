import turtle
import time
import random
import math
import numpy as np
# Tworzenie konsoli
wn = turtle.Screen()
wn.setup(800,600)
wn.title("Pęd")
wn.bgcolor("black")
wn.tracer(0)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
#tworzenie cząstek
class Ball():
    def __init__(self,xpos,ypos,mass,dx, dy,color):
        self.shape = ("circle")
        self.mass = mass
        self.dx = dx
        self.dy = dy
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.width = 20
        self.height = 20
        self.momentum = self.mass*math.sqrt((self.dx**2)+(self.dy**2))
        self.energy = (1/2)*((self.dx**2)+(self.dy**2))
        self.newdx = self.dx
    def render(self,pen):
        pen.goto(self.xpos,self.ypos)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

    def movement(self):
        self.xpos += self.dx
        self.ypos += self.dy
        if self.xpos > 400 - 10  or self.xpos < -400+10:
            self.dx *= -1
        if self.ypos > 300 - 10  or self.ypos <= -300+10:
            self.dy *= -1

    def is_collision(self, other):
        if math.sqrt((other.xpos - self.xpos) ** 2 + (other.ypos - self.ypos) ** 2) < 20:
            return True
        else:
            return False
    def after_collision(self,other):
         self.dx = ((self.newdx*(self.mass - other.mass) + 2*other.mass*other.newdx)/(self.mass+other.mass))
         other.dx = (other.newdx*(other.mass - self.mass) + 2*self.mass*self.newdx)/(self.mass+other.mass)
         self.newdx = self.dx






ball1 = Ball(250,200,1,-2,0,"white")
ball2 = Ball(-250,200,1,3,0,"yellow")
Balls = [ball1,ball2]

while True:
    pen.clear()
    for ball in Balls:
        ball.render(pen)
        ball.movement()
    if ball1.is_collision(ball2):



        print(ball1.dx,ball2.dx)

    wn.update()
    time.sleep(0.025)










