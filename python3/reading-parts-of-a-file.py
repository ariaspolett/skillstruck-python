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
files = open("reading-parts-of-a-file.txt", "r")
data = files.read()
words = data.split()
print(len(words))
files.close()

#Challenge - How many Lines?
money = open('reading-parts-of-a-file.txt','r')
print(len(money.readlines()))
money.close()