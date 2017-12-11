import turtle
from nim_class import *


def main():
    n = Nim()                                                                       #nim object to call all nim methods
    n.introduce_user()                                                              #introduces the user and asks how many balls to play with
    n.create_balls()                                                                #creates all the balls given the amount they choose
    n.user_turn()
    # n.comput er_turn()
    n.wn.onkey(n.end_turn, "space")
    n.wn.listen()
    n.wn.mainloop()

main()
