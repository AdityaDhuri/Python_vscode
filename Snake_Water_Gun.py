import random

def gameWin(comp, player):
    if comp == player:
        return None
    if comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True
    elif comp == 'w':
        if player == 'g':
            return False
        elif player == 's':
            return True
    elif comp == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True               

comp = print("Computer Turn: choose between Snake(s), water(w) or gun(g):")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'

player = input("Player Turn: choose between Snake(s), water(w) or gun(g):")

print(f"Computer choose: {comp}")
print(f"Player choose: {player}")
a = gameWin(comp, player)
if a == None:
    print("Game is a tie!!!")
elif a == True:
    print("You Won the Game.")
else:
    print("You loose.")        