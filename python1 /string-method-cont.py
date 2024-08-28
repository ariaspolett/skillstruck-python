#Checkpoint
string1 = "I love my mom and dad!"
print(string1[0:7])
print(string1.split())
print(len(string1))
print(string1.find("I"))

#Challenge - How many Words?
enter = str(input("Enter a sentence."))
print(len(enter.split()))

#Challenge - First and Last
string = input("enter a sentence with many e's")
first = (string.find("e"))
last = (string.rfind("e"))
print(str(first) + "-" + str(last))

#Challenge - String Characcter Selection
string1 = input("enter a word")
third = string1[2]
third_last = string1[-3]
fourth = string1[3]
selection = third + third_last + fourth
print(selection)

#Challenge - Second Time
enter = str(input("Enter a sentence with words that have the letter g."))
print(enter.rfind("g"))

#Challenge - Cut the String
enter = str(input("Enter a word with even amount of letters."))
n = len(enter)
mid = n//2
first_half = enter[:mid]
second_half = enter[mid:]
end = second_half + first_half
print(end)

#Challenge - Remove String Section
string = input("enter a sentence with two instances of j")
first = int(string.find("j"))
last = int(string.rfind("j"))
leng = int(len(string))
challenge = string[0:first]
challenges = string[last+1:leng + 1]
done = challenge + challenges
print(done)

#Challenge - Reverse String Section
string = input("enter a sentence with at least two j's")
firstj = int(string.find("j"))
secondj = int(string.rfind("j"))
js = string[firstj:secondj +1]
reverse = js[len(js)::-1]
print(reverse)