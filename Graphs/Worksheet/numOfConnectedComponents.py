class Solution:
    def countComponents(self, n: int, edges) -> int:
        adjList = {i:[] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        
        def dfs(curNode):
            if visited[curNode] is True:
                return
            visited[curNode] = True
            for neighbor in adjList[curNode]:
                if visited[neighbor] is False:
                    dfs(neighbor)
            return
        
        visited = [False] * n
        count = 0
        for i in range(n):
            if visited[i] is False:
                dfs(i)
                count += 1
        return count
if __name__ == '__main__':
    sol = Solution()
    print(sol.countComponents(5, [[0,1],[1,2],[3,4]]))
    print(sol.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))