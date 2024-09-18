answer = "y"
names = []
while answer == "y":
    name = input("What is the name of your contact?")
    names.append(name)
    answer = input("Do you want to add more contacts? y or n.")
names.sort()
print(names)