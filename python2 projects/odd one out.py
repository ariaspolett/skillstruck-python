#CODE IS STILL NOT CORRECT 
words = input().split()
letter_count = []
for word in words:
	if word[0] not in letter_count:
		letter_count.append(word[0])
		letter_count.append(1)
	else:
		letter_count[letter_count.index(word[0])+1] += 1

max_count = 0 
most_common_letter = ""
for i in range(0, len(letter_count), 2):
    if letter_count[i+1] > max_count:
        max_count = letter_count[i + 1]
        most_common_letter = letter_count[i]

common_words = [word for word in words if word.startswith(most_common_letter)]

print(common_words)