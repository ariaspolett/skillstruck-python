lists = ["money", "family", "hate", "marker", "crayon", "gamble", "creativity", "scrambles", "teacher", "write", "eat"]

number = int(input("enter a number between 0-10"))

tether = list(lists[number])

turns = 12

while turns > 0:
    turns -= 1
    my_letter = input("enter a letter")
    if my_letter == tether:
        print(my_letter)
    else: 
        print("-")

#FIGURRE THIS OUT SOON