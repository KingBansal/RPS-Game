import random
import time

sci = """
\ /
 A
O O
"""

pap = """
 ____
|^^^ |
|^^*^|
|____|
"""

rok = """
 _
/ \\
\_/
"""


outcomes = ["rock", "paper", "scissor"]
number = random.randint(0, 2)
user_points = 0
comp_points = 0
round = 1


def call():
    global cmd
    cmd = input(f">ROUND {round}:")


while True:
    if round > 3:
        print(f"YOU: {user_points} \nME: {comp_points}")
        if user_points > comp_points:
            print("YOU WON!!!")
        else:
            print("YOU LOST!!!")
        break
    call()
    if cmd == "scissor" or cmd == "rock" or cmd == "paper":
        number = random.randint(0, 2)
        reply = outcomes[number]
        print(reply)
        if cmd == reply:
            print("Huh! its a draw")
        else:
            round += 1
            if cmd == "scissor" and reply == "rock":
                comp_points += 1
                print('I won this round! To check scores type "scores"')
            elif cmd == "rock" and reply == "paper":
                comp_points += 1
                print('I won this round! To check scores type "scores"')
            elif cmd == "paper" and reply == "scissor":
                comp_points += 1
                print('I won this round! To check scores type "scores"')
            else:
                user_points += 1
                print('You won this round! To check scores type "scores"')
    elif cmd == "quit":
        break
    elif cmd == "scores":
        print(f"YOU: {user_points} \nME: {comp_points}")
    elif cmd == "help":
        print(
            'RESPONSES: "rock","paper","scissor" \nTYPE "quit" TO QUIT THE GAME \nTYPE "scores" TO KNOW SCORES'
        )
    else:
        print('Please enter a valid response! \nTYPE "help" TO KNOW COMMANDS')
