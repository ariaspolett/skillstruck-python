got_permission = [str(n) for n in input("Input a list of names separated by spaces").split()]

permission = dict.fromkeys(got_permission, "yes")

# if "George" in permission_dictionary:
# 	permission_dictionary["George"] = "no"
	
# if "Veronica" in permission_dictionary:
# 	permission_dictionary.pop("Veronica")

print(permission)