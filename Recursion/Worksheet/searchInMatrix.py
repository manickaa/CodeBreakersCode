class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        #O(log(MN)) time
        #O(1) space
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n -1
        
        while(start <= end):
            mid = (start + end) // 2
            
            row = (mid) // n
            col = (mid) % n
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

if __name__ == '__main__':
    soln = Solution()
    print(soln.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
    print(soln.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
    