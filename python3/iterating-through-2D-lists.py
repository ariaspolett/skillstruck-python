#Checkpoint -
my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]
rows = 5
cols = 3
for x in range(rows):
    for y in range(cols):
        my_list[x][y] = my_list[x][y] + 3
print(my_list)

#Challenge - Multiply List Values
my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
rows = 4
cols = 3
mult = int(input("enter a number: "))
for x in range(rows):
    for y in range(cols):
        my_list[x][y] = my_list[x][y] * mult
print(my_list)

#Find the Largest Value
x = int(input("What is the first number?"))
y = int(input("What is the second number?"))
z = int(input("What is the third number?"))
my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]
rows = 4
cols = 3
largest = 0
for x in range(rows):
    for y in range(cols):
        if my_list[x][y] > largest:
            largest = my_list[x][y]
print(largest)