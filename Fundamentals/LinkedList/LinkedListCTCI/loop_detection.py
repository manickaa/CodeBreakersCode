#Similar to ../linked_list_cycle.py
#In this problem, we additionaly return the node at the beginning of the loop

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __str__(self):
        #O(N) time
        #O(N) space
        result = ""
        current = self
        while(current):
            result += str(current.value) + "|"
            current = current.next
        return result

def loopDetection(head):

    #Base case - If there are no nodes or only one node, it means there are no cycle
    if not head or not head.next:
        return None #No cycle found
    
    node = head
    nodeSet = set()
    while(node):
        if node in nodeSet:
            return node
        nodeSet.add(node)
        node = node.next
    return None

#O(N) - Linear time
#O(1) - Constant space
#We use only two pointers here