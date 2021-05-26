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


def detectCycle(head):
    
    #1->2-> 3
    #   ^   |
    #   |   |
    #   `---

    #Base case - If there are no nodes or only one node, it means there are no cycle
    if not head or not head.next:
        return False
    slow = head
    fast = head.next

    while(slow and fast and fast.next):
        if(slow == fast): #Point to the same node
            return True
        slow = slow.next
        fast = fast.next.next
    return False


#O(N) - Linear time
#   Explanation:
#   When there is no cycle, each node is traversed exactly once - O(N)
#   When there is a cycle, the slow pointer goes through all the nodes that are not in the cycle N (non-cyclic length)
#                          the fast pointer goes (distance between two pointers / difference of speed) loops in order to catch up with slow pointer - K (cyclic length)
#                           O(N+K) => O(N)


#O(1) - Constant space
#We use only two pointers here