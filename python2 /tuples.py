#Checkpoint - 
grades = (95, 70, 85, 92, 100)
print(grades)
print(grades[-2])
print(grades[0:3])

#Challenge - Check for Number
friends = (3, 5, 7, 8, 10, 2, 12, 4)
num = int(input("enter a number"))
if num in friends:
    print("Yes")
else:
    print("No")

#Challenge - Third from last
random = ("money", "must", "be", "funny", "ina", "rich", "mans", "world")
print(random[-3])
print(random[5])
print(random[0:4])

#Challenge - Negative Range
candies = (3, 5, 7, 8, 10, 2, 50, 4, 29, 14)
print(candies[-4:-1])