earningsgoal = int(input("How much do you want to save in a year?"))
month = earningsgoal/12
week =  earningsgoal/48
day = earningsgoal/365
months = round(month, 2)
weeks = round(week, 2)
days = round(day, 2)
print("To save up " + str(earningsgoal) + " dollars per year, you will need to save " + str(months) + " dollars per month.")
print("To save up " + str(earningsgoal) + " dollars per year, you will need to save " + str(weeks) + " dollars per week.")
print("To save up " + str(earningsgoal) + " dollars per year, you will need to save " + str(days) + " dollars per day.")