
def buildAdjList(edges):
    adjList = {}
    for source, destination in edges:
        if source in adjList:
            adjList[source].append(destination)
        else:
            if destination:
                adjList[source] = [destination]
            else:
                adjList[source] = []
    return adjList