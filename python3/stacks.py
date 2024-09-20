#Checkpoint - 
stack = []
stack.append("i'll")
stack.append("make no more")
stack.append("use of it")
stack.append("when theres no more you")
stack.pop()
print(stack)

#Challenge - Stack Scramble
first = "r"
second = "t"
third = "s"
fourth = "y"
fifth = "o"
stack = []
stack.append(third)
stack.append(second)
stack.append(fifth)
stack.append(first)
stack.append(fourth)
print(stack)

#Challenge - Foods with the Letter S
answer = ["apples", "steak", "potatoes", "carrots"]
word = input("enter a word")
if "s" in word:
    answer.append(word)
    print(answer)
else:
    print("The input doesn't have the letter s")

#Challenge - Word Makeover
answer = ["c", "r", "o", "a", "k"]
answer.append("i")
answer.append("n")
answer.append("g")
answer.pop()
answer.pop()
print(answer)