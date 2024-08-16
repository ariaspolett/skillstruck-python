#Checkpoint
string1 = "My birthday "
string2 = "is coming up "
string3 = "very soon."
string4 = string1 + string2 + string3
print(string4)

#Challenge - Personal Info
name = input("Please input your name.")
age = input("Please input your age.")
birthday = input("Please input your birthday.")
personal_info = ("Hi " + name + "!" + " You are " + age + " years old and you were born on " + birthday + ".")
print(personal_info)

#Challenge - Combine Strings and Integer Inputs
number = input("Please enter a number.")
word = input("Please enter a word.")
connect = number + word
print(connect)

#Challenge - Crazy Concatenation Sentence
animal = input("enter the name of an animal.")
place = input("enter the name of a place.")
plural_noun = input("enter any plural noun.")
adjective = input("enter any adjective.")
crazy_sentence = ("Today I rode a " + animal + " to the " + place + " to buy some " + plural_noun + "." + " It was " + adjective + ".")
print(crazy_sentence)

#Challenge - Halloween Candy Count
#This challenge was uncompleted

#Challenge - Detective Buggy's Message
recipient = input("Who is the message for?")
place = input("Where do you want to meet?")
minutes = input("In how many minutes would you like to meet?")
print("I have an important message for " + recipient + ". " + "Meet me at the " + place + " in " + minutes + " minutes. From, Detective Buggy.")