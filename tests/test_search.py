import pytest
from graphtool.graph import *
from graphtool.algorithms.search import *
from utils import *


@pytest.fixture
def triangle():
    a, b, c = Vertex(0), Vertex(1), Vertex(2)
    return Graph.from_edge_list([Edge(a, b), Edge(b, c), Edge(c, a)])


def test_connected_components(triangle):
    g = GraphGenerator.empty(3)
    g.add_edge(0, 1)
    assert len(get_connected_components(g)) == 2
    assert len(get_connected_components(triangle)) == 1


def test_dfs():
    g = Graph.from_edge_list("graph_examples/graph_100n_1000m.txt")
    functors = count_nodes_functors()
    assert depth_first_search(g, Vertex(0), functors) == 100


def test_no_prefunctor_dfs():
    g = Graph.from_edge_list("graph_examples/graph_100n_1000m.txt")
    functors = (no_pre_functor, no_neighbour_functor, no_post_functor)
    assert depth_first_search(g, Vertex(0), functors) is None


def test_topological_sort():
    g = GraphGenerator.empty(4, type="oriented")
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    assert topological_sort(g) == [Vertex(3),
                                   Vertex(2), Vertex(1), Vertex(0)]

    g.add_edge(3, 0)
    try:
        topological_sort(g)
        assert False
    except Exception as e:
        assert str(e) == "Topological sort error : cycles found graph"
