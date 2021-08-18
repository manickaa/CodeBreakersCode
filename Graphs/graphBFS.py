from typing import Deque
from collections import deque
from buildAdjList import buildAdjList
def BFS(adjList, source, destination):
    #O(N) space
    #O(N^2) runtime
    queue = deque()
    queue.append(source)
    visited = set()
    while queue:
        currentVertex = queue.popleft()
        if currentVertex == destination:
            return True
        visited.add(currentVertex)
        for neighbor in adjList[currentVertex]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False

if __name__ == '__main__':
    loveConnections = [("Hermia", "Lysander"), ("Demetrius", "Lysander"),
                        ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania"), ("Hermia", "Puck"), ("Puck", "Helena")]
    adjList = buildAdjList(loveConnections)
    print(adjList)
    print(BFS(adjList, "Hermia", "Oberon"))