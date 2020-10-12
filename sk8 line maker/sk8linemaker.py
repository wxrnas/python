import random

#tricks
out = ["kickflip", "shuvit", "tre flip", "heelflip", "front shuvit"]
results0 = random.choices(out, weights=[2, 1, 1, 2, 1], k=1)

#slides/grinds
grindslide = ["50/50", "tail slide", "nose slide", "5/0", "Nose grind", "boardslide", "croocked", "lip slide", "blunt slide"]
results1 = random.choices (grindslide, weights=[2, 1, 2, 1, 1, 1, 2, 1, 1],k=1)


#text
a = "your skate line:"
b = "+"


#code
print(a)
print(results1)
print(b)
print(results0)
