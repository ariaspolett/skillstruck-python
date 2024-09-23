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