'''
Given an array of integers and a target, find a subarray that sums up to the target.
Return the start and end indices of the array (end index exclusive)

Eg: 
nums = [1,-20,-3,30,5,4]
target = 7

output = (1,4) ,which is [-20,-3,30] the end index num is excluded here

Contains only one unique solution
'''

def subArraySum(array, k):
    
    prefix_sum = {}
    curr_sum = 0

    for i in range(0, len(array)):
        
        curr_sum += array[i]
        complement = curr_sum - k
        if complement in prefix_sum:
            return (prefix_sum[complement]+1, i+1)
        prefix_sum[curr_sum] = i
    
    return (None, None)


if __name__ == '__main__':
    nums = [1,-20,-3,30,5,4]
    target = 7
    print(subArraySum(nums, target))
    print(subArraySum([1,3,-3,8,5,7], 5))