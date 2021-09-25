import random

def GameWin(comp,player):
    if comp == player:
        return None
    if comp == 's':
        if player == 'p':
            return True
        else:
            return False
    if comp == 'p':
        if player == 'c':
            return True
        else:
            return False            
    if comp == 'c':
        if player == 's':
            return True
        else:
            return False

comp = print("Computer Turn: Choosee between Stone(s), Paper(p) or Scisssor(c):")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
else:
    comp = 'c'        
player = input("Player Turn: Choosee between Stone(s), Paper(p) or Scisssor(s): ")
a = GameWin(comp, player)
print(f"Computer choose: {comp}")
print(f"Player choose: {player}")
if a == True:
    print("You Won!!!")
elif a == None:
    print("It is a Tie!")    
else:
    print("You loose!")    