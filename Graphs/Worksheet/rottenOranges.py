from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:
        freshOranges = 0
        queue = deque()
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    #add to queue
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    freshOranges += 1
        
        queue.append((-1,-1))   #marker
        
        timeElapsed = -1
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while queue:
            current_r, current_c = queue.popleft()
            if current_r == -1 and current_c == -1:
                timeElapsed += 1
                if queue:   #make sure there are any oranges in queue that are about to rot. If not it marks the end of the traversal of the grid
                    queue.append((-1,-1)) #append another marker now
                
                continue
            for x, y in directions:
                new_r = current_r + x
                new_c = current_c + y
                
                if 0 <= new_r < m and 0 <= new_c < n:
                    if grid[new_r][new_c] == 0:
                        continue
                    elif grid[new_r][new_c] == 1:
                        #rot it
                        grid[new_r][new_c] = 2
                        freshOranges -= 1
                        queue.append((new_r, new_c))
        if freshOranges == 0:
            return timeElapsed
        else:
            return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(sol.orangesRotting([[0,2]]))