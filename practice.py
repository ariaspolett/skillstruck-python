month = input("enter a month 1-12: ")
date = input("enter a date 1-31: ")
month = int(month)
date = int(date)

def next_day(month, date):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if date < 31:
            next_date = date + 1
            next_month = month
        else: 
            next_month = month + 1 if month < 12 else 1
            next_date = 1
    elif month == 2:
        if date < 28:
            next_date = date + 1
            next_month = month
        else: 
            next_month = month + 1
            next_date = 1
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if date < 30:
            next_date = date + 1
            next_month = month
        else:
            next_month = month + 1
            next_date = 1
    return next_month, next_date

result = next_day(month, date)
if result:
    next_month, next_date = result
    print(next_month,next_date)