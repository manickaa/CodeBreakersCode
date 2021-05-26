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

def reverseLinkedList(head):
    current = head
    prev = None

    while(current):
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

head = Node('Head')
current = head
for i in range(10):
    current.next = Node(i)
    current = current.next
print(head.next) #0|1|2|3|4|5|6|7|8|9|
head.next = reverseLinkedList(head.next)
print(head.next) #9|8|7|6|5|4|3|2|1|0|

#O(n) - linear time complexity - go through all the nodes exactly once and reverses the pointers
#O(1) - constant space complexity