import unittest
import random

from BFS import SimpleGraph


class BFSTests(unittest.TestCase):

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

    def test_regression_BreadthFirstSearch(self):

        self.tree.AddEdge(0, 0)
        self.assertEqual(
            [node.Value for node in self.tree.BreadthFirstSearch(0, 0)], [0, 0]
        )

        self.assertEqual(self.tree.BreadthFirstSearch(0, 6), [])
        self.assertEqual(self.tree.BreadthFirstSearch(6, 0), [])
        self.assertEqual(
            [node.Value for node in self.tree.BreadthFirstSearch(3, 6)], [3, 7, 6]
        )
        self.assertEqual(
            [node.Value for node in self.tree.BreadthFirstSearch(2, 1)], [2, 1]
        )
        self.assertEqual(
            [node.Value for node in self.tree.BreadthFirstSearch(1, 7)],
            [1, 2, 3, 7],
        )

    def test_find_two_most_distant_vertexes(self):
        self.assertEqual(self.tree.find_farthest_vertexes_path_len(), 4)
        self.tree.RemoveEdge(2, 3)
        self.tree.RemoveEdge(2, 5)
        self.tree.RemoveEdge(7, 6)
        self.assertEqual(self.tree.find_farthest_vertexes_path_len(), 4)


if __name__ == "__main__":
    unittest.main()
