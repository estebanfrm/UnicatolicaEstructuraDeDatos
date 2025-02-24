arr = [3,5,1,2,8]


def InsertionSort(A):
    N = len(A) #longitud
    i=1 #comenzamos desde el segundo numero

    while i<N:
        current = A[i]
        j = i-1
        
        while j>=0 and A[j]>current:
            A[j+1]=A[j]
            j -= 1
        
        A[j+1]=current
        i += 1

InsertionSort(arr)
print("Arreglo ordenado:", arr)