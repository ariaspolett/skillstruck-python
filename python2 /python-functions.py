#Checkpoint - 
def race():
    print("Micheal Jackson won the race?!")
race()

#Challenge - Charlie the Dog
def charlie():
    print("Charlie is the best dog ever! He's super cute and he follows me around everywhere. He cheers me up when I'm sad and watches shows with me. He barks a lot but it doesn't bother me that much anymore, it's reassuring if anything.")
charlie()

#Challenge - Start the Game
init = input("Launch game? Enter yes or no.")
def initialize():
    if init == "yes":
        print("Initialization Complete")
    else:
        print("Initialization Failed")
initialize()

#Challenge - Chickens and Eggs
chickens = 35
eggs_per_week = 5
def farmer():
    print(chickens*eggs_per_week)
farmer()

#Challenge - Hello Generator
number = int(input("Choose a number"))
def how_many():
    print("Hello"*number)
how_many()

#Challenge - Hungry for Apples
def hungry():
    fruit = input("Enter the name of a fruit")
    print(fruit*3)
hungry()

#Challenge - Cube Calculations
length = 4
def surface_area():
    print(length*length*6)
surface_area()
def volume():
    print(length*length*length)
volume()