class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
  def __init__(self, listNode):     
    # head references first node in chain of nodes					# 1 -> 2 -> 3 -> 4 		Head: 1
    self.head = listNode
  
  def function1(self, newNode):   						# NewNode: 5
    newNode.next = self.head							# 5 -> 1-> 2-> 3 -> 4  	Head: 5
    self.head = newNode
  
  def function2(self, newNode):						#NewNode:  6
    if self.head is None:							# 5 -> 1 -> 2 -> 3 -> 4 -> 6 	Head: 5
      self.head = newNode
      return
    cur = self.head
    while(cur.next):
      cur = cur.next
    cur.next = newNode
  
  def function3(self):								# 5 -> 1 -> 2 -> 3 -> 4 -> 6 	Head: 5
    if self.head:	
      self.head = self.head.next

  def __str__(self):
        #O(N) time
        #O(N) space
        result = ""
        current = self.head
        while(current):
            result += str(current.val) + "|"
            current = current.next
        return result


if __name__ == '__main__':
  headNode = Node(1)  
  linkedList = LinkedList(headNode)   #1
  print(linkedList)
  newNode = Node(2)
  linkedList.function1(newNode)       #2|1
  print(linkedList)
  newNode = Node(3)
  linkedList.function2(newNode)       #2|1|3
  print(linkedList)
  linkedList.function3()              #1|3
  print(linkedList)