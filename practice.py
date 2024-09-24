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