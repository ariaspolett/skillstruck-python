#Checkpoint -
my_list = ["love", "hate", "war", "peace", "time", "stars", "money"]
print(my_list[0:3])
my_list[6] = "family"
print(my_list)
print(len(my_list))

#Challenge - Find the Largest Value
my_list = [int(n) for n in input().split()]
biggest = max(my_list)
print(biggest)

#Challenge - Greater than Left Index
my_list = [int(n) for n in input().split()]
current = my_list[0]
for x in my_list:
    if x > current:
        print(x)
    current = x

#Challenge - Unique Numbers
my_list = [int(s) for s in input().split()]
new_list = [] 
for x in my_list:
	if x not in new_list:
		new_list.append(x)
print(len(new_list))

#Challenge - Swap Neighbors
#This challenge was not completed.

#Challenge - Greater than Neighbors
#This challenge was not completed.