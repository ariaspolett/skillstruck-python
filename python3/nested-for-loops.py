#Checkpoint - 
rows = 3
pets = ["fish", "turtle", "monkey", "parrot", "dog"]
list = [[x for x in pets] for i in range(rows)]
print(list)

#Challenge - Multiply by the Number of Rows
my_list = [1, 2, 3, 4, 5]
rows = int(input("how many rows do you want?"))
lists = [[(x*rows) for x in my_list] for i in range(rows)]
print(lists)

#Challenge - Weather Watcher
rows = input("Input a list of weather").split()
cols = ["windy", "breezy", "calm"]
lists = [[(x + " " + y) for y in cols] for x in rows]
print(lists)