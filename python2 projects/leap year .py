year = int(input("enter a year"))
if year%4 == 0:
    print(str(year) + " is a leap year")
elif year%400 == 0 and year%100 == 0:
    print(str(year) + " is a leap year")
elif year%100 == 0 and year%400 == 1: 
    print(str(year) + " is not a leap year")
else:
    print(str(year) + " is not a leap year")