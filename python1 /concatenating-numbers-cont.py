#Checkpoint
string1 = "I have {} fish. I want {} chocolates!"
thing = 12
number = 32
print(string1.format(thing, number))

#Challenge - Sum the Digits
three = input("enter a three-digit number")
first = int(three[0])
second = int(three[1])
third = int(three[2])
sum1 = int(first + second + third)
print("The sum of those digits is " + str(sum1))

#Challenge - Trip Planner
one_day = int(input("Number of miles your car can drive in a day."))
total = int(input("Total number of miles driven to get to destination."))
days = float(total / one_day)
road_trip = "The total number of days you will need to drive there is {}"
print(road_trip.format(days))

#Challenge - First Decimal 
number = float(input("enter a number w/ a decimal"))
mod = number%100
mods = mod%10
modss = mods%1
float_to_str = str(modss)
decimal_find = float_to_str.find(".")
length_of_decimal = len(float_to_str)
cut = float_to_str[decimal_find+1:3]
cuts = int(cut)
fin = "The first decimal digit is {}"
print(fin.format(cuts))

#Challenge - Cookie Cost Calculator
dollars = int(input("how many dollars does 1 cookie cost."))
cents = int(input("how many cents does 1 cookie cost."))
cookie = int(input("how many cookies do you want to buy?"))
dollars_to_cents = dollars*100
total_cost = dollars_to_cents + cents
total_money = total_cost/100
total = total_money * cookie
message = "The total cost of {} cookies is ${}"
print(message.format(cookie, total))

#Challenge - What day is it?
#This challenge was uncompleted.