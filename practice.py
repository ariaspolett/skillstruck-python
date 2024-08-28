string = input("enter a sentence with at least two j's")
firstj = int(string.find("j"))
secondj = int(string.rfind("j"))
js = string[firstj:secondj +1]
reverse = js[len(js)::-1]
print(reverse)