class Graph:
    def __init__(self, V) -> None:
        #V - len of vertices
        self._V = V
        self._E = 0
        self._adjList = [[] for _ in range(V)]
    
    def V(self):
        return self._V
    
    def E(self):
        return self._E
    
    def addEdge(self, u, v):
        self._validateVertex(u)
        self._validateVertex(v)
        self._E += 1
        #since it is an undirected graph, we must add edges from u to v and v to u
        self._adjList[u].append(v)
        self._adjList[v].append(u)
    
    def adj(self, v):
        self._validateVertex(v)
        return self._adjList[v]
    
    def _validateVertex(self, v):
        if v < 0 or v >= self._V:
            raise Exception("vertex " + str(v) + "is invalid. Should be between 0 and " + str(self._V - 1))
    
    def __str__(self) -> str:
        return str(self._adjList)

if __name__ == '__main__':
    vertices = ["A", "B", "C", "D"]
    V = len(vertices)
    G = Graph(V)

    G.addEdge(0,1)
    G.addEdge(0,2)
    G.addEdge(0,3)
    G.addEdge(2,3)

    print(G.adj(0))
    print(str(G))