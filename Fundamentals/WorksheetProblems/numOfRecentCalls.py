#Node class
class Node:
    #initialize node with given value and next pointer to none
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

#Queue class
class Queue:
    #initialize a queue
    def __init__(self):
        #O(1) time and space
        self.size = 0       #initial size is 0
        self.head = Node('Dummy') #Create a dummy node.
        self.tail = self.head   #Point the head and tail to dummy node
    
    #returns the size of the queue
    def getSize(self): 
        #O(1) time and space 
        return self.size
    
    #returns true is the queue is empty
    def isEmpty(self):
        #O(1) time and space
        return self.getSize() == 0
    
    #adds an item to the queue
    def enqueue(self, value):
        #O(1) time and space
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1
    
    # removes and returns the least recently added item
    def dequeue(self):
        #O(1) time and space
        if self.isEmpty():
            print('Cannot remove from empty queue')
        out = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        if self.isEmpty():
            self.tail = self.head
        return out.val
    
    #returns a list of items in the queue
    def items(self):
        #O(N) time and space
        output = []
        cur = self.head.next
        while(cur):
                output.append(cur.val)
                cur = cur.next
        return output
    
class RecentCounter:

    '''
    Thoughts:

    We should add requests at time t when pinged to a data structure.
    Also, we have to return the number of requests in range [t-3000, t].
    As, every call to ping is strictly increasing, we wont need any values that are before the time t-3000
    This means we have to remove from front.

    Thus, queue is a great data structure to add at the end and remove from front

    Pseudocode:

    1. Initialize a queue in __init__. Queue is implemented with linked list nodes
    2. For ping function, add t to the end of the queue. 
    3. While the value in the front of the queue is less than t-3000, remove from the queue
    4. When the start value of the queue comes within the range, return the current length of the queue 

    '''
    def __init__(self):
        self.requests = Queue()

    def ping(self, t: int) -> int: 
        self.requests.enqueue(t)
        while(self.requests.head.next.val < t - 3000):
            self.requests.dequeue()
        return self.requests.getSize()

#Time complexity of Ping(): 

# We start popping out elements only when t gets greater than 3000. 
# In worst case, the while loop runs 3000 times to pop out the old requests.
# In best case, when the t is less than 3000, the while loop doesnt get executed.
# And the initialization of queue, adding and popping takes only constant time
# So, the worst case runtime is O(3000) => O(1)

#Space complexity of Ping():

#In worst case, the length of the queue will be 3000. So, the space complexity is O(3000) => O(1)

#Main function to test the RecentCounter
if __name__ == "__main__":
    obj = RecentCounter()
    result = []
    result.append(obj.ping(1))
    result.append(obj.ping(100))
    result.append(obj.ping(3001))
    result.append(obj.ping(3002))
    print(result)