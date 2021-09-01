from buildAdjList import buildAdjList

def detectCycle(adjList):
    visited = set()
    for key in adjList.keys():
        if key not in visited:
            if(DFS(key, set(), visited, adjList)):
                return True
    return False

def DFS(curNode, curPath, visited, adjList):
    if curNode in curPath:
        return True
    curPath.add(curNode)
    visited.add(curNode)
    for neighbor in adjList[curNode]:
        if curNode == neighbor:
            continue
        if neighbor not in visited:
            if DFS(neighbor, curPath, visited, adjList):
                return True
    curPath.remove(curNode) #to backtrack
    return False


if __name__ == '__main__':
    loveConnections = [("Hermia", "Lysander"), ("Demetrius", "Lysander"),
                        ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania"), ("Hermia", "Puck"), ("Puck", "Helena")]
    adjList = buildAdjList(loveConnections)
    print(adjList)
    print(detectCycle(adjList))