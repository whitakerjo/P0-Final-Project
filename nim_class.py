import random
import time
import turtle
from ball_class import *

class Nim:
    def __init__(self):
        self.user_clicks = 0
        self.num_balls = 0
        self.winner = ""
        #self.introduce_user()
        self.wn = turtle.Screen()
        self.ball_list = []
        #self.create_balls()
        #self.wn.onkey(self.end_turn , "e")
        # always last!
        #self.wn.listen()
        #self.wn.mainloop()
        self.your_turn = True


    def user_turn(self):                                                      #this is how many ball(s) the user will pick per turn                                 #asks the user
        while self.user_clicks < 4 or self.user_clicks > -1:                                           #while loop that works until user picks 1-4 balls
            break
        if self.user_clicks == 4:
            return 0
        #a = input("Is your turn over?")

    def computer_turn(self):
        for i in range (4, -1, -1):
            if self.num_balls % 5 == i:
                if i == 0:
                    pass
                else:
                    print(i)
                    count = 0
                    for ball in self.ball_list:
                        for i in range(self.num_balls):
                            if ball.am_I_clicked == False:
                                ball.leave_screen(100, 100)
                                # ball = self.num_balls
                                # if ball <= 4:
                                #     for i in range(ball):
                                #ball.am_I_clicked = True
                                count += 1
                                if count == i:
                                    break


    def end_turn(self):
        if self.user_clicks > 0:
            self.user_clicks = 0
        self.computer_turn()

    def check_num_clicks(self):
        if self.user_clicks > 3:
            print(self.user_clicks)
            self.user_clicks = 0
            self.your_turn = False
            return 0
            # Computer's turn

    def create_balls(self):
        for i in range(self.num_balls):
            b = Ball(self)
            b.draw_ball(random.randint(-200, 200), random.randint(-200, 200))
            self.ball_list.append(b)

    def introduce_user(self):                                                                  #introduces the user to the game and rules
        #delay = 2.0
        #print("Hello! Today you will be playing the game of Nim.")
        #time.sleep(delay)
        #print("Here are the rules:")
        #time.sleep(delay // 2)
        #print("1. You will get to choose how many balls to play with.")
        #time.sleep(delay // 2)
        #print("2. You can pick up 1 to 4 balls per turn. You and the computer will take turns picking up balls.")
        #time.sleep(delay // 2)
        #print("3. You will go first. The goal is to have the last ball(s).")
        #time.sleep(delay)
        self.num_balls = int(input("How many balls do you want to play with (more than 15)?"))       #return the value of x when it's not equal to zero



