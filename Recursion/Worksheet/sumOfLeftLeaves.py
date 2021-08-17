#O(N) time
#O(N) space

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        return self.recurse(root, False)
    
    def recurse(self, node, isLeftSubTree):
        if not node:
            return 0
        if not node.left and not node.right:
            if isLeftSubTree:
                return node.val
        
        total = 0
        total += self.recurse(node.left, True)
        total += self.recurse(node.right, False)
        return total

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.sumOfLeftLeaves(root))
    root = TreeNode(1)
    print(sol.sumOfLeftLeaves(root))