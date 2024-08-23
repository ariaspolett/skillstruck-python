#Checkpoint
caterpillars = 3
leaves = 25
print(caterpillars * leaves)

#Challenge - Adding Numbers
number1 = int(input("What is your first number?"))
number2 = int(input("What is your second number?"))
sum = number1 + number2
print(sum)

#Challenge - Number Neighbors
number = int(input("enter a number."))
one_less = str(number - 1)
one_more = str(number + 1)
comma = (",")
number_neighbors = (one_less + comma + one_more)
print(number_neighbors)

#Challenge - Group Gift
number_people = int(input("How many people will help?"))
number_money = int(input("How much money will everyone contribute?"))
total = number_people * number_money
print(total)

#Challenge - Inheritance
family = int(input("How many family members will split the inheritance?"))
total = (48682.76/family)
print("If " + str(family) + " people split the inheritance, each person would get " + str(total) + " dollars.")

#Challenge - What's the Century?
year = int(input("What year is it?"))
century = int(year/100)
century2 = (century + 1)
print(century2)

#Challenge - Debugging Challenge 2
num_people = int(input("How many people are coming to dinner? "))
num_people = num_people

hamburger_price = 1.29
rolls_price = 0.49
corn_price = 0.80

hamburger_count = int(input("How many hamburgers will everyone have? "))
rolls_count = int(input("How many rolls will everyone have? "))
corn_count = int(input("How many pieces of corn will you have?"))

total = 0
total = total + float(hamburger_count * hamburger_price * num_people)
total = total + float(rolls_count * rolls_price * num_people)
total = total + float(corn_count * corn_price * num_people)

noChange = int(total / num_people)
change = float(total / num_people)
print("Each person owes $" + str(noChange) + " without change, or $" + str(change) + " if change is included.")