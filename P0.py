from Nim import Nim
import turtle

class Ball:

    def __init__(self):
        self.size = 0
        self.color = ""

    def draw_balls(self, balls):
        cody = turtle.Turtle()
        cody.penup()
        cody.goto(-300, 0)
        cody.pendown()
        if balls == 15:
            for balls in range(15):
                cody.circle(25)
                cody.penup()
                cody.forward(60)
                cody.pendown()
        elif balls == 16:
            for balls in range(16):
                cody.circle(25)
                cody.penup()
                cody.forward(60)
                cody.pendown()
        elif balls == 17:
            for balls in range(17):
                cody.circle(25)
                cody.penup()
                cody.forward(60)
                cody.pendown()
        elif balls == 18:
            for balls in range(18):
                cody.circle(25)
                cody.penup()
                cody.forward(60)
                cody.pendown()
        elif balls == 19:
            for balls in range(19):
                cody.circle(25)
                cody.penup()
                cody.forward(60)
                cody.pendown()
        elif balls == 20:
            for balls in range(20):
                cody.circle(25)
                cody.penup()
                cody.forward(60)
                cody.pendown()
        else:
            print("Invalid answer. Please pick another.")

    def user_picks(self):
        '''
        This function is where the user will click on the screen with the amount of balls they want to take for their turn.
        :return:
        '''



def main():
    wn = turtle.Screen()
    wn.screensize(1200, 760, "blue")

    ball = Ball()
    balls = int(input("Please pick a number of balls to choose from between 15 and 20."))
    ball.draw_balls(balls)

    wn.exitonclick()


main()





