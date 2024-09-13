number = int(input("Enter a number"))
total = 1
sums_total = 0
for x in range(1, number +1):
    factorial = 1
    for y in range(1, x+1):
        factorial *= y
    sums_total += factorial
print(str(sums_total))