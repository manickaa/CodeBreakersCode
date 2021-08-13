class Solution:
    def searchRange(self, nums, target: int):
        lower_bound = self.findTarget(nums, target, True)
        if lower_bound == -1:
            return [-1,-1]
        upper_bound = self.findTarget(nums, target, False)
        return [lower_bound, upper_bound]
    
    def findTarget(self, nums, target, isFirst):
        
        start = 0
        end = len(nums)-1
        while(start <= end):
            mid = (start+end)//2
            if nums[mid] == target:
                if isFirst:
                    #check if we have the same number on the left
                    if mid == start or nums[mid-1] < target:
                        return mid
                    else:
                        end = mid-1
                else:
                    if mid==end or nums[mid+1] > target:
                        return mid
                    else:
                        start = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return -1
            
if __name__ == '__main__':
    soln = Solution()
    print(soln.searchRange([5,7,7,8,8,10], 8))
    print(soln.searchRange([8], 8))
    print(soln.searchRange([5,7,7,8,8,20],10))
    print(soln.searchRange([],0))