from collections import deque
from buildAdjList import buildAdjList
def DFS(adjList, source, destination):
    #O(N) space
    #O(N^2) runtime
    visited = set()
    return _recursive_dfs(adjList, visited, source, destination)

def _recursive_dfs(adjList, visited, src, dest):
    if src == dest:
        return True
    if src in visited:
        return False
    visited.add(src)
    #O(N)
    for neighbor in adjList[src]:
        #O(N)
        if _recursive_dfs(adjList, visited, neighbor, dest):
            return True
    return False

if __name__ == '__main__':
    loveConnections = [("Hermia", "Lysander"), ("Demetrius", "Lysander"),
                        ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania"), ("Hermia", "Puck"), ("Puck", "Helena")]
    adjList = buildAdjList(loveConnections)
    print(adjList)
    print(DFS(adjList, "Hermia", "Oberon"))