
class Node:

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
        
class MyHashMap:

    '''
    Let N be the number of keys, K be the original capacity, M is the extra nodes added as a linked list 

    Time complexity : In worst case, we iterate through all the nodes in a map's index 
                       So, O(N/K)
    Space complexity : In worst case, there will be M more space needed to add the key-value pairs as node.
                        So, O(K + M)
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1000
        self.map = []
        
        for _ in range(self.capacity):
            self.map.append(Node('Dummy', 'Dummy'))

    def _hash(self, key):
        """
        Helper function to get the key's index in the array
        It also returns the prevNode of the current key's node.
        Getting the prevNode makes it easy to remove/add a node
        """
        
        index = key % self.capacity
        
        prevNode = self.map[index]
        current = prevNode.next
        
        while current:
            if current.key == key:
                return True, prevNode
            
            current = current.next
            prevNode = prevNode.next
        return False, prevNode
        
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        keyExists, prevNode = self._hash(key)
        if keyExists:
            #Given key's node is prevNode's next
            prevNode.next.value = value
        else:
            #prevNode is the last node
            #create a new node(key-value) pair and point the prev's next to new node
            prevNode.next = Node(key, value)
        
            

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
        keyExists, prevNode = self._hash(key)
        if keyExists:
            #Given key's node is prevNode's next
            return prevNode.next.value
        else:
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        
        keyExists, prevNode = self._hash(key)
        if keyExists:
            #Given key's node to be removed is prevNode's next
            prevNode.next = prevNode.next.next