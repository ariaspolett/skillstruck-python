#Checkpoint
string1 = "I have eaten {} burgers in the past week."
string2 = 3
print(string1.format(string2))

#Challenge - Print Your Age
age = 16
birthday = "this year on my birthday, I will be {}"
print(birthday.format(age))

#Challenge - Apples in Wheelbarrows
tree = int(input("Number of apples he gets from 1 tree?"))
one_wheelbarrow = float(tree / 3)
tree2 = float(one_wheelbarrow * 8)
apples = "If Bob harvested one tree, he would have {} apples per wheelbarrow. If he harvested the whole orchard, he would have {} apples per wheelbarrow."
print(apples.format(one_wheelbarrow, tree2))

#Challenge - Hours and Minutes
number = int(input("enter a number"))
count = int(number/60)
count2 = (number % 60)
h_m = "It has been {} hour(s) and {} minute(s) since midnight."
print(h_m.format(count, count2))

#Challenge - Work Tables
table = int(input("How many employees?"))
tables= int(table % 2)
if tables == 0:
    table2 = int(table/2)
    minimum = "Minimum number of tables: {}"
    print(minimum.format(table2))
elif tables == 1:
    table3 = int(table/2 + 1)
    minimums = "Minimum number of tables: {}"
    print(minimums.format(table3))

#Challenge - Marble Bags
jas = int(input("Number of bags Jasmine has."))
jas_tot = int(jas * 12)
chl = int(input("Number of bags Chloe has."))
chl_tot = int(chl * 10)
bags = "If Jasmine had {} bags, she would have {} marbles total. If Chloe had {} bags, she would have {} marbles total."
print(bags.format(jas, jas_tot, chl, chl_tot))