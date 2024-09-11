num_people = int(input("how many people are in a group?"))

large_pizza_feed = 7 
medium_pizza_feed = 3
small_pizza_feed = 1

mx_lg_pizza = num_people//7
remaining_people = num_people%7
mx_md_pizza = remaining_people//3
remaining_people2 = remaining_people%3
mx_sm_pizza = remaining_people2//1
remaining_people3 = mx_sm_pizza%1

print("You will need " + str(mx_lg_pizza) + " large pizzas, " + str(mx_md_pizza) + " medium pizzas, and " + str(mx_sm_pizza) + " small pizzas.")
