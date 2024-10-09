import unittest
import random

from DFS import SimpleGraph


class DFSTests(unittest.TestCase):

    def setUp(self) -> None:
        self.tree = SimpleGraph(8)
        self.tree.AddVertex(0)
        self.tree.AddVertex(1)
        self.tree.AddVertex(2)
        self.tree.AddVertex(3)
        self.tree.AddVertex(4)
        self.tree.AddVertex(5)
        self.tree.AddVertex(6)
        self.tree.AddVertex(7)

        self.tree.AddEdge(3, 7)
        self.tree.AddEdge(3, 4)
        self.tree.AddEdge(3, 2)
        self.tree.AddEdge(7, 6)
        self.tree.AddEdge(4, 5)
        self.tree.AddEdge(2, 1)
        self.tree.AddEdge(2, 5)
        self.tree.AddEdge(5, 6)

    def test_regression(self):

        self.tree.AddEdge(0, 0)
        self.assertEqual(
            [node.Value for node in self.tree.DepthFirstSearch(0, 0)], [0, 0]
        )

        self.assertEqual(self.tree.DepthFirstSearch(0, 6), [])
        self.assertEqual(self.tree.DepthFirstSearch(6, 0), [])
        self.assertEqual(
            [node.Value for node in self.tree.DepthFirstSearch(3, 6)], [3, 2, 5, 6]
        )
        self.assertEqual(
            [node.Value for node in self.tree.DepthFirstSearch(2, 1)], [2, 1]
        )
        self.assertEqual(
            [node.Value for node in self.tree.DepthFirstSearch(1, 7)],
            [1, 2, 3, 4, 5, 6, 7],
        )

    def test_regression_is_connected_graph(self):
        self.assertFalse(self.tree.is_connected_graph())

        self.tree.AddEdge(0, 0)
        self.assertFalse(self.tree.is_connected_graph())

        self.tree.AddEdge(0, 1)
        self.assertTrue(self.tree.is_connected_graph())

        self.tree.RemoveVertex(7)
        self.assertTrue(self.tree.is_connected_graph())

    def test_is_vertexes_connected(self):
        self.assertEqual(self.tree.is_vertexes_connected(0, 1), (False, []))
        self.assertEqual(
            tuple(vertex.Value for vertex in self.tree.is_vertexes_connected(1, 3)[1]),
            (1, 2, 3),
        )
        self.assertTrue(self.tree.is_vertexes_connected(1, 3)[0])


if __name__ == "__main__":
    unittest.main()
