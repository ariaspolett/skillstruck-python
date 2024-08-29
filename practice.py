my_list = [int(n) for n in input("Input a list of numbers").split()] 

cash_back = []

for x in my_list:
	if x >= 5:
		cash_back_amount = x * .1
		cash_back.append(round(cash_back_amount,1))
		
print(cash_back)