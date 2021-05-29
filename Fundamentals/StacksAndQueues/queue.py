# helper linked list class
class Node:
	def __init__(self, item):
		self.item = item
		self.next = None

class Queue:
	#creates an empty queue
	def __init__(self):
		#O(1) time and space
		self._size = 0
		self.front = Node('dummy')
		self.end = self.front

	#adds an item to the queue
	def enqueue(self, item):
		#O(1) time and space
		self.end.next = Node(item)
		self.end = self.end.next
		self._size += 1
	
	# removes and returns the least recently added item
	def dequeue(self):
		#O(1) space and time
		if self.isEmpty():
			print("Cannot dequeue from an empty queue")
			return
		out = self.front.next
		self.front.next = self.front.next.next
		self._size -= 1
		if(self.isEmpty()):
			self.end = self.front
		return out.item
	
	#returns boolean indicating of the queue is empty
	def isEmpty(self):
		#O(1) space and time
		return self.size() == 0
	
	#returns the number of items in the queue
	def size(self):
		#O(1) space and time
		return self._size
	
	#returns a list of items in the queue
	def items(self):
		#O(N) time and space
		output = []
		cur = self.front.next
		while(cur):
				output.append(cur.item)
				cur = cur.next
		return output

if __name__ == "__main__":
    #test cases
    queue = Queue()
    for i in range(3):
        queue.enqueue(i)
    print(queue.items()) #0 1 2
    for _ in range(4):
        print(queue.dequeue())
    #0 1 2 None
    for i in range(2,4):
        queue.enqueue(i)
    print(queue.items()) #should print 2 3

    