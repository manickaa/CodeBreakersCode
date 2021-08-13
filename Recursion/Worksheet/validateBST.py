class Node:
    def __init__(self, val=0, left=None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #O(N) time, since all nodes are checked for validity
    #O(N) space for recursion stack
    def isValidBST(self, root) -> bool:
        
        def validate(root, minVal, maxVal):
            if not root:
                return True
            if root.val <= minVal or root.val >= maxVal:
                return False
            return validate(root.left, minVal, root.val) and validate(root.right, root.val, maxVal)
        
        minVal = float('-inf')
        maxVal = float('+inf')
        return validate(root, minVal, maxVal)

if __name__ == '__main__':
    root = Node()
    root.val = 2
    root.left = Node(1)
    root.right = Node(3)

    soln = Solution()
    print(soln.isValidBST(root))

    root = Node(5)
    root.left = Node(1)
    root.right = Node(4, Node(3), Node(6))

    print(soln.isValidBST(root))
