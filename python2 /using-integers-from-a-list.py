#Checkpoint - 
lasers = [3, 10, 4, 15, 11]
print(lasers[2]*10)
pi = 3.14159265
print(round(pi,3))
for x in range(0,10):
    print(x)
for x in range(0,10,2):
    print(x)

#Challenge - Add the List
my_list = [int(n) for n in input().split()]
total = 0
for x in my_list:
    total = total + x
print(total)

#Challenge - Multiply the List
my_list = [int(n) for n in input().split()]
total = 1
for x in my_list:
    total = total * x
print(total)

#Challenge - Get Info Fast
my_list = ["James", 10, "blue", "Zoe", 8, "red", "Dan", 12, "pink", "Shana", 11, "orange", "Sebastian", 9, "yellow", "Cynthia", 13, "green"]
know = input("What do you want to know?")
if know == "name":
    print(my_list[0:18:3])
elif know == "age":
    print(my_list[1:18:3])
elif know == "favorite color":
    print(my_list[2:18:3])
else: 
    print("Invalid Inpput")

#Challenge - Paddle Board
options = [.20, .30, .40, .50, .60, .70]
choice = int(input("Which number will you pick? 0-5")) 
scratch_off = options[choice
price = 29.95
discount = price * scratch_off
total = price - discount
people = int(input("How many people?"))
per_person =  total/people
print(round(per_person,2))