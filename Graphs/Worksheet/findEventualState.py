import collections
class Solution:
    def eventualSafeNodes(self, graph):
        #topological sort
        inNodesMap = collections.defaultdict(list)
        outDegree = collections.defaultdict(int)
        
        n = len(graph)
        
        queue = collections.deque()
        
        for i in range(n):
            outDegree[i] = len(graph[i])
            if outDegree[i] == 0:
                queue.append(i)
            for num in graph[i]:
                inNodesMap[num].append(i)
        
        result = []
        #do bfs
        while queue:
            term_node = queue.popleft()
            result.append(term_node)
            for node in inNodesMap[term_node]:
                outDegree[node] -= 1
                if outDegree[node] == 0:
                    queue.append(node)
        
        return sorted(result)

if __name__ == '__main__':
    sol = Solution()
    print(sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
    print(sol.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))