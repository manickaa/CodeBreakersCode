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
        
        '''
        Thoughts:

        To know if a given list is a palindrome, the first half of the list must be reverse order to match the second half of the list.
        We can have two runner, slow and fast, fast running at twice the speed of the slow.
        Both start at head and by the time fast reaches the end, slow is at the middle.
        We can put the nodes passed by slow in a stack.
        And compare the remaining nodes with the top value of the top. If it matches, pop it out, check the next node.
        If not, return False, since it is not a palindrome

        Pseudocode:
        
        #Base case: If there are no nodes, or only one node, then the linked list already a palindrome. Return true

        1. Point slow and fast, both to head
        2. Move slow by one step and fast by two steps till the fast reaches the end. Simultaneously add slow's value to the stack
        3. If the fast is currently NOT pointing at None, then the length is odd.
        4. Move the slow by one step to skip the middle element
        5. Move slow step by step until reaches the end. Compare the slow's value and stack's topmost by popping the stack.
        6.      If equal, continue
        7.      Else, return False, since it is not a palindrome
        8. Return True, if slow reaches end and everything matches
        '''
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

#Time complexity - O(N) - since we are moving through the linked list only once
#Space complexity - O(N//2) - O(N) - since we are storing node values of half of the linked list to compare with other half

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