#Given an array of numbers, count the number of subarrays whose product is strictly less than k

def numSubarrayProductLessThanK(self, nums, k: int) -> int:
    #O(N) runtime
    #O(1) space
    if k ==0 or k==1:
        return 0
    start = -1
    product = 1
    count = 0
    for i in range(0, len(nums)):
        product *= nums[i]
        while product >= k:
            start += 1
            product /= nums[start]
        count += i-start 
    return count