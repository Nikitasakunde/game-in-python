# snake, water gun game

import random

def gameWin(comp , you):
# if two values are equal,declare tie!
    if comp==you:
        return None
# check all possibility when computer choose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
# check all possibility when computer choose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
# check all possibility when computer choose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
# print(randNo)
if randNo == 1:
    comp= 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'
    
you = input("Your's Turn: Snake(s) Water(w) or Gun(g)?")

a = gameWin(comp,you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("the game is tie")
elif a:
    print("You Win")    
else:
    print("you lose")


    







a = input("do you want to play again? y/n")
if a == 'y':
    print('welcome')
else:
    print("stop")