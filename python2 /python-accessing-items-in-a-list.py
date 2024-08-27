#Checkpoint -
strings1 = ["Love", "Peace", "Trees","Hatred", "Wars"]
print(strings1[2])
print('I love forests! ' + strings1[2] + ' are so large and imposing.')

#Challenge - Multiply Center Number
my_list = [int(n) for n in input("Create a list of 9 numbers").split()]
print(my_list[4]*100)

#Challenge - Getting Around
my_list = input("Enter 5 strings").split()
print("Some animals " + my_list[0] + " and some " + my_list[4])

#Challenge - First Two, Last Two
my_list = [int(n) for n in input("Create a list of 6 numbers").split()]
print(my_list[0] + my_list[1] + my_list[4] + my_list[5])

#Challenge - Missing Number
my_list = [int(n) for n in input("Input a list of numbers").split()]
for x in my_list:
	missing = x + 1
	if missing not in my_list:
		print(missing)

#Challenge - Boat Cruise
choice = input("Choose a letter")	
boat = "On our boat cruise we saw crocodiles, flamingos, turtles, fish, and even a manatee!"
if choice in boat:
	words = boat.split(choice)
	print(words)
else:
	print("The letter " + choice + " is not in the string")