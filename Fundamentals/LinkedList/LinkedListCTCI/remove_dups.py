
#Input      1->2->1->8->10->None
#Output     1->2->8->10->None

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

def removeDuplicates(head):
    
    if not head or not head.next:
        return head
    
    nodeSet = set()

    prev = None
    current = head

    while(current):
    
        nextCurrent = current.next
        
        if(current.value not in nodeSet):
            nodeSet.add(current.value)
            prev = current
        else:
            prev.next = nextCurrent
        
        current = nextCurrent
    
    return head

#O(N) - runtime complexity - Each node is traversed once to check for duplicates
#O(N) - space complexity - If there are no duplicates, all the node values will be in the set

if __name__ == '__main__':
    linkedList = LinkedList()
    for i in range(1, 6):
        linkedList.insertFront(i)
    print(linkedList) #5|4|3|2|1| #invokes __str__ method
    linkedList.insertAtPosition(1, 4)
    linkedList.insertAtPosition(4, 1)
    print(linkedList) #4|5|4|1|3|2|1|
    linkedList.head.next = removeDuplicates(linkedList.head.next)
    print(linkedList)  #4|5|1|3|2

    linkedList = LinkedList()
    for i in range(5):
        linkedList.insertFront(2)
    print(linkedList) #2|2|2|2|2|
    linkedList.head.next = removeDuplicates(linkedList.head.next)
    print(linkedList) #2