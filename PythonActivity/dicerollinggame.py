import random

def get_name(key):
    n = ""
    while not n:
        n = input(f"Input your name, {key}: ")
    return n

def throw_dice(key):
    dices = random.choices(range(1,7),k=2)
    print(f"{names[key]} threw: {dices}", end = " ")
    if sum(dices) % 2 == 0:
        score[key] += 10
        print("Even. You earn 10 points.")
    else:
        score[key] -= 5
        print("Odd. You loose 5 points")

def print_score():
    for n in score:
        print(f"  {names[n]} has got {score[n]} points.")

def win_message(s,n):
    print_score()
    if score["P1"] > score["P2"]:
        print(f"{names['P1']} won")
    else:
        print(f"{names['P2']} won") 



player = ""
score = {}
names = {}

for n in ["P1","P2"]:
    names[n] = get_name(n)
    score[n] = 0

# twice the amount of rows wanted, because players take turn

for c in range(10):
    # switches between player1 and player2
    player = "P1" if player != "P1" else "P2"

    print(f"Round {c//2 + 1}: it is {names[player]}'s turn.")
    print_score()
    throw_dice(player)

win_message(score,names)