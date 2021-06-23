# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

# Return k after placing the final result in the first k slots of nums.
def removeDuplicates(self, nums) -> int:
    #O(N) time
    #O(1) space
    start = 0
    for end in range(1, len(nums)):
        if nums[end] != nums[start]:
            start += 1
            nums[start] = nums[end]
    return start+1
    