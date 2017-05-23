A = [] # declare array

for n in range (10): # 10 numbers
    A.append(input("Input Number: "))
print (A)

def insertionSort(A): # Define unsertion Sort

    for j in range (1,len(A)):
        key=A[j]
        i = j-1
        while (i>=0 and A[i]>key):
            A[i+1] = A[i]
            i = i-1
            A[i+1] = key

insertionSort (A) # define our function and pass argument
print ("Sorted Array")
for k in range (len(A)):
    print (A[k])
