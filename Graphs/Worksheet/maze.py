from collections import deque
class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        
        if maze[start[0]][start[1]] == 1:
            return False
        
        m = len(maze)
        n = len(maze[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)] #up, down, right, left
        
        visited = set()
        
        queue = deque()
        queue.append((start[0], start[1]))
        
        visited.add(tuple(start))
        
        while queue:
            
            current = queue.popleft()
            if current[0] == destination[0] and current[1] == destination[1]:
                return True
            
            for x, y in directions:
                new_row = current[0] + x
                new_col = current[1] + y
                #ball rolls in the same direction until it hits a wall
                #do not stop until the ball hits a wall
                while( 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] == 0):
                    new_row += x
                    new_col += y
                
                #how the ball has hit the wall
                #move one position back so that its not wall
                r = new_row - x
                c = new_col - y
                #if the position is not visited yet, visit it and add to queue
                if (r,c) not in visited:
                    visited.add((r,c))
                    queue.append((r, c))
        
        return False
if __name__ == '__main__':
    sol = Solution()
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    print(sol.hasPath(maze, [0,4], [4,4]))
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    print(sol.hasPath(maze, [0,4], [3,2]))
    maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
    print(sol.hasPath(maze, [4,3], [0,1]))