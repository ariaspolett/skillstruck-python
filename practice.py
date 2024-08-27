family = ["Amanda", "Levi", "Nicole", "Lilly"]

mitch = int(input("input an age"))

if mitch >= 15:
    family.insert(0, "Mitch")
    print(family)
elif 16 < mitch >= 13:
    family.insert(1, "Mitch")
    print(family)
elif 13 < mitch >= 10:
    family.insert(2, "Mitch")
    print(family)
elif 10 < mitch >= 6:
    family.insert(3, "Mitch")
    print(family)
else:
    family.append(["Mitch"])
    print(family)