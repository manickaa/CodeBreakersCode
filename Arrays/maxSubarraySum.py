
#Input: [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#        [4,-1,2,1] has the maximum sum

def maxSubarraySum(arr):

    #O(N) time
    #O(1) space

    maxSum = float('-inf')
    maxEndingHere = 0

    for i, num in enumerate(arr):
        maxEndingHere += num
        if(maxSum < maxEndingHere):
            maxSum = maxEndingHere
        if(maxEndingHere < 0):
            maxEndingHere = 0
    return maxSum


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarraySum(arr))
