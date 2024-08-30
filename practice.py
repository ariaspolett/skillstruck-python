day_number = int(input("enter a number 1-365"))
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
start_of_index = 4
day_of_week_index = (start_of_index + (day_number - 1))%7
message = "The day of the week is the number {}"
print(message.format(day_of_week_index))