#Checkpoint - 
money = open("reading-parts-of-a-file.txt","r")
print(money.read(10))
print(money.readline())
print(money.readline())
money.close()

#Challenge - Read a Specific Number of Characters
number = int(input("enter a number"))
files = open("reading-parts-of-a-file.txt", "r")
print(files.read(number))

#Challenge - How Many Words?
#This challenge was not completed.

#Challenge - How many Lines?
money = open('reading-parts-of-a-file.txt','r')
print(len(money.readlines()))
money.close()