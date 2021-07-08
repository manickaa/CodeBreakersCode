class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # quick sort algorithm
        # return self.quicksort(nums, 0, len(nums)-1)
    
    # def quicksort(self, nums, lo, hi):
    #     if lo >= hi:
    #         return
    #     pivot = self.partition(nums, lo, hi)
    #     self.quicksort(nums, lo, pivot-1)
    #     self.quicksort(nums, pivot+1, hi)
    
    # def partition(self, nums, lo, hi):
    #     pivot = nums[lo]
    #     swapIndex = lo + 1
    #     for i in range(lo+1, hi+1):
    #         if nums[i] < pivot:
    #             nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
    #             swapIndex += 1
    #     nums[lo], nums[swapIndex-1] = nums[swapIndex-1], nums[lo]
    #     return swapIndex-1
    
        # #two pass algorithm
        # numofzero = numofone = numoftwo = 0
        # for num in nums:
        #     if num == 0:
        #         numofzero += 1
        #     elif num == 1:
        #         numofone += 1
        #     else:
        #         numoftwo += 1
        # nums[:] = [0] * numofzero + [1] * numofone + [2] * numoftwo
        # return nums
        
        #One pass algorithm Dutch national flag
        p1 = 0
        p2 = len(nums)-1
        curr = 0
        
        while(curr <= p2):
            if nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            elif nums[curr] == 0:
                nums[curr], nums[p1] = nums[p1], nums[curr]
                p1 += 1
                curr += 1
            else:
                curr += 1
        return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [2,2,0,0,1,1]
    print(solution.sortColors(nums))
    