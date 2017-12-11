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
        for i in range (4, -1, -1):             # Tries to take right number of balls using modulus (makes game smart)
            if self.num_balls % 5 == i:         # Determines number to take
                # print("Mod passed: ", i)
                if i == 0:
                    # Take random
                    pass
                else:
                    count = 0                   # count is the number of balls removed. Want to take i balls
                    for ball in self.ball_list:         # Go through every ball to see if it's been clicked yet
                        # print("Length: ", len(self.ball_list))
                        # print("Ball state: ", ball.am_I_clicked)
                        # for j in range(self.num_balls): # Take the number of balls not clicked
                        if ball.am_I_clicked == False:      # if balls not clicked
                            # print(i, count)
                            ball.leave_screen(100, 100)     # Make it leave
                                # ball = self.num_balls
                                # if ball <= 4:
                                #     for i in range(ball):
                            ball.am_I_clicked = True    # set as clicked
                            # print("Count: ", count)
                            count += 1
                            if count == i:
                                # print("Taken enough balls")
                                break
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
        last_pos = (-200, -200)
        for i in range(self.num_balls):
            b = Ball(self)
            b.draw_ball(last_pos[0], last_pos[1])
            last_pos = (last_pos[0] + 50, last_pos[1])
            if last_pos[0] > 400:
                last_pos = (-200, last_pos[1]+50)
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



