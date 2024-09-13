#Checkpoint - 
files = open("porcupine.txt", "w")
files.write("In short, I love to code!")
files.close()

#Challenge - Never Mind
files = open("email.txt", "w")
files.write("Never mind")
files.close()

#Challenge - Custom Greeting Cards
answer = input("what do you want to say?")
files = open("report.txt", "w")
files.write(answer)
files = open("report.txt", "w")
print(files.read())