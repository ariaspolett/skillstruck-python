year = int(input("enter a year"))
if year%4 == 0:
    print("Leap")
elif year%400 == 0 and year%100 == 0:
    print("Leap")
elif year%100 == 0 and year%400 == 1: 
    print("Common")
else:
    print("Common")