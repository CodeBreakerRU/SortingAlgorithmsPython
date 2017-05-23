arr = []

for x in range (8):
    arr.append (input("input number: "))
print (arr)

def bubbleSort (arr):
    n = len (arr)

    for i in range (0, n):
        for j in range (n-1, i, -1):

            if arr[j] > arr[j-1]:
                arr[j], arr [j-1] = arr [j-1], arr [j]

bubbleSort (arr)

print ("Sorted Array is : ")

for i in range(len(arr)):
    print (arr[i])
