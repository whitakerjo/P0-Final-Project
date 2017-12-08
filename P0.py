import turtle
from nim_class import *


def main():
    n = Nim()
    n.introduce_user()
    n.create_balls()
    n.user_turn()
    # n.computer_turn()
    n.wn.onkey(n.end_turn(), "Space")
    n.wn.listen()
    n.wn.mainloop()

main()
