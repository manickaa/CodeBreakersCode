from collections import Queue
#Given 2D matrix

def bfsGrid(self, grid):
    N = len(grid)
    visited = set()
    queue = Queue()
    queue.enqueue((0,0))
    direction = [(-1,0),(0,-1),(1,0),(0,1)]
    while queue:
        i, j = queue.dequeue()
        visited.add((i,j))

        #add logic to do something

        for x,y in direction:
            new_i, new_j = i+x, j+y
            if (new_i, new_j) not in visited:
                #check if it is in bounds
                if 0 <= new_i < N and 0 <= new_j < N:
                    queue.enqueue((new_i, new_j))