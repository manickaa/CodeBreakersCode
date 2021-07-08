from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:       
    def insertionSortList(self, head):
        dummy = ListNode()
        curr = head
        while(curr is not None):
            prev = dummy
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next
            next = curr.next
            #insert curr between prev and next
            curr.next = prev.next
            prev.next = curr
            #increment curr
            curr = next
        return dummy.next
    
if __name__ == '__main__':
    solution = Solution()
    head = ListNode(4)
    curr = head
    for i in range(0, 5):
        newNode = ListNode(i)
        curr.next = newNode
        curr = newNode
    
    
    resultHead = solution.insertionSortList(head)
    curr = resultHead
    while curr:
        print(curr.val)
        curr = curr.next
    

    
    