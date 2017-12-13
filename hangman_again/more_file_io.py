import os
import random

file_names = os.listdir("data")

for i,f in enumerate(file_names):
    print(str(i)+ ") " + f)

choice = input("Which one? ")
choice = int(choice)

file = "data/" + file_names[choice]

with open(file,'r') as f:
    lines = f.read().splitlines()

print(lines)

category = lines[0]
puzzle = random.choice(lines[1:])

print(category)
print(puzzle)
