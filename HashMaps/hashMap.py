
class Node:
	
	#O(1) time and space
	def __init__(self, key, value) -> None:
		self.key = key
		self.value = value
		self.next = None
		 
class SeparateChainingHashMap:
	# Initializes an emtpy hash map.
	#O(capacity) time and space
	def __init__(self, capacity):
		self.map = [Node("dummy", "dummy") for _ in range(capacity)]


	# Given a key, will return the value associated with that key if it’s in the table. 
	# This function will return None if the key is not in the hash map. 
	# O(N)/capacity time average space..If capacity is N, average time is O(1). O(N) in worst case
	# O(1) space
	def get(self, key):
		index = self._hash(key)
		cur = self.map[index]
		while(cur.next):
			if cur.next.key == key:
				return cur.next.value
			cur = cur.next
		return None
	
	# Inserts the key-value pair into the hashmap. 
	# If the key already exists it will overwrite the previous value with the new value. 
	# O(N)/capacity time average space..If capacity is N, average time is O(1). O(N) in worst case
	# O(1) space
	def put(self, key, value):
		index = self._hash(key)
		cur = self.map[index]
		while(cur.next):
			if cur.next.key == key:
				cur.next.value = value
				return
			cur = cur.next
		cur.next = Node(key, value)
		return

	#deletes a key and its val from the hashmap
	def delete(self, key):
		index = self._hash(key)
		prev = self.map[index]
		cur = prev.next
		while(cur.next):
			if cur.key == key:
				prev.next = cur.next
			prev = cur
			cur = cur.next

 	# # Returns true if it contains the key. 
 	# # O(1) runtime.
	# def contains(self, key):
	# 	index = self._hash(key)
	# 	if self.array[index][0] == key:
	# 		return True
	# 	else:
	# 		return False

	# Private function to compute an integer hash value for a given key. 
	# O(1) time and space
	def _hash(self, key):
		return key % len(self.map)

	#O(N) time and space
	def __str__(self) -> str:
		out = ""
		for index in range(len(self.map)):
			cur = self.map[index].next
			while(cur):
				out += str(cur.value) + " "
				cur = cur.next
			out += "\n"
		return out

if __name__ == "__main__":
	map = SeparateChainingHashMap(3)
	for i in range(10):
		map.put(i, i*2)
	
	#0 6 12 18
	#2 8 14
	#4 10 16

	print(map)
	print(map.get(4))
	for i in range(3):
		map.delete(i)
	print(map)