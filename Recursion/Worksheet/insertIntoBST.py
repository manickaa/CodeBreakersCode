class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #O(H) time
    #O(H) space
    def insertIntoBST(self, root, val: int):
        root = self.recurse(root, val)
        return root
    
    def recurse(self, node, val):
        if not node:
            return TreeNode(val)
        if node.val > val:
            node.left = self.recurse(node.left, val)
        if node.val < val:
            node.right = self.recurse(node.right, val)
        return node

if __name__ == '__main__':
    soln = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    result = soln.insertIntoBST(root, 25)
    print(result)