#Checkpoint - 
measurement = {
    "length" : 4,
    "width" : 6,
    "depth" : 7
}
for x in measurement.values():
    print(x)

#Challenge - Secret Beach Day
amanda_people = int(input("How many people will Amanda bring?"))
jane_people = int(input("How many people will Jane bring?"))
group = { "Fred" : 12, "Jackson" : 15, "Sophie" : 20, "Amanda" : amanda_people, "Jane" : jane_people,}
total = 0
for x in group.values():
    total += x
print(total)

#Challenge - Add it All Together
first = int(input("Pick a first number"))
second = int(input("Pick a second number"))			
group = {
	3 : 10,
	5 : 3,
	10 : 6,
	4 : 30,
	first : second
}
total = 0
for x,y in group.items():
	total = total + (x * y)
print(total)

#Challenge - Boxes
num = int(input("enter a number 1-10"))
group = { "box1" : 5, "box2" : 2, "box3" : 10, "box4" : 3, "box5" : num }
total_vol = 0
for y in group.values():
    volume = 25*y
    total_vol = total_vol + volume
print(total_vol)

#Challenge - Shoes
name = input("enter a name")
shoes = int(input("enter a number"))
group = {
    "Sally" : 10,
    "Cameron" : 3, 
    "Spencer" : 6, 
    name : shoes
}
for x,y in group.items():
    print(str(x) + " has " + str(y) + " pairs of shoes.")

#Challenge - Family Banquet
#This challenge was not completed.