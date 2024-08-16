#Checkpoint
polett_age = 16
kaitlyn_age = 14
if polett_age > kaitlyn_age:
    print("Kaitlyn looks older than Polett is.")
else: 
    print("Kaitlyn is super old!")

#Challenge - Minimum of Two Numbers
number = input("enter a number")
number2 = input("enter another number")
if number < number2:
    print(number)
else:
    print(number2)

#Challenge - Sign Switcher
number = input("Enter any number, positive or negative.")
positive = "0"
if number < positive:
    print("-1")
else: 
    print("1")

#Challenge - Three Digit Number
number = int(input("Please enter a positive number"))

if 100 <= number <= 999:
    print("Yes")
else:
    print("No")

#Challenge - Odd or Even
number = int(input("enter a number."))
math = number % 2 
if math == 0: 
    print("Even")
else: 
    print("Odd")

#Challenge - Divide by 3?
number = 152
if number % 3 == 0: 
    print("This number is divisble by 3")
else: 
    print("This number is not divisble by 3")