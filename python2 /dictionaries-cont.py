#Checkpoint - 
coins = { 
    "pennies" : 43,
    "nickels" : 8,
    "dimes" : 54,
    "quarters" : 69
}
coins["silver dollar"] = 23
coins.pop("pennies")
print(coins)
print(len(coins))

#Challenge - How Many?
dictionary = {
	1: "bicycle",
	2: "soccer balls",
	3: "piano books"
}
dictionary[4] = input("What do you have 4 of?")
dictionary[5] = input("What do you have 5 of?")
dictionary[6] = input("What do you have 6 of?")  
print(dictionary)

#Challenge - Work Schedule
work = {
    "Monday" : 5,
    "Tuesday" : 8,
    "Wednesday" : 6,
    "Thursday" : 7,
    "Friday" : 5,
}
work["Saturday"] = 5
work.pop(
    "Wednesday")
print(len(work))
if "Friday" in work:
    print(work)

#Challenge - Word Counter
#This challenge was not completed.

#Challenge - Fruit Shopping List
shopping = {
}
apples = int(input("enter the number you need of this fruit"))
bananas = int(input("enter the number you need of this fruit"))
strawberries = int(input("enter the number you need of this fruit"))
if apples > 5 and bananas > 7 and strawberries > 3:
    shopping["apples"] = 5
    shopping["bananas"] = 7
    shopping["strawberries"] = 3
    print(shopping)
else:
    " "

#Challenge - Permission Slips
got_permission = [str(n) for n in input("Input a list of names separated by spaces").split()]

permission = dict.fromkeys(got_permission, "yes")

# if "George" in permission_dictionary:
# 	permission_dictionary["George"] = "no"
	
# if "Veronica" in permission_dictionary:
# 	permission_dictionary.pop("Veronica")

print(permission)