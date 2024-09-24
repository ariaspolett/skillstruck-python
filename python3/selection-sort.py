arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
number = int(input("Enter a number"))
arr.append(number)
def selection(arr):
    indexing_leng = range(0, len(arr)-1)

    for i in indexing_leng:
        mini_value = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini_value]:
                mini_value = j
        if mini_value != i:
            arr[mini_value], arr[i] = arr[i], arr[mini_value]
    return arr
sorted_arr = selection(arr)
print(sorted_arr)