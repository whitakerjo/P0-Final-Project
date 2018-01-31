import turtle
import random

class Ball:

    def __init__(self, nim):
        self.nim = nim
        self.size = 0
        self.color = ""
        self.cody = turtle.Turtle()
        self.cody.onclick(self.leave_screen)
        self.am_I_clicked = False

    def leave_screen(self, x, y):
        self.am_I_clicked = True
        self.nim.num_balls -= 1
        if self.nim.your_turn == True:
            self.cody.clear()
            self.nim.user_clicks += 1
            self.nim.check_num_clicks()
            self.cody.penup()
            self.cody.goto(100, 100)


    def draw_ball(self, x, y):
        wn = turtle.Screen()
        wn.screensize(1200, 760, "blue")
        self.cody.speed(0)
        self.cody.pencolor("yellow")
        self.cody.penup()
        self.cody.goto(x, y)
        self.cody.pendown()
        self.cody.begin_fill()
        self.cody.circle(25)
        self.cody.penup()
        self.cody.forward(60)
        self.cody.pendown()
        self.cody.end_fill()




