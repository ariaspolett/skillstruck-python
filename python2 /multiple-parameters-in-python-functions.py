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