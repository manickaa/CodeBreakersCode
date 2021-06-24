
def selectionSort(nums):
    #O(N^2) runtime
    #O(1) space
    sum = 0
    for i in range(0, len(nums)):
        currentNumber = nums[i]
        swapIndex = i
        for j in range(i+1, len(nums)):
            sum += 1
            if nums[j] < currentNumber:
                currentNumber = nums[j]
                swapIndex = j
        #swap the element at index i with element at swapIndex
        nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
    print(sum)
    print(nums)
    return

if __name__ == '__main__':
    nums = [10,9,8,7,6,5,4,3,2,1]
    selectionSort(nums)
    nums = [0,15,2,8,3,4,9,4,6,2,1]
    selectionSort(nums)
    nums = [1,2,3,4,5,6,7,8,9,10]
    selectionSort(nums)
        