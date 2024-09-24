arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
number = int(input("Enter a number"))
arr.append(number)

def insertion(arr):
    indexing_leng = range(1, len(arr))
    for i in indexing_leng:
        value_sorting = arr[i]

        while arr[i-1] > value_sorting and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1
            
    return arr

print(insertion(arr))