def getIntersectionNode(head1, head2):

    '''
    Thoughts: 
    
    Naive - For each node in LL1, we can compare with nodes in LL2. If any two nodes are the same, that will be the intersection node. O(N*M)
    
    Optimized Approach - we can have two runners running at equal pace.
                If one runner reaches the end, it can start again from the other runner's start
                This will set the pointer of one runner in the correct position and make it match the other runner,
                so that both of them reach the intersection node at the same time
                If the two lined lists never intersect, both the runners reach NONE at some time.
    
    '''
    
    '''
    Pseudocode:

    1. Have two runners. Make them point to the respective heads of the linkedlists
    2. While the two runners do not point to the same node, check:
    3.      If a runner has reached the end of the list, make it start again from the head of the other runner's list
    4.      Else, make the runners move to the next node.
    5. When both the runners point to the same node or None(if the lists dont intersect), return any one of the runner
    '''

    runner1 = head1
    runner2 = head2

    while(runner1 != runner2):
        if runner1:
            runner1 = runner1.next
        else:
            runner1 = head2
        
        if runner2:
            runner2 = runner2.next
        else:
            runner2 = head1
    
    return runner1

#O(N+M) - Linear time complexity - since each runner goes down each list in order to get lined up and then they go together to find the intersection.
#                                  In worst case, each runner goes through both the lists [O(2.N + 2.M)], if the intersection is at the end and lengths are not the same.
#                                  In best case, each runner goes through the respective list only once, if the lengths of the lists are equal. 
#O(1) - Constant space complexity - since the function does not use any additional data structure of size related to the input size.
