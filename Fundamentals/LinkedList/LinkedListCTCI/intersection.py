#O(N+M) - Linear time complexity - since each runner goes down each list in order to get lined up and then they go together to find the intersection.
#                                  In worst case, each runner goes through each list twice fully(if the intersection is at the end and lengths are not the same)
#O(1) - Constant space complexity

def intersection(head1, head2):

    '''
    Thoughts: 
    
    Naive - For each node in LL1, we can compare with nodes in LL2. If any two nodes are equal, that will be the intersection node. O(N*M)

    Approach 2 - we can add each node in LL1 in a set and go through each node in LL2 and check if it is in the set. If true, we found the intersection node 
                Time - O(N+M) Space - O(N)
    
    Approach 3 - we can have two runners runnig at equal pace.
                If one runner reaches the end, it can start again from the other runner's start
                This will make one of the runner match the difference in lengths of the list by letting it run from the longest list and make the runners meet at the intersection again
                If the two lined lists never intersect, both the runners reach NONE at some time.
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
