class Solution:
    def subsets(self, nums):
        
        #O(N*2^N) to generate all subsets and copy to output - time
        #O(N) curr at most store N numbers  - space
        def backtrack(first, curr):
            #if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                #add nums[i] to the current combo
                curr.append(nums[i])
                #backtrack to see if the combo is done or need to add more
                backtrack(i+1, curr)
                #once done, we pop out the element(nums[i]) to see if next number fits the combo        
                #backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n+1):
            backtrack(0,[])
        return output

if __name__ == '__main__':
    soln = Solution()
    print(soln.subsets([1,2,3]))
    print(soln.subsets([0]))
    print(soln.subsets([]))