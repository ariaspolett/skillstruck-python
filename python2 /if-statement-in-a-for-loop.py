#Checkpoint - 
foods = ["Radish", "Salmon", "Shrimp", "Ceviche", "Beets", "Asparagus"]
for x in foods:
	if foods == "mushroom":
		print(x + " is gross")
	elif foods == "broccoli":
		print(x + " is gross")
	elif foods == "fish":
		print(x + " is gross")
	else:
		print(x + " is gross")

#Challenge - Count the Zeros
my_list = [int(n) for n in input("Input a list of numbers").split()]
total = 0
for number in my_list :
	if number == 0:
		total += 1
print(total)

#Challenge - Find the Even Numbers
my_list = [int(n) for n in input().split()]
for number in my_list:
    if number % 2 == 0:
        print(number)

#Challenge - World Travel
my_list = input().split()
countries = my_list
for country in countries:
    if "p" in country.lower() or "P" in country.upper():
        print(country)

#Challenge - Better than Average
my_list = [int(n) for n in input().split()]
total = 0
for x in my_list:
	total = total + x

average = total/len(my_list)

for x in my_list :
	if x > average:
		print(x)

#Challenge - Color Inspector
choice = input("Choose a letter")
letter = choice
my_list = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white", "gray", "pink", "indigo", "brown", "tan", "gold", "silver"]
total = 0
for x in my_list:
	if letter in x:
		total += 1
print("There are " + str(total) + " items in the list that have the letter " + choice + " in it.")