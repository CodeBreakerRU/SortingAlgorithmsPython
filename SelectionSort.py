arr = []

for x in range (6):
    arr.append(input("input number: "))
print(arr)

def selectionSort(arr):
    n=len(arr)
    for j in range(0, n-1):
        smallest = j
        for i in range (j+1, len(arr)):
            if arr[i] < arr [smallest]:
                smallest=i
        arr[j], arr[smallest] =arr [smallest], arr[j]


selectionSort(arr)
print("Sorted Array: ")
print(arr)
