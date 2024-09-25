input_words = input("Enter a list of words separated by spaces: ")

words = input_words.split()

starting_letter_count = {}

for word in words:
    starting_letter = word[0].lower()  
    if starting_letter in starting_letter_count:
        starting_letter_count[starting_letter] += 1
    else:
        starting_letter_count[starting_letter] = 1

most_common_letter = max(starting_letter_count, key=starting_letter_count.get)

result_words = [word for word in words if word.startswith(most_common_letter)]

print(' '.join(result_words))