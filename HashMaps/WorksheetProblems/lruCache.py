class Node:
    #initialize Node
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    
    '''
    Time complexity for put() and get() - Constant time O(1)
    Space complexity: O(capacity) - which is the maximum size of the cache
    '''
    def __init__(self, capacity) -> None:
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        self.cache = {}

    def _add(self, node):
        #node: 1
        #head<->tail
        #head<->1<->tail
        #node: 2
        #head<->2<->1<->tail
        nextToHead = self.head.next
        #update head's next's prev to point to given node
        nextToHead.prev = node
        #update head's next to point to given node
        self.head.next = node
        #update next and prev of given node
        node.next = nextToHead
        node.prev = self.head
        return
    
    def _remove(self, node):
        
        #node: 2
        #head<->1<->2<->3<->tail
        #head<->1<->3<->tail

        #get prev of node
        prevNode = node.prev
        #get next of node
        nextNode = node.next
        #prevNode's next will be nextNode
        prevNode.next = nextNode
        #nextNode's prev will be prevNode
        nextNode.prev = prevNode
        return

    def _move_to_front(self, node):
        
        self._remove(node) #remove from its position
        self._add(node) #adds to the front, next to head
        return
    
    def get(self, key):
        #if key in cache
        if key in self.cache:
            #get the node
            curNode = self.cache[key]
            #move it to front
            self._move_to_front(curNode)
            #return node's value
            return curNode.value
        #else, return -1
        return -1

    def put(self, key, value):
        #if key in cache
        if key in self.cache:
            #get the node
            curNode = self.cache[key]
            #change the node's value with the given value
            curNode.value = value
            #move it to front
            self._move_to_front(curNode)
            return
        #else
        else:
            #create a new node with key and value
            newNode = Node(key, value)
            #Add it to cache
            self.cache[key] = newNode
            #Add the new node to the front of the linkedlist
            self._add(newNode) #adds to front
            #Increment size
            self.size += 1
            #If size exceeds capacity
            if self.size > self.capacity:
                #Pop a node from last
                nodeToBeDeleted = self.tail.prev
                self._remove(nodeToBeDeleted)
                #delete from cache
                del self.cache[nodeToBeDeleted.key]
                self.size -= 1
            return
    
    def asList(self):
        result = []
        cur = self.head.next
        while(cur.next):
            result.append((cur.key, cur.value))
            cur = cur.next
        return result

if __name__ == "__main__":
    lruCache = LRUCache(10)
    for i in range(1,6):
        lruCache.put(i, i)
    print(lruCache.asList()) #[(5,5),(4,4),(3,3),(2,2),(1,1)]
    
    print(lruCache.get(5)) #5
    print(lruCache.get(3)) #3
    print(lruCache.get(8)) #-1

    for i in range(6, 11):
        lruCache.put(i,i)
    print(lruCache.asList())  #[(10, 10), (9, 9), (8, 8), (7, 7), (6, 6), (3, 3), (5, 5), (4, 4), (2, 2), (1, 1)]

    lruCache.put(11, 11)
    print(lruCache.asList()) #[(11,11), (10, 10), (9, 9), (8, 8), (7, 7), (6, 6), (3, 3), (5, 5), (4, 4), (2, 2)]     