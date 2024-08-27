#Checkpoint -
flowers = ["rose", "tulip", "lilac", "sunflower"]
flowers.append("daisy")
print(flowers)
flowers.extend(["snapdragon", "iris", "spiderlily", "dahlia", "carnation"])
print(flowers)
flowers.insert(5, "poppy")
print(flowers)

#Challenge - Last Minute Treats
treats = ["popcorn", "popsicles", "soda", "chips", "cookies"]
more_treat = input("enter the name of another treat")
more_treats = input("enter the name of another treat")
treats.extend([more_treat, more_treats])
print(treats)

#Challenge - Olympic Events
olympics = ["track", "gymnastics", "swimming", "volleyball", "basketball"]
new_olympics = ["baseball", "skateboarding", "sport climbing", "pickleball"]
olympics.extend(new_olympics)
print(olympics)

#Challenge - Spelling Bee
word = input("enter one word")
bee = []
bee.append(word)
bee.extend(str(word))
bee.append(word)
print(bee)

#Challenge - More Siblings!
family = ["Amanda", "Levi", "Nicole", "Lilly"]
mitch = int(input("input an age"))
if mitch >= 15:
    family.insert(0, "Mitch")
    print(family)
elif 16 > mitch >= 13:
    family.insert(1, "Mitch")
    print(family)
elif 13 > mitch >= 10:
    family.insert(2, "Mitch")
    print(family)
elif 10 > mitch >= 6:
    family.insert(3, "Mitch")
    print(family)
else:
    family.append("Mitch")
    print(family)

#Challenge - Donation