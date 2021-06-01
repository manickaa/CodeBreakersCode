class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeKthLast(head, k):

    '''
    Thoughts:

    The naive solution would be to find the length of the linked list (N). Then calculate
    the index of the to be removed.
    Again pass through the linked list to remove the node at the index found.
    This will take two passes through the linked list. O(N + N-K) => O(N)
    
    Optimized solution with one pass:

    We dont know the total length. Let it be N
    We can have two runner, starting at position 0 (head).
    First, we can move the fast runner ahead by k steps, so that position of the runner is k.
    In order for the fast runner to reach the end, it has to take N-k steps.
    Now, we move both the slow and fast runners at equal speed till the fast runner reaches the end
    When the fast reaches end, the position of the slow will be at N-k, which is the node to be removed.

    '''
    '''
    Pseudocode:

    1. Create a dummy node, in case the head needs to be removed
    2. Dummy's next will point to head
    3. Point slow and fast to dummy
    4. Move fast by k steps
    5. Move fast and slow till fast's next is the end
    6. Slow's next is the node to be removed. Remove slow's next
    7. Return dummy's next
    '''

    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    
    for i in range(0, k):
        fast = fast.next
    
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next
    
    slow.next = None if not slow.next else slow.next.next
    return dummy.next

#Time complexity - We go through the linked list only once. If there are N nodes in the linked list,
#                  the runtime is O(N).
#Space complexity - No additional space, whose size depends on input size is used.
#                   O(1)