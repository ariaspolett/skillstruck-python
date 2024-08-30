#Checkpoint
coins = 10
if coins > 20:
    print("You have more than enough money to buy a puppy")
elif coins == 20: 
    print("You have exactly enough to buy a puppy")
else: 
    print("You do not have enough to buy a puppy")

#Challenge - Greater than?
number = input("enter a number")
number2 = input("enter another number")
if number > number2: 
    print("The first number is larger.")
elif number2 > number:
    print("The second number is larger.")
elif number == number2:
    print("The numbers are the same.")

#Challenge - Smallest of Three Numbers
number = input("Enter a number")
number2 = input("Enter a number")
number3 = input("Enter a number")

if number < number2 and number < number3:
    print(number)
elif number2 < number and number2 < number3:
    print(number2)
elif number3 < number and number3 < number2:
    print(number3)
elif number == number2 and number < number3:
    print(number)
elif number2 == number3 and number2 < number:
    print(number2)
elif number3 == number and number3 < number2:
    print(number3)
else:
   print("zero")

#Challenge - Equal Numbers
number = input("Enter a number")
number2 = input("Enter a number")
number3 = input("Enter a number")

if number == number2 and number == number3:
    print("3")
elif number == number2 or number == number3 or number2 == number3:
    print("2")
else:
    print("0")

#Challenge - Forest Adventure
choice = input("which direction should you go?")
if choice == "left":
    print("You walk down the left path and your eyes widen when you realize the building is an abandoned Taco-Bell. You walk inside and explore. Unfortunately, you do not make it through the night. The rats got you.")
elif choice == "right":
    print("You walk down the right path and you frown softly as you progress further and the last light of the sun fades through the tick bushes. You continue walking until you come across a well. You approach the well and take a look inside. You jolt back when you gaze upon the face of a young girl's lifeless eyes.")
elif choice == "center": 
    print("You walk down the center path and you feel yourself tense up as the rustling sounds grow louder. You feel the hairs on your neck stand up and you freeze as you gaze upon a creek filled with bones.")
else: 
    print("You decided to turn around and go home. You should be glad. You could've met a terrible end.")

#Challenge - Order of Outlier

#make sure that only 2 numbers are the same
number1 = input("Enter a number")
number2 = input("Enter a  number")
number3 = input("Enter a number")

if number1 == number2 and number1 != number3:
    print("3")
elif number1 == number3 and number1 != number2:
    print("2")
elif number2 == number3 and number2 != number1:
    print("1")
else: 
    print("0")

#Challenge - Order the Digits
number1 = int(input("Enter a number"))
number2 = int(input("Enter a number"))
number3 = int(input("Enter a number"))

if number1 < number2 and number2 < number3 :
    print(number1, number2, number3)
elif number2 < number1 and number1 < number3:
    print(number2, number1, number3)
elif number3 < number1 and number1 < number2:
    print(number3, number1, number2)
elif number3 < number2 and number2 < number1:
    print(number3, number2, number1)
elif number2 < number3 and number3 < number1:
    print(number2, number3, number1)
elif number1 < number3 and number3 < number2:
    print(number1, number3, number2)
else: 
    print("nothing")

#Challenge - Days in a Month
number = int(input("enter a number 1-12"))
if number == 1:
    print("31")
elif number == 2:
    print("28")
elif number == 3:
    print("31")
elif number == 4:
    print("30")
elif number == 5:
    print("31")
elif number == 6:
    print("30")
elif number == 7:
    print("31")
elif number == 8:
    print("31")
elif number == 9:
    print("30")
elif number == 10:
    print("31")
elif number == 11:
    print("30")
elif number == 12:
    print("31").

#Challenge - Same Color
num1 = int(input("enter number 1-8"))
num2 = int(input("enter number 1-8"))
num3 = int(input("enter number 1-8"))
num4 = int(input("enter number 1-8"))
square1 = num1 + num1
square2 = num3 + num4
if square1%2 == 0 and square2%2 == 0:
    print("Yes")
else: 
    print("No")

#Challenge - Leap Year
year = int(input("enter a year"))
if year%4 == 0:
    print("Leap")
elif year%400 == 0 and year%100 == 0:
    print("Leap")
elif year%100 == 0 and year%400 == 1: 
    print("Common")
else:
    print("Common")