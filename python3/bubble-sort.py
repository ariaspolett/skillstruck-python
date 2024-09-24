#Checkpoint - 
arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
number = int(input("Enter a number"))
arr.append(number)
def bubble(arr):
    indexing_leng = len(arr) - 1
    sorteds = False

    while not sorteds:
        sorteds = True
        for i in range(0, indexing_leng):
            if arr[i] > arr[i+1]:
                sorteds = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
sorted_arr = bubble(arr)
print(sorted_arr)