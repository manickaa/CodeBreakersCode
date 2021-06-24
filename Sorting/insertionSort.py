def insertionSort(nums):
    #O(N^2) worst and average case runtime
    #O(1) space
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break
    
    print(nums)
    return

if __name__ == '__main__':
    nums = [10,9,8,7,6,5,4,3,2,1]   #worst case #O(N^2)
    insertionSort(nums)
    nums = [0,15,2,8,3,4,9,4,6,2,1] #average case #O(N^2)
    insertionSort(nums)
    nums = [1,2,3,4,5,6,7,8,9,10]   #best case #O(N)
    insertionSort(nums)