dollars = int(input("how many dollars does 1 cookie cost."))
cents = int(input("how many cents does 1 cookie cost."))
cookie = int(input("how many cookies do you want to buy?"))
dollars_to_cents = dollars*100
total_cost = dollars_to_cents + cents
total_money = total_cost/100
total = total_money * cookie
message = "The total cost of {} cookies is ${}"
print(message.format(cookie, total))