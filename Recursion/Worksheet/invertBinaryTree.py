class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        root = self.recurse(root)
        return root
    
    def recurse(self, root):
        if not root:
            return None
        left = self.recurse(root.left)
        right = self.recurse(root.right)
        root.left = right
        root.right = left
        return root

if __name__ == '__main__':
    soln = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    print(soln.invertTree(root))