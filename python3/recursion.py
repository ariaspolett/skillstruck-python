#Checkpoint - 
this_list = ['panda', 'lion', 'giraffe', 'tiger', 'elephant', 'monkey', 'fish', 'snake', 'bearded dragon', 'koala']
def feeding(this_list):
    if len(this_list) == 1:
        print("The " + this_list[0] + " has been fed")
    else:
        mid = len(this_list) // 2
        first_half = this_list[:mid]
        second_half = this_list[mid:]
        feeding(first_half)
        feeding(second_half)
feeding(this_list)

#Challenge - Books and Sequels
books = [int(n) for n in input("Input a list of numbers").split()]
def book(books):
    if len(books) == 2:
        add = books[0] + books[1]
        print(add)
    else:
        mid = len(books)//2
        first = books[:mid]
        second = books[mid:]
        book(first)
        book(second)
book(books)

#Challenge - Pollinating Bees
flowers = [int(n) for n in input("How many blossoms are on each tree? ").split()]
def orchard(flowers):
    if len(flowers) == 1:
        multiply = flowers[0] * 3
        print(multiply)
    else:
        mid = len(flowers)//2
        first = flowers[:mid]
        second = flowers[mid:]
        orchard(first)
        orchard(second)
orchard(flowers)