# Given n non-negative integers a_1, a_2, ..., a_n and a target k, count the number of contiguous subarrays that are less than k. 

# Example:
#   Input: nums = [1,2,3,2,1], k = 3
#   Output: 7
#   Explanation: The 8 subarrays that have sum less than 3 are: [1], [2], [3], [2], [1], [1,2], [2,1]

def numOfSubArraysLessThanK(nums, k):
    
    #O(2N) => O(N) runtime
    # O(1) space 

    #base case:
    if(len(nums) == 0):
        return 0

    count = 0
    total_sum = 0
    start = -1

    #i represents the end point in the sliding window
    for i in range(len(nums)):
        total_sum += nums[i]
        while(total_sum > k):
            start += 1
            total_sum -= nums[start]
        count += i-start
    return count

nums = [1,2,3,2,1]
print(numOfSubArraysLessThanK(nums, 3))
nums = [1,2,3,0,3]
print(numOfSubArraysLessThanK(nums, 3))