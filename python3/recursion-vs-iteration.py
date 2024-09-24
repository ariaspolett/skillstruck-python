#Checkpoint - 
num = int(input("enter a number"))
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
print(factorial(num))

#Challenge - Add the List
list_of_nums = [int(n) for n in input().split()]
def add(list_of_nums):
    if len(list_of_nums) == 1:
        return(list_of_nums[0])
    else:
        return list_of_nums[0] + add(list_of_nums[1:])
total = add(list_of_nums)
print(total)

#Challenge - Fibonacci
#THE CODE BELOW DOES NOT WORK, FIX SOON
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
num = int(input("enter a number"))
def numbers(num):
    if num <= 10:
        print(fibonacci[0:num])
    else:
        print(' ')
numbers(num)