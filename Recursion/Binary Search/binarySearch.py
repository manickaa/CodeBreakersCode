def binarySearchRecursive(array, target):
    #O(log N) time
    #O(log N) space - stack space for recursive calls
    if not array or not target:
        return -1
    return _helper(array, target, 0, len(array)-1)

def _helper(array, target, lo, hi):
    if lo > hi:
        return -1
    mid = (hi+lo) // 2
    if target == array[mid]:
        return mid
    if target < array[mid]:
        return _helper(array, target, lo, mid-1)
    else:
        return _helper(array, target, mid+1, hi)

def binarySearchIterative(array, target):
    #O(logN) time
    #O(1) space - No extra space
    if not array or not target:
        return -1
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = (hi+lo) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            hi = mid -1
        else:
            lo = mid +1
    return -1

if __name__ == '__main__':
    array = [0,1,4,6,8,12,34,67,86]
    print(binarySearchRecursive(array, 6))
    print(binarySearchRecursive(array, 86))
    print(binarySearchIterative(array, 6))
    print(binarySearchIterative(array, 86))