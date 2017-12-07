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
            self.nim.ball_list.remove(self)
            self.cody.goto(10000, 10000)
            self.nim.ball_track.append(self.nim.ball_track[-1] - self.nim.user_clicks)

    def draw_ball(self, x, y):
        self.cody.pencolor("yellow")
        self.cody.penup()
        self.cody.goto(x, y)
        self.cody.pendown()
        # for balls in range(balls):
        self.cody.begin_fill()
        self.cody.circle(25)
        self.cody.penup()
        self.cody.forward(60)
        self.cody.pendown()
        self.cody.end_fill()
            # if balls > 15:
            #     self.cody.begin_fill()
            #     self.cody.circle(25)
            #     self.cody.penup()
            #     self.cody.forward(60)
            #     self.cody.pendown()
            #     self.cody.end_fill()




# def main():
#     wn = turtle.Screen()
#     wn.screensize(1200, 760, "blue")
#
#     ball = Ball()
#     balls = int(input("Please pick a number of balls to play with."))
#     ball.draw_balls(balls)
#
#     wn.exitonclick()
#
# main()





