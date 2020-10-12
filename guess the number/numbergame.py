import random

#start
rawnum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = random.choice(rawnum)



#hadani
print("(1.pokus) vaše číslo:")
hadani=int(input())

#POKUS 1
if hadani == num:
    print("správně")
elif hadani < num:
    print("špatně, moc malé číslo")
elif hadani > num:
    print("špatně, moc velké číslo")
else:
    print("prohrál jsi")
    

#POKUS 2
print("(2.pokus) vaše číslo:")
hadani=int(input())

if hadani == num:
    print("správně")
elif hadani < num:
    print("špatně, moc malé číslo")
elif hadani > num:
    print("špatně, moc velké číslo")
else:
    print("prohrál jsi")


#POKUS 3
print("(3.pokus) vaše číslo:")
hadani=int(input())

if hadani == num:
    print("správně")
elif hadani < num:
    print("špatně, moc malé číslo")
elif hadani > num:
    print("špatně, moc velké číslo")
else:
    print("prohrál jsi")
