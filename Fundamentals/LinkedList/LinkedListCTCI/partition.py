'''
Input 3->5->8->5->10->2->1 partition=5
Output 3->1->2->10->5->5->8  
'''

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

def partition(head, p):
    
    if not head or not p:
        return head
    
    current = head

    left = Node('head')
    ptr1 = left
    right = Node('head')
    ptr2 = right

    while(current):
        newNode = Node(current.value)
        if(current.value < p):
            ptr1.next = newNode
            ptr1 = ptr1.next
        else:
            ptr2.next = newNode
            ptr2 = ptr2.next
        current = current.next
    
    ptr2.next = None
    ptr1.next = right.next

    return left.next

#O(n) - linear time complexity - goes through all the nodes exactly once
#O(n) - Linear space complexity - creates two linkedlists whose combined size is equal to the original size of the linked list

if __name__ == '__main__':
    
    head = Node('Head')
    current = head
    
    for i in range(5):
        current.next = Node(i)
        current = current.next
    
    current.next = Node(0)
    print(head.next) #0|1|2|3|4|0
    head = partition(head.next, 3)
    print(head) #0|1|2|0|3|4|