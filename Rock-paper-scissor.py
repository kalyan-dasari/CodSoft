import random

choose = ['rock','paper', 'scissor' ]
computer=random.choice(choose)
player = None
while player not in choose:
    player = input("choose any one: ").lower()
    if player in choose:
        print("player: ", player)
        print("computer: ", computer)
        if player == computer:
            print("it's a TIE! ")
        elif player == 'paper' and computer == 'rock':
            print("you won!")
        elif player == 'scissor' and computer == 'paper':
            print("you won!")
        elif player == 'rock' and computer == 'scissor':
            print("you won!")
        else:
            print("you loose!")
    else:
        print("invalid")
    