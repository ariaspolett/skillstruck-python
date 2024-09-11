dinosaur = {}
new_dino = input("What dino do you want to add? ")
while new_dino != "triceratops":
    dino_height = int(input("How tall is your dinosaur? "))
    dinosaur[new_dino] = dino_height
    new_dino = input("What dino do you want to add? ")
dino_height = int(input("How tall is your dinosaur? "))
dinosaur[new_dino] = dino_height
print(dinosaur)