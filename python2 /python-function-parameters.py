#Checkpoint - 
def lunch(food):
    print("I love today's lunch of " + food)
lunch("pizza")
lunch("salad")
lunch("pasta")

#Challenge - Hungry for Apples 2
fruit = input("Please enter the name of a fruit: ")
def hungryForApples(fruit):
    print(fruit+fruit+fruit)
hungryForApples(fruit)

#Challenge - Count the Days in a Month Function
choice = int(input("Enter a number 1-12"))
def invitation (choice) :
	if choice == 1  or choice == 3 or choice == 5 or choice == 7 or choice == 8 or choice == 10 or choice == 12:
		print("31")
	elif choice == 2:
		print("28")
	else:
		print("30") 
invitation(choice)

#Challenge - Odd/Even Checking Function
def odd_even(num):
	if num % 2 == 0:
		print("even")
	else:
		print("odd")
odd_even(43)
odd_even(67)
odd_even(44)

#Challenge - A Party for the letter C
#This challenge was not completed.

#Challenge - Is it a Leap Year?
year = int(input("What year?"))
def leap_year(year):
	if year % 4 == 0  and year % 100 != 0:
		print("Leap year!")
	else:
		print("Not a leap year.")
leap_year(year)

#Challenge - Area of a Circle
radius = int(input("Enter a nnumber for the radius"))
def area_circle(radius):
    calculation = 3.14159*radius*radius
    print(round(calculation, 1))
area_circle(radius)