class Node:
    #initialize Node
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

# head <-> tail
# head <-> 3 <-> 1 <-> 2 <-> tail

#head: prev: None
#      next: 3

#3: prev: head
#   next: 1

#1: prev: 3
#   next: 2

#2: prev: 1
#   next: tail

#tail: prev: 2
#      next: None

class Deque:
	# initialize an empty deque
	def __init__(self):
		self.size = 0
		self.tail = Node('head', 'head')
		self.head = Node('tail', 'tail')
		self.tail.prev = self.head
		self.head.next = self.tail
        
	# is the deque empty?
	# returns a Boolean 
	def is_empty(self):
		return self.getSize() == 0

    # returns the number of items in the deque
	def getSize(self):
		return self.size

    # inserts item to the front of the deque
	def add_first(self, key, value):
		
		#head <-> tail
		#head <-> 1 <-> tail
		#head <-> 2 <-> 1 <-> tail

		newNode = Node(key, value)
		nextToHead = self.head.next
		#update head.next
		self.head.next = newNode
		#update head.next.prev
		nextToHead.prev = newNode
		#update newNode's next and prev
		newNode.prev = self.head
		newNode.next = nextToHead

		self.size += 1

	# inserts item at the end of the deque
	def add_last(self, key, value):
		
		#head<->tail
		#head<->1<->tail
		#head<->1<->2<->tail

		newNode = Node(key, value)
		prevToTail = self.tail.prev
		#update tail.prev
		self.tail.prev = newNode
		#update tail.prev.next
		prevToTail.next = newNode
		#update newNode's prev and next
		newNode.next = self.tail
		newNode.prev = prevToTail
		self.size += 1 

	# delete and return the key-value pair at the front of the deque 
	def remove_first(self):
		if self.is_empty():
			print('Cannot remove from empty list')
			return
		#head<->1<->2<->tail
		#head<->2<->tail

		#head next next's prev will be head
		self.head.next.next.prev = self.head
		#head's next will be head next's next
		self.head.next = self.head.next.next
		self.size -= 1
		
	# delete and return the key-value at the end of the deque
	def remove_last(self):
		if self.is_empty():
			print("Cannot remove from an empty list")
			return
		#head<->1<->2<->tail
		#head<->1<->tail
		#tail's prev's prev's next will be tail
		self.tail.prev.prev.next = self.tail
		#tail's prev will be tail's prev's prev
		self.tail.prev = self.tail.prev.prev
		self.size -= 1

	def asList(self):
		out = []
		cur = self.head.next
		while(cur.next):
			out.append(cur.value)
			cur = cur.next
		return out

if __name__ == "__main__":
	dq = Deque()

	for i in range(1, 6):
		dq.add_first(i, i)
	print(dq.asList()) #[5,4,3,2,1]

	for i in range(6, 10):
		dq.add_last(i, i)
	print(dq.asList()) #[5,4,3,2,1,6,7,8,9]

	dq.remove_first()
	print(dq.asList()) # [4,3,2,1,6,7,8,9]

	dq.remove_last()
	print(dq.asList()) # [4,3,2,1,6,7,8]
		