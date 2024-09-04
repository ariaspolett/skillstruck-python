x = 0
y = 0
run=True
while x<=5 and y<=5 and x>=0 and y>=0 and run == True:
	direction=input('What way would you like to go (n,s,e,w)? ')
	if direction == "n":
		y+=1
	elif direction == "s":
		y-=1
	elif direction == "e":
		x+=1
	elif direction == "w":
		x-=1
	elif direction=='exit':
		print('Program exited. You left the grid at (' + str(x) + ',' + str(y) + ')')
		run=False
	else:
		print('Bad input')
    if not (0 <= x <= 5 and 0 <= y <= 5): 
        print(f'You left the grid at ({x}, {y})') 
        run = False 
print('You left the grid at ' + '(' + str(x) + "," + str(y) + ')')