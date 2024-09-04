#Checkpoint -
harvest = ["pumpkins", "apples", "corn", "squash", "carrots"]
harvest.remove("squash")
good = harvest.pop(1)
print(harvest)

#Challenge - Skills
skills = ["Piano", "Soccer", "Coding", "Cooking", "Writing"]
skill = input("enter a skill from the list above")
skills.remove(skill)
print(skills)

#Challenge - Bronze Medal
my_list = input().split()
name = my_list.pop(2)
print(name + " got the bronze medal")

#Challenge - Beans
my_list = input().split()
my_list.remove("lima")
print(my_list)

#Challenge - Remove the Center Number
my_list = input().split()
center = int(len(my_list)/2)
if len(my_list) % 2 == 1 :
    my_list.pop(center)
else:
    my_list.pop(center)
    my_list.pop(center-1)
print(my_list)