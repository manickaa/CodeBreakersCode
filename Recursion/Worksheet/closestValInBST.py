class Node:
    def __init__(self, val=0, left=None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValInBST(self, root, target):
        def helper(node, gap):
            if not node:
                return
            currentGap = abs(target - node.val)
            if currentGap < gap:
                self.closestVal = node.val
                gap = currentGap
                
            if node.val > target:
                helper(node.left, gap)
            else:
                helper(node.right, gap)
        
        self.closestVal = root.val
        helper(root, float('inf'))
        return self.closestVal

if __name__ == '__main__':
    soln = Solution()
    root = Node(4, Node(2, Node(1), Node(3)), Node(5))
    target = 3.714286
    print(soln.closestValInBST(root, target))
    root = Node(1)
    print(soln.closestValInBST(root, target))