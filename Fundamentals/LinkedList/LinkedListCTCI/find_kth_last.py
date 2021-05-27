class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = Node("Dummy")
        self._size = 0
    
    def __str__(self):
        #O(N) time
        #O(N) space
        result = ""
        current = self.head.next
        while(current):
            result += str(current.value) + "|"
            current = current.next
        return result
    
    def insertFront(self, val):
        #O(1) time
        #O(1) space
        node = Node(val)
        nodes_next = self.head.next
        self.head.next = node
        node.next = nodes_next
        self._size += 1
    
    def insertLast(self, val):
        #O(n) time
        #O(1) space
        current = self.head
        while(current.next is not None):
            current = current.next
        node = Node(val)
        current.next = node
        self._size += 1
    
    def insertAtPosition(self, pos, val):
        #O(n) time
        #O(1) space
        #H->1->2->3 pos = 2 val = 4
        #H->1->4->2->3
        current = self.head
        currentPos = 0
        while(current):
            currentPos += 1
            if(currentPos) == pos:
                newNodesNext = current.next
                newNode = Node(val)
                current.next = newNode
                newNode.next = newNodesNext
                self._size += 1
                return
            current = current.next
        return
            
    def removeBeginning(self):
        #O(1) time
        #O(1) space
        assert(self.size() > 0)
        self.head.next = self.head.next.next
        self._size -= 1
    
    def size(self):
        return self._size

def findKthToLast(head, k):
    
    #start both the runners from head
    slow = head
    fast = head

    #move fast ahead of slow by K steps
    for i in range(0, k):
        if(fast is None):
            return None
        fast = fast.next
    
    #By now, fast is already 'K'steps ahead. 
    #If we move fast 'Length-K' more steps while moving slow simulatenously,
    #Slow will be at 'Length-K' nodes from the start or K nodes from the end
    #return slow        

    while(fast):
        fast = fast.next
        slow = slow.next
    
    return slow

#O(N) - Time complexity -O(K+N-K) - O(N) - where N be the length of the linked list
#(1) - Constant space complexity

if __name__ == '__main__':
    linkedList = LinkedList()
    for i in range(1, 6):
        linkedList.insertFront(i)
    print(linkedList) #5|4|3|2|1| #invokes __str__ method
    print(findKthToLast(linkedList.head.next, 4).value) #4
    print(findKthToLast(linkedList.head.next, 1).value) #1
    print(findKthToLast(linkedList.head.next, 10)) #None
    print(linkedList) #4|5|4|1|3|2|1|