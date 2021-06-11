#find the maximum sum of two numbers in the array

#Input: [-4,1,2,5,-6,7] 
#Output: 12

#Can use greedy approach here
#since the sum of largest two numbers will be the maximum sum of two numbers in the array


def maxSum(arr):

    #O(N) time
    #O(2) => O(1) space

    maxSumArray = []    #to hold the largest two numbers
    for num in arr:
        maxSumArray.append(num)
        maxSumArray.sort(reverse=True)
        if len(maxSumArray) > 2:
            maxSumArray.pop()
    return maxSumArray[0] + maxSumArray[1]


arr = [-4,1,2,5,-6,7]
print(maxSum(arr)) #12