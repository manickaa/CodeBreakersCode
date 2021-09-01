from collections import deque
class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        m = len(heights)
        n = len(heights[0])
        
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(m):
            pacific_queue.append((i,0))
            atlantic_queue.append((i, n-1))
        for i in range(n):
            pacific_queue.append((0,i))
            atlantic_queue.append((m-1,i))
        
        #function for bfs traversal
        def bfs(queue):
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            reachable = set()
            while queue:
                r, c = queue.popleft()
                if (r, c) in reachable:
                    continue
                reachable.add((r,c))
                for x, y in directions:
                    new_r = r + x
                    new_c = c + y
                    if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n:
                        continue
                    if ((new_r, new_c) in reachable):
                        #already traversed
                        continue
                    else:
                        if heights[new_r][new_c] >= heights[r][c]:
                            queue.append((new_r, new_c))
                        else:
                            continue
            return reachable
                
        
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        #return the intersection of both these sets
        return list(pacific_reachable.intersection(atlantic_reachable))

if __name__ == '__main__':
    sol = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(sol.pacificAtlantic(heights))
    print(sol.pacificAtlantic([[2,1],[1,2]]))
