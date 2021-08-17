class Graph:
    def __init__(self, V) -> None:
        #V - len of vertices
        self._V = V
        self._E = 0
        self._adjList = []
        for i in range(0, V):
            self._adjList.append([False] * V)
    
    def V(self):
        return self._V
    
    def E(self):
        return self._E
    
    def addEdge(self, u, v):
        self._validateVertex(u)
        self._validateVertex(v)
        if not self._adjList[u][v]:
            self._E += 1
        #since it is an undirected graph, we must add edges from u to v and v to u
        self._adjList[u][v] = True
        self._adjList[v][u] = True
        
    def adj(self, v):
        self._validateVertex(v)
        neighbors = []
        for u in range(0, self._V):
            if self._adjList[v][u]:
                neighbors.append(u)
        return neighbors
    
    def _validateVertex(self, v):
        if v < 0 or v >= self._V:
            raise Exception("vertex " + str(v) + "is invalid. Should be between 0 and " + str(self._V - 1))
    
    def __str__(self) -> str:
        s = ""
        for row in self._adjList:
            s += str(row) + "\n"
        return s

if __name__ == '__main__':
    vertices = ["Albert", "Bob", "Christa", "Danielle"]
    V = len(vertices)
    G = Graph(V)

    G.addEdge(0,1)
    G.addEdge(0,2)
    G.addEdge(0,3)
    G.addEdge(2,3)

    print(G.adj(0))
    print(str(G))