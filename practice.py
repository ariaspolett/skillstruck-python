answer = input("what do you want to say?")

files = open("report.txt", "w")
files.write(answer)

files = open("report.txt", "w")
print(files.read())