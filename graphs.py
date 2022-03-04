"""
Graphs
a graph is pictorial representation of a set of objects
where some pairs of objects are connected by links.
the interconnected objects are represented by points
termed as vertices, and the links that connects the vertices
are called edges.
operations in graphs::
1. display graph vertices
2. display graph edges
3. add a vertex
4. add an edge
5. creating a graph
"""
# vertex - V, edge = E
V = {'a', 'b', 'c', 'd','e'}
E = {'ab', 'bd', 'ac', 'cd', 'de'}

# creating the dictionary with graph elements
graph = {'a': ['b', 'c'],
         'b': ['a', 'd'],
         'c': ['a', 'd'],
         'd': ['e', 'b', 'c'],
         'e': ['d']
         }
print(graph)


class Graph:   # display graph vertices
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

g = Graph(graph)
print(g.getVertices())


class Graph:   # finding edges
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()

    def findedges(self):
        edgeName = []
        for vertex in self.gdict:
            for nxt_vertex in self.gdict[vertex]:
                if {nxt_vertex, vertex} not in edgeName:
                    edgeName.append({vertex, nxt_vertex})
        return edgeName

g = Graph(graph)
print(g.edges())


class Graph:   # adding a vertex
    def __init__(self, gd=None):
        if gd is None:
            gd = {}
        self.gd = gd

    def get_vertices(self):
        return list(self.gd.keys())

    def add_vertex(self, vrtx):
        if vrtx not in self.gd:
            self.gd[vrtx] = []

g = Graph(graph)
g.add_vertex('f')
print(g.get_vertices())


class Graph:
    def __init__(self, gd=None):
        if gd is None:
            gd = {}
        self.gd = gd

    def edges(self):
        return self.findEdges()

    def addEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gd:
            self.gd[vrtx1].append(vrtx2)
        else:
            self.gd[vrtx1] = [vrtx2]

    def findEdges(self):
        edgeName = []
        for vrtx in self.gd:
            for nxtvrtx in self.gd[vrtx]:
                if {nxtvrtx, vrtx} not in edgeName:
                    edgeName.append({vrtx, nxtvrtx})
        return edgeName

g = Graph(graph)
g.addEdge({'a', 'e'})
g.addEdge({'a', 'c'})
print(g.edges())