#Checkpoint - 
def name(first, last) :
	print("The first name is " + first )
	print("The last name is " + last)
name("Silly", "Rock")
name("Crazy", "Grass")

#Challenge - Hungry for Apples 3
fruit1 = input("Please enter the name of the fruit you would like: ")
fruit2 = input("Please enter the name of the fruit you would like: ")
fruit3 = input("Please enter the name of the fruit you would like: ")
def hungryForApples(fruit1,fruit2,fruit3):
    print(fruit1+fruit2+fruit3)
hungryForApples(fruit1,fruit2,fruit3)

#Challenge - Find the Smallest Integer Function
choice1 = int(input("What is the first number?"))
choice2 = int(input("What is the second number?"))
def my_function(choice1, choice2):
	if choice1 > choice2:
		print(choice2)
	else:
		print(choice1)
my_function(choice1,choice2)

#Challenge - How Mant are Equal Function
choice1 = int(input("What is the choice1 number?"))
choice2 = int(input("What is the choice2 number?"))
choice3 = int(input("What is the choice3 number?"))
def my_function(choice1, choice2, choice3):
	if choice1 == choice2 == choice3:
		print("3")
	elif choice1 == choice2 or choice2 == choice3 or choice1 == choice3 :
		print("2")
	else: 
		print("0")	
my_function(choice1, choice2, choice3)

#Challenge - Find the Smallest of Five Function
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))
num4 = int(input("enter a number"))
num5 = int(input("enter a number"))
def my_function(num1, num2, num3, num4, num5):
	smallest = num1
	if num2 < num1:
		smallest = num2
	if num3 < num2:
		smallest = num3
	if num4 < num3:
		smallest = num4
	if num5 < num4:
		smallest = num5
	print(smallest)
my_function(num1, num2, num3, num4, num5)

#Challenge -  Spot the Difference Function
choice1 = int(input("What is the choice1 number?"))
choice2 = int(input("What is the choice2 number?"))
choice3 = int(input("What is the choice3 number?")) 
def my_function(choice1, choice2, choice3):
	if choice1 == choice3 and choice1 != choice2:
		print("2")
	elif choice2 == choice3 and choice1 != choice2:
		print("1")
	else: 
		print("3")
my_function(choice1, choice2,choice3)

#Challenge - What Day is it Tomorrow Function
#This challenge was not completed.