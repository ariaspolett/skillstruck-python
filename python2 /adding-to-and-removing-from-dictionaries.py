#Checkpoint - 
friends = {
	"Shane" : 10,
	"Samantha" : 9,
	"Shiloh" : 12,
	"Sean" : 11	
}
friends["Sebastian"] = 8
print(friends)
friends.pop("Shiloh")
print(friends)

#Challenge - Dictionary of Shapes
my_shape = input("What shape do you want to add?")
my_shape_height = int(input("How tall is your shape?"))
shapes = {
    "Triangle": 8,
    "Circle": 15,
    "Square": 10,
	"Rectangle" : 12,
}
shapes[my_shape] = my_shape_height
print(shapes)

#Challenge - Arborist
trees = { "aspen" : 75, "pine" : 82, "maple" : 60, "oak" : 65, "willow" : 80, "cottonwood" : 100 }
remove = input("which tree would you like to remvoe?")
trees.pop(remove)
print(trees)

#Challenge - Goals 
goals = { "piano" : 5, "run" : 3, "paint" : 2, "serve" : 7, "homework" : 7}
remove = input("enter the goal you wish to remove")
goals.pop(remove)
print(goals)

#Challenge - Dinosaurs 
dinosaur = {}
new_dino = input("What dino do you want to add? ")
while new_dino != "triceratops":
    dino_height = int(input("How tall is your dinosaur? "))
    dinosaur[new_dino] = dino_height
    new_dino = input("What dino do you want to add? ")
dino_height = int(input("How tall is your dinosaur? "))
dinosaur[new_dino] = dino_height
print(dinosaur)