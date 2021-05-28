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

def sumLists(head1, head2):

    if not head1 and not head2:
        return None
    
    carry = 0
    
    newList = Node('dummy')
    current = newList

    while(head1 or head2):
        
        sum = carry
        if head1:
            sum += head1.value
        if head2:
            sum += head2.value

        resultVal = sum % 10
        
        newNode = Node(resultVal)

        if sum >= 10:
            carry = 1
        else:
            carry = 0

        current.next = newNode
        current = current.next

        head1 = None if not head1 else head1.next
        head2 = None if not head2 else head2.next

    if carry!= 0:
        newNode = Node(carry)
        current.next = newNode
    return newList.next

'''
Let N be the maximum of lengths of linkedlist1 and linkedlist2

Time: O(N)
Space: O(N) since we create a new linked list with the sum

'''

if __name__ == '__main__':

    head1 = Node(1)
    current = head1
    for i in range(2, 5):
        current.next = Node(i)
        current = current.next
    print(head1) #1|2|3|4|
    head2 = Node(1)
    current = head2
    for i in range(5, 10):
        current.next = Node(i)
        current = current.next
    print(head2) #1|5|6|7|8|9|
    head = sumLists(head1, head2)
    print(head) #2|7|9|1|9|9