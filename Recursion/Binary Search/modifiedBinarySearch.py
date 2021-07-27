#given array is rotated with a particular index, which is not given
#Eg: array = [4,5,6,8,0,1,2]
#Search for a target using binary search. Time complexity must be O(logN)

def modifiedBinarySearch(rotatedArray, target):
    #O(log N) runtime
    #O(1) space
    if not rotatedArray:        #[4,5,6,8,0,1,2]    #target:6
        return -1
    lo = 0                      #0    #0    #2
    hi = len(rotatedArray)-1    #6     #2   #2

    while lo <= hi:
        mid = (hi+lo)//2        #3      #1      #2
                #element at mid #8      #5      #6
        #if the mid element is the target, then done
        if target == rotatedArray[mid]:     #6==6
            return mid                      #returns 2
        #if the mid element is one of the pivoted element
        if rotatedArray[lo] > rotatedArray[mid]:    #4>8 No   4>5 No
            #If the target is greater than lo or less than mid
            if target >= rotatedArray[lo] or target <= rotatedArray[mid]:
                hi = mid-1
            #else
            else:
                lo = mid+1
        #if the mid element is not a pivoted element
        else:                                   
            #If the target is between lo and mid 
            if rotatedArray[lo] <= target < rotatedArray[mid]:  #6 is between 4 and 8 Yes   #6 between 4 and 5 No
                hi = mid-1                                      #hi = 2     #lo=2
            #else
            else:
                lo = mid+1
    return -1
if __name__ == '__main__':
    array = [4,5,6,8,0,1,2]
    print(modifiedBinarySearch(array, 0)) #should return 4
