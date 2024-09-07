##trees = { "aspen" : 75, "pine" : 82, "maple" : 60, "oak" : 65, "willow" : 80, "cottonwood" : 100 }
#remove = input("which tree would you like to remvoe?")
#trees.pop(remove)
#print(trees)

choice1 = int(input("What is the first number?"))
choice2 = int(input("What is the second number?"))
def my_function(choice1, choice2):
	if choice1 > choice2:
		print(choice2)
	else:
		print(choice1)
my_function(choice1,choice2)