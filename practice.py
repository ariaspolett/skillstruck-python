files = open("append-a-line-to-a-text-file.txt", "a")
files.write("I love programming!")
files = open("append-a-line-to-a-text-file.txt", "r")
print(files.read())