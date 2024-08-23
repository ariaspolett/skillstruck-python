#Checkpoint
animals = ["hedgehog", "sea urchin", "echidna", "porcupine"]
for x in animals:
    print(x + " is the spikiest animal ever!")

#Challenge - Automatic Numbers
var1 = int(input('Enter a number'))
var2 = int(input('Enter another number.'))
for x in range(var1, var2 + 1):
    print(x)

#Challenge - Add the Numbers
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
var = 0
for x in range (num1, num2):
    var = var + x
print(var)

#Challenge - Factorial
number = int(input("Enter a number"))
total = 1
for x in range(1, number + 1):
    total = int(total * x)
print(str(total))