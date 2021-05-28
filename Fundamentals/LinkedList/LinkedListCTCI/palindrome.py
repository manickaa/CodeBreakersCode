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

def isPalindrome(head):
        
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        
        stack = []
        
        while(fast and fast.next):
            stack.append(slow.value)
            slow = slow.next
            fast = fast.next.next
        
        if(fast is not None): #length of lined list is odd
            slow = slow.next #skip the middle element since it cannot be matched with another in stack
            
        while(slow):
            topStackVal = stack.pop()
            if(topStackVal != slow.value):
                return False
            slow = slow.next
        
        return True

if __name__ == '__main__':
    
    head = Node(1)
    current = head
    
    for i in range(2, 4):
        current.next = Node(i)
        current = current.next
    for i in range(4, 0, -1):
        current.next = Node(i)
        current = current.next
    print(head) #1|2|3|4|3|2|1
    print(isPalindrome(head)) #True