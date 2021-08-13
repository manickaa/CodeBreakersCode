
#Time complexity - O(N)
#Space complexity - N + N = O(N) (recursion stack space and dict space)
def twoSum(nums, target: int):
    numDict = {}
    return helper(nums, target, numDict, 0)

def helper(nums, target, memo, i):
    if i < len(nums):
        if target-nums[i] in memo:
            return [memo[target-nums[i]], i]
        memo[nums[i]] = i
        i += 1
        return helper(nums, target, memo, i)

if __name__ == '__main__':
    print(twoSum([2,7,11,15], 9))
    print(twoSum([3,3], 6))
    print(twoSum([1,2,3,4], 4))
    print(twoSum([3,3], 10))