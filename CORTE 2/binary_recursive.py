def binarySearch(A, target, low =0, high=None):
    if high is None:
        high = len(A) - 1
    if low > high:
        return -1  

    mid = (low + high) // 2

    if A[mid] == target:
        return mid  
    elif A[mid] < target:
        return binarySearch(A, target, mid + 1, high)
    else:
        return binarySearch(A, target, low, mid - 1)

A=[1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
print(binarySearch(A, target))