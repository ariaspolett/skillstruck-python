my_list = input().split()

center = int(len(my_list)/2)

if len(my_list) % 2 == 1 :
    my_list.pop(center)
else:
    my_list.pop(center)
    my_list.pop(center-1)
print(my_list)