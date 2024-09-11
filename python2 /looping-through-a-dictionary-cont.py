#Checkpoint - 
ride = {
    "Minni" : 123, 
    "Lio" : 143,
    "Paul" : 112,
    "Charl" : 102, 
    "Clare" : 99
}
for x in ride.values():
    if x >= 100:
        print("This person is tall enough to ride.")
    else:
        print("This person is too short to ride.")

#Challenge - Check for a Key
dictionary = { 7: "first", 3: "second", 4: "third", 8: "fourth", 9: "fifth" }
my_list = [int(n) for n in input().split()]
for x in my_list:
    if x in dictionary:
        print("Yes")
    else:
        print("No")

#Challenge - Word Frequency
#This challenge was not completed.

#Challenge - Power Dictionary
n = int(input("How many keys in dictionary?"))
dictionary = {}
for i in range(n):
    dictionary[i] = i * i
print(dictionary)

#Challenge - Thesaurus
#This challenge was not completed.

#Challenge - Student Body President
#This challenge was not completed.