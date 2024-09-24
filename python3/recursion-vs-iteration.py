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
final = []
def numbers(num):
    if num <= 1:
        return num
    else:
        return(numbers(num-1) + numbers(num-2))
length = int(input("enter a number"))
for i in range(length):
    final.append(numbers(i))
print(final)