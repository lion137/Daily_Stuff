# graphs


class Graph:
    """class graph"""
    def __init__(self, v_in):
        """constructor -  takes number of vertices and creates a graph
         with no edges (E = 0) and an empty adjacent lists of vertices"""
        self.V = v_in
        self.E = 0
        self.adj = []
        for i in range(v_in):
            self.adj.append([])

    def V(self):
        """returns number of vertices"""
        return self.V

    def E(self):
        """returns number of edges"""
        return self.E

    def add_edge(self, v, w):
        """void, adds an edge to the graph"""
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def adj_list(self, v):
        """returns the adjacency lists of the vertex v"""
        return self.adj[v]

    def __str__(self):
        """to string method"""
        s = str(self.V) + " vertices, " + str(self.E) + " edges\n"
        for v in range(self.V):
            s += str(v) + ": "
            for w in self.adj[v]:
                s += str(w) + " "
            s += "\n"
        return s

def dfs(gr, v):
    """depth first search"""
    marked = [False] * gr.V
    def df(grap, w):
        """central dfs recursivemethod"""
        marked[w] = True
        for x in grap.adj_list(w):
            if marked[x] == False:
                df(grap, x)
    df(gr, v)
    return marked


if __name__ == '__main__':
    gr1 = Graph(4)
    print(gr1)
    print(gr1.adj_list(1))
    print(gr1.E, gr1.V)
    gr1.add_edge(2, 3)
    print(gr1)
    print(gr1.E)
    print(gr1.adj_list(2))
    print(gr1.adj_list(0))
    print("---------dfs------------")
    gr2 = Graph(6)
    gr2.add_edge(0,5)
    #gr2.add_edge(2, 4)
    gr2.add_edge(2, 3)
    gr2.add_edge(1, 2)
    gr2.add_edge(0, 1)
    #gr2.add_edge(3, 4)
    gr2.add_edge(3, 5)
    gr2.add_edge(0, 2)
    print(gr2)
    print(dfs(gr2, 0))