import random
import time
import turtle
from ball_class import *

class Nim:
    def __init__(self):
        self.user_clicks = 0
        self.num_balls = 0
        self.winner = ""
        self.wn = turtle.Screen()
        self.ball_list = []
        self.your_turn = True

    def user_turn(self):
        while self.user_clicks < 4 or self.user_clicks > -1:  # while loop that works until user picks 1-4 balls
            break
        if self.user_clicks == 4:
            if len(self.ball_list) == 0:
                print("The computer has won.")
            return 0
        if len(self.ball_list) == 0:
            print("The computer has won.")

    def computer_turn(self):
        self.user_clicks = 0
        if len(self.ball_list) == 0:
            print("The player has won.")
        for i in range(4, -1, -1):  # Tries to take right number of balls using modulus (makes game smart)
            if self.num_balls % 5 == i:  # Determines number to take
                if i == 0:
                    count1 = 0
                    count = random.randint(1,4)
                    for ball in self.ball_list:
                        if ball.am_I_clicked == False:
                            ball.leave_screen(100,100)
                            ball.am_I_clicked = True
                            count1 += 1
                            if count1 == count:
                                break
                            self.user_clicks = 0
                    pass
                else:
                    count = 0  # count is the number of balls removed. Want to take i balls
                    for ball in self.ball_list:  # Go through every ball to see if it's been clicked yet
                       if ball.am_I_clicked == False:
                            ball.leave_screen(100, 100)
                            ball.am_I_clicked = True
                            count += 1
                            if count == i:
                                break
                    self.user_clicks = 0
                    break

    def end_turn(self):
        if self.user_clicks > 0:
            self.user_clicks = 0
        self.computer_turn()

    def check_num_clicks(self):
        if self.user_clicks > 3:
            print(self.user_clicks)
            self.user_clicks = 0
            return 0
            # Computer's turn

    def create_balls(self):
        last_pos = (-200, -200)
        for i in range(self.num_balls):
            b = Ball(self)
            b.draw_ball(last_pos[0], last_pos[1])
            last_pos = (last_pos[0] + 50, last_pos[1])
            if last_pos[0] > 400:
                last_pos = (-200, last_pos[1] + 50)
            self.ball_list.append(b)

    def introduce_user(self):  # introduces the user to the game and rules
        delay = 2.0
        print("Hello! Today you will be playing the game of Nim.")
        time.sleep(delay)
        print("Here are the rules:")
        time.sleep(delay // 2)
        print("1. You will get to choose how many balls to play with.")
        time.sleep(delay // 2)
        print("2. You can pick up 1 to 4 balls per turn. You and the computer will take turns picking up balls.")
        time.sleep(delay // 2)
        print("3. You will go first. The goal is to have the last ball(s).")
        time.sleep(delay)
        print("4. To play, simply click the number of balls you want to take on your turn. When you're done, hit space to confirm the computer turn.")
        self.num_balls = int(input("How many balls do you want to play with (more than 15)?"))  # return the value of x when it's not equal to zero
