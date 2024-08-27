options = [.20, .30, .40, .50, .60, .70]

choice = int(input("Which number will you pick? 0-5")) 

scratch_off = options[choice]
print(scratch_off)

price = 29.95

discount = price * scratch_off
print(discount)

total = price - discount
print(total)

people = int(input("How many people?"))

per_person =  total/people

print(round(per_person,2))