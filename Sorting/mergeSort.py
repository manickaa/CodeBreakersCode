def mergeSort(arr):

    #O(N logN) time
    #O(N) space - recursion stack space and space for the copy array

    divide(arr, 0, len(arr)-1)

def divide(arr, lo, hi):
    if lo >= hi:
        return
    
    mid = (lo+hi)//2 + 1

    #divide first half
    divide(arr, lo, mid-1)
    #divide second half
    divide(arr, mid, hi)
    #merge in sorted order
    merge(arr, lo, mid, hi)


def merge(arr, start1, start2, end2):

    p1 = start1
    p2 = start2
    current = start1
    copyArr = arr[:]

    while(current <= end2):
        if p1 < start2 and p2 <= end2:
            if copyArr[p1] < copyArr[p2]:
                arr[current] = copyArr[p1]
                p1 += 1
            else:
                arr[current] = copyArr[p2]
                p2 += 1
        elif p1 < start2:
            arr[current] = copyArr[p1]
            p1 += 1
        else:
            arr[current] = copyArr[p2]
            p2 += 1

        current += 1

if __name__ == '__main__':
    arr = [7,10,9,5,1,4,3,6,2,8]
    mergeSort(arr)
    print(arr)