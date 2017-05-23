arr = []

for x in range(7):
    arr.append (input("input number: "))
print(arr)

def partition(arr,low,high): # pass array, first index, last index of the array
    i = (low-1)
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] <=pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort (arr, low, high):
    if low<high:
        pi = partition(arr, low, high)
        quickSort(arr,low, pi -1 )
        quickSort(arr, pi+1, high)

n= len(arr)

quickSort(arr, 0, n-1)
print ("Sorted Array is: ")
for i in range (n):
    print(arr[i])
