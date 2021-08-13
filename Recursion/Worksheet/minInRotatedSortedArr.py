class Solution:
    def findMin(self, nums) -> int:
        start = 0
        end = len(nums)-1
        minElement = None
        while(start <= end):
            mid = (start+end)//2
            if(mid == end):
                minElement = nums[end]
                return minElement
            if(nums[mid] < nums[end]):
                end = mid
            else:
                start = mid+1
        return minElement

if __name__ == '__main__':
    soln = Solution()
    print(soln.findMin([5,6,7,8,9,0,1,2]))
    print(soln.findMin([5,1,2,3,4]))
    print(soln.findMin([11,13,15,17]))
    print(soln.findMin([4,5,6,7,0,1,2]))