class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        return self.recurse(p, q)
    
    def recurse(self, p, q):
        if (p and not q) or (q and not p):
            return False
        if not p and not q:
            return True
        if p and q and p.val != q.val:
            return False
        
        return self.recurse(p.left, q.left) and self.recurse(p.right, q.right)

if __name__ == '__main__':
    soln = Solution()
    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    root2 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    print(soln.isSameTree(root1, root2))
    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    root2 = TreeNode(4, TreeNode(2, None, TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    print(soln.isSameTree(root1, root2))