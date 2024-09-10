#Checkpoint -
mountains = {"Timpanogos" : 6, "Everest": 10, "Kilimanjaro": 7, "Vesuvius": 5}
print(mountains)
print(mountains["Vesuvius"])
mountains["Kilimanjaro"] = 8
print(mountains)

#Challenge - Dictionary Author
holidays = {"January" : "New Years", "Febuary" : "Valentines", "March" : "love", "May" : "school", "July" : "Fourth", "August" : "birthday", "October" : "halloween", "November" : "grateful", "december" : "gifts", "june" : "mom"}
print(holidays)

#Challenge - Dictionaries and Lists
packing = {"shoes": "vans", "socks": "dots", "shirts": "cotton", "pants": "jeans", "pjs": "stripes", "money" : "greed", "mom" : "warmth", "dad" : "warm", "siblings" : "loud", "family" : "good"}
print(packing)
packing_list = ["shoes", "socks", "shirts", "pants", "pjs"]
print(packing_list)

#Challenge - Survival
knife = int(input("From 1-10, how important is a knife?"))
fire_starter = int(input("From 1-10, how important is a fire starter?"))
pot = int(input("From 1-10, how important is a pot?"))
rope = int(input("From 1-10, how important is a rope?"))
tarp = int(input("From 1-10, how important is a tarp?"))
survive = { "knife" : knife, "fire starter": fire_starter, "pot": pot, "rope": rope, "tarp": tarp}

print(survive)

#Challenge - Color Dictionary
colors = {
    "red" : 3,
    "blue" : 4,
    "orange" : 5,
    "purple" : 6, 
    "pink" : 7
}
print(colors["orange"])
print(colors["purple"])
colors["red"] = 2
colors["blue"] = 1
print(colors)

#Challenge - All the Pets
pets = {
    "fish" : 30,
    "dogs" : 2,
    "chickens" : 5,
    "cats" : 2,
    "bunnies" : 1
}
pets["fish"] = 20
pets["bunnies"] = 7
print("Because 10 fish died, and the bunny had 6 babies, you now have " + str(pets["fish"]) + " and " + str(pets["bunnies"]) + " at your house.")
print(pets)