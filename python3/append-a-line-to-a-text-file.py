#Checkpoint - 
files = open("append-a-line-to-a-text-file.txt", "a")
files.write("I love programming!")
files = open("append-a-line-to-a-text-file.txt", "r")
print(files.read())

#Challenge - Pen Pal
files = open("letter.txt","a")
letter.write("From your Pen Pal")
files = open("letter.txt","r")
print(files.read())

#Challenge - Give Credit
files = open("report.txt", "a")
report.write("Quote was said by Gandhi")
files = open("report.txt", "r")
print(files.read())

#Challenge - Custom Line
response = input("Enter a a line you want to add to the text file.")
files = open("report.txt", "a")
report.write(response)
files = open("report.txt", "r")
print(report.read())