def binary_search(A,target):
    indexHigh = len(A)-1
    indexLow=0

    while indexLow<=indexHigh:
        indexMid=round((indexHigh+indexLow)/2)

        if A[indexMid]== target:
            return indexMid
        
        elif A [indexMid] < target:
            indexLow = indexMid+1
        
        else:
            indexHigh=indexMid-1
            
    return -1

A=[1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
print(binary_search(A, target)) 