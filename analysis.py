#Exponential - O(2^N)

def subsets(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        return  [[nums[0]] + x for x in subsets(nums[1:])] + [x for x in subsets(nums[1:])]
'''
# Block (a)
sum = 0;
n = N
while n > 0: 
    for i in range(0, n):
        sum += 1;
    n = n // 2



# Block (b)
sum = 0
i = 1
while i < N:
    for j in range(0, i):
        sum += 1
    i = i * 2



# Block (c)
sum = 0
i = 1
while i < N:
    for j in range(0, N):
        sum += 1
    i = i * 2
'''
if __name__ == "__main__":
        all_subsets = subsets(range(0,5))
        print(all_subsets)
        for subset in all_subsets:
            print(subset)