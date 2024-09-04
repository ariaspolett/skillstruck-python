#Checkpoint - 
number = 1
while number <= 50:
    print(number)
    number += 1

#Challenge - How many numbers?
total = 0
number = int(input("Enter a number"))
while number > 0:
    total += 1
    number = int(input("Enter a number or 0 to stop"))
print(total)

#Challenge - Sum of Numbers
total = 0
number = int(input("Enter a number"))
while number > 0:
    total += number
    number = int(input("Enter a number or 0 to stop"))
print(total)

#Challenge - Largest Number
my_number = int(input("Pick a number."))
largest = my_number
while my_number != 0:
    my_number = int(input("Pick a number or 0 to stop."))
    if my_number == 0:
        break
    elif my_number > largest:
        largest = my_number
print(largest)

#Challenge - Find the Average
my_number = int(input("Pick a number."))
total = my_number
totals = 0
while my_number > 0:
    my_number = int(input("Pick a number or 0 to stop."))
    total += my_number
    totals += 1
    average = total/totals
print(average)

#Challenge - Running Trainer
day1 = int(input("Enter your first distance on day 1 (10 or bigger)"))
day2 = int(input("Enter your race distance"))
total_days = 1
while day1 <= day2:
    percent = float(day1/10)
    day1 += percent
    total_days += 1
print(total_days)

#Challenge - Pirate Ship
#This challenge was not completed.