#Checkpoint - 
class Hat:
    def __init__(self, kind, color, material):
        self.kind = kind 
        self.color = color
        self.material = material
myObject = Hat("Baseball Cap", "Blue", "Cotton")

#Challenge - A Fruit Festival
class Fruit:
    def __init__(self, shape, kind, size):
        self.shape = shape
        self.kind = kind
        self.size = size
Watermelon = Fruit("Oval-like", "Seedless", "Larger than a head")
Melon = Fruit("Sphere", "Honeydew", "Smaller than a head")
Kiwi = Fruit("Sphere", "Hawaiian", "Smaller than palm")
Pear = Fruit("Pear-shaped", "Hawaiian", "Palm-sized")
print(Watermelon.kind)
print(Melon.kind)
print(Kiwi.kind)
print(Pear.kind)

#Challenge - Pet Store
class Pet:
    def __init__(self, kind, age, color):
        self.kind = kind 
        self.age = age 
        self.color = color
Pet1 = Pet("Turtle", "3y/o", "green")
Pet2 = Pet("Dog", "5y/o", "brown")
Pet3 = Pet("Hamster", "1y/o", "silver")

#Challenge - Vacation Planner
class Vacation:
    def __init__(self, location, activity, food):
        self.location = location
        self.activity = activity
        self.food = food
vakay1 = Vacation("Italy", "Wine Tasting", "Gelato")
vakay2 = Vacation("England", "Shopping", "Biscuits&Tea")
vakay3 = Vacation("Japan", "Street Market", "Mochi")
print("I went to " + vakay1.location + " last month")
print("I want to go " + vakay2.activity + " today")
print("I want to eat " + vakay3.food + " for dessert")