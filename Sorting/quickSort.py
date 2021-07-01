def quickSort(arr):
    _quickSort(arr, 0, len(arr)-1)

def _quickSort(arr, lo, hi):
    if lo >= hi:
        return
    pivot = partition(arr, lo, hi)

    #partition left subarray with respect to pivot
    _quickSort(arr, lo, pivot-1)
    #partition right subarray with respect to pivot
    _quickSort(arr, pivot+1, hi)
    
def partition(arr, lo, hi):
    #returns the index of the pivot element
    #everything with index < index of pivot is < pivot
    #[1,3,4,2,5,8,10,12] #if 8 is the pivot element
    pivot = arr[lo]
    swapIndex = lo+1
    for i in range(lo+1, hi+1):
        if arr[i] < pivot:
            arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
            swapIndex += 1
    arr[lo], arr[swapIndex-1] = arr[swapIndex-1], arr[lo]
    return swapIndex-1
    
if __name__ == '__main__':
    arr = [10,9,8,7,6,5,4,3,2,1,14,13,13] #average case O(N logN)
    quickSort(arr)
    print(arr)
    arr = [10,9,8,7,6,5,4,3,2,1] #worst case O(N^2) #can be avoided by picking the pivot randomly
                                 #or we can randomly shuffle the array before starting with the current algorithm
    quickSort(arr)
    print(arr)