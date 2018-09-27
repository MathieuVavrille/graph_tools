
class Vertex:
    def __init__(self, name=None, data=None):
        self.name = name
        self.data = data


class Edge:
    def __init__(self, start=None, end=None, oriented=False, data=None):
        self.data = data
        self.start = start
        self.end = end
        self.oriented = oriented

    def __eq__(self, other):
        if self.oriented:
            return self.stat == other.start and self.end == other.end
        return {self.start, self.end} == {other.start, other.end}


class Graph:
    """
    A class representing a graph.
    Data are stored as adjacency lists stored in a dictionnary
    """

    def __init__(self, _graph_dict):
        """
        Initialization function. Is not meant to be called as it is.
        """
        self._dict = _graph_dict

    # --------------- Initialization methods --------------------------
    @staticmethod
    def from_edge_list(l, oriented=False):
        if isinstance(l, str):
            print(l)
            edges = []
            # Load from a file
            with open(l, 'r') as f:
                for s in f.readlines():
                    s = s.strip().split()
                    edges.append(Edge(Vertex(s[0]), Vertex(s[1]), oriented))
        else:
            edges = l
        graph_dict = dict()
        for edge in edges:
            if edge.start not in graph_dict:
                graph_dict[edge.start] = [edge.end]
            else:
                graph_dict[edge.start].append(edge.end)
            if not edge.oriented:
                if edge.end not in graph_dict:
                    graph_dict[edge.end] = [edge.start]
                else:
                    graph_dict[edge.end].append(edge.start)
        return Graph(graph_dict)

    @staticmethod
    def from_adjacency_dict(d):
        if isinstance(d, str):
            # Load from a file
            pass
        return Graph(d)

    @staticmethod
    def from_adjacency_matrix(m):
        if isinstance(m, str):
            # Load from a file
            pass
        return Graph({})

    @staticmethod
    def erdos_renyi(n, p):
        return Graph({})

    # ---------------- Getters and setters -----------------------------
    def vertices(self):
        """
        Returns an iterator over the vertices of the graph
        """
        return self._dict.keys()

    def edges(self):
        """
        Returns an iterator over the edges of a the graph
        """
        return []

    # ---------------  Modification of the data ------------------------
    def add_vertex(self, vertex):
        if vertex not in self._dict:
            self._dict[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self._dict:
            del self._dict[vertex]

    def add_edge(self, edge):
        pass

    def remove_edge(self, edge):
        pass

    # ---------------- Stats computations -----------------------------
    def vertex_degree(self):
        return [len(self._dict[v]) for v in self.vertices()]

    def degree_sequence(self):
        degree_list = self.vertex_degree()
        degree_list.sort()
        return degree_list

    def is_erdos_gallai(self):
        """
        Returns True if and only if the graph respects the Erdös-Gallai
        property.
        See https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gallai_theorem
        """
        return False
