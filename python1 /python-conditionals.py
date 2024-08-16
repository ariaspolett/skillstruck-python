#Checkpoint
age = int(input("enter your age"))
license = True
if age >= 16 and license == True:
    print("You are old enough to drive.")
else: 
    print("You are not old enough to drive.")

#Challenge - Can I Ride?
height = str(input("Enter your height in inches."))
if height >= "48":
    print("You can ride the roller coaster.")
else: 
    print("You can't ride the roller coaster.")

#Challenge - More than Average?
number = int(input("enter a number between 0 and 100."))
if number >= 50:
    print("More than average")
else: 
    print("Fewer than average")

#Challenge - Black Square
row = int(input("enter a positive one digit number"))
column = int(input("enter a positive one digit number"))
coordinates = row + column
if coordinates%2 == 0:
    print("No")
elif coordinates%2 == 1:
    print("Yes")