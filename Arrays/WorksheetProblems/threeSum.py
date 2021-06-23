# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

#O(N^2) runtime
#O(N) space

def threeSum(self, nums):
    result = []
    nums.sort()
    for i in range(0, len(nums)):
        if nums[i] > 0:
            break
        #to avoid duplicates
        if i == 0 or nums[i-1] != nums[i]:
            self.twoSum(nums, i, result)
    return result

def twoSum(self, nums, index, result):
    hashSet = set()
    j = index + 1
    while j < len(nums):
        complement = -nums[index] -nums[j]  #x+y+z = 0 => x= -y-z
        if complement in hashSet:
            result.append([complement, nums[index], nums[j]])
            #to avoid duplicates:
            while(j+1 < len(nums) and nums[j] == nums[j+1]):
                j += 1
        hashSet.add(nums[j])
        j += 1