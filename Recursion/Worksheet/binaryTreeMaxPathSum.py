# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # the maxsum will either be the sum of left subtree or sum of right subtree or 
    # node.val + sum of left subtree + sub of right subtree or
    # node.val + sum of left subtree or right subtree
    
    #initially max sum can be 0.
    #if there is no root, return 0
    
    #go to left, calculate the max sum. This will be left subtree sum
    #go to right, calculate the max sum. This will be right subtree sum
    
    #total path sum = node.val + left subtree sum + right subtree sum
    #max sum will be the max of max sum and total path sum
    
    #what should we return?
    #return max(node.val + max(left sum, right sum), 0)
    #For eg: 10
    #       -5  5
    
    #   For node(-5) ->left sum = 0, right sum =0 If we return 0+0-5=-5, it means that -5 is included in the path. This will reduce the path sum (-5+10+5 = 10) to be lower than that if we exclude -5(ie. 10+5= 15). So, we take the max of the calculation and 0.
    
    #why are we taking max(left sum, right sum) -> While going bottom up, we calculate the node.val+left+right to get the max sum. But for traversing up, we cannot choose both the left and right, which would make the path invalid. 
    
    #For eg:
    #           10
    #          /   \
    #       5       -10
    #.    /   \     /  \
    #   -5      1 50    20
    
    #10 -> -10 -> 50 -> 20  ===> Invalid path.
    #To include node 10, the node(-10) must include either 50 or 20 but not both.
    #Refer https://youtu.be/6cA_NDtpyz8
    
    def maxPathSum(self, root) -> int:
        
        self.maxSum = float('-inf')
        self.helper(root)
        return self.maxSum
    
    def helper(self, node):
        if not node:
            return 0
        left_sum = self.helper(node.left)
        right_sum = self.helper(node.right)
        
        path_sum = node.val + left_sum + right_sum
        self.maxSum = max(self.maxSum, path_sum)
        
        return max(node.val + max(left_sum, right_sum), 0)


if __name__ == '__main__':
    soln = Solution()
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(soln.maxPathSum(root))