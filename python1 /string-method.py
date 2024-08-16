#Checkpoint
string1 = "I wish I hadn't missed yesterday's class."
print(string1.upper())
string2 = "I FEEL BETTER BUT STILL FEEL SICK."
print(string2.lower())
string3 = "Damn, I love money." 
print(string3.replace("money", "my family"))

#Challenge - 1 to one
one = str(input("Please enter a sentence including the number one."))
print(one.replace("1", "one"))

#Challenge - Shouting Sentences
shout = str(input("Please enter a sentence."))
print(shout.upper())

#Challenge - Group Thank You Message
thanks = str(input("Please enter a few sentences that serve as a thank you message with the word I present."))
print(thanks.replace("I", "We"))

#Challenge - Where is the @?
where = str(input("Please enter a sentence with the symbol @."))
print(where.replace("@", ""))