#   Delete a node in the middle(any node except the first and last) of the linked list
#   Given only access to that particular node

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

def deleteNode(node):
    
    if not node or not node.next:   #in this method, we cannot delete a node at the end. Assume, the given node is not the first or the last node
        return None

    newNode = node.next #copy the next node

    node.value = newNode.value #assign the value of the current node with next node's value
    node.next = newNode.next #assign the ptr of the current node with the next node's ptr

    #This deletes the connection with the next node

    return True

#Given the node, we are just copying the next node's details to the given node and deleting the next node
#O(1) - Both time and space

if __name__ == '__main__':
    
    head = Node('Head')
    current = head
    nodeToBeDeleted = None
    
    for i in range(5):
        current.next = Node(i)
        if i==3:
            nodeToBeDeleted = current.next
        current = current.next
    
    print(head.next) #0|1|2|3|4|
    print(nodeToBeDeleted.value) #3
    
    deleteNode(nodeToBeDeleted) #0|1|2|4|
    print(head.next)





