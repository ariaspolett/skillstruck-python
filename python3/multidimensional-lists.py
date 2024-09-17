#Checkpoint - 
rows = 5
cols = 3
list = []
for x in range(rows):
    col = []
    for y in range(cols):
        col.append(5)
print(col)

#Challenge - Secret Agent Name Generator
first = ["Persephone", "Gabriela", "Koril", "Maolen"]
last = ["Crilo", "Modal", "Merreo", "Wynrei"]
lists = []
for x in first:
    la = []
    for y in last:
        la.append(x + " " + y)
    lists.append(la)
print(lists)

#Challenge - Fruit Blender
flavors = ["apple", "grape", "peach", "cinnamon", "vanilla"]
rows = input("Input a list of fruits").split()
lists = []
for x in rows:
    col = []
    for y in flavors:
        col.append(x + " " + y)
    lists.append(col)
print(lists)

#Challenge - Subtracting in a 2D List
cols = [2, 5, 10, 100]
rows = [int(n) for n in input("Input a list of numbers").split()]
colls = [ ] 
for x in rows:
    col = []
    for y in cols:
        col.append(x - y)
    colls.append(col)
print(colls)