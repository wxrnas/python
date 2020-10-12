import random

#vars
user = "Cutonaito is using "
keyboards = ["Leopold FC750 R", "Ducky One two mini", "SOME EXPENSIVE ONE!!"]
results = random.choices(keyboards, weights=[2, 2, 18], k=1)



print("What kind of keyboard is Cutonaito using rn?")
print("                        ")             
print(user)
print(results)


