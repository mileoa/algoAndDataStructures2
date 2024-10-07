import unittest
import random

from DFS import SimpleGraph


class DFSTests(unittest.TestCase):

    def test_regression(self):
        tree = SimpleGraph(8)
        tree.AddVertex(0)
        tree.AddVertex(1)
        tree.AddVertex(2)
        tree.AddVertex(3)
        tree.AddVertex(4)
        tree.AddVertex(5)
        tree.AddVertex(6)
        tree.AddVertex(7)

        tree.AddEdge(3, 7)
        tree.AddEdge(3, 4)
        tree.AddEdge(3, 2)
        tree.AddEdge(7, 6)
        tree.AddEdge(4, 5)
        tree.AddEdge(2, 1)
        tree.AddEdge(2, 5)
        tree.AddEdge(5, 6)

        tree.AddEdge(0, 0)
        self.assertEqual([node.Value for node in tree.DepthFirstSearch(0, 0)], [0, 0])

        self.assertEqual(tree.DepthFirstSearch(0, 6), [])
        self.assertEqual(tree.DepthFirstSearch(6, 0), [])
        self.assertEqual(
            [node.Value for node in tree.DepthFirstSearch(3, 6)], [3, 2, 5, 6]
        )
        self.assertEqual([node.Value for node in tree.DepthFirstSearch(2, 1)], [2, 1])
        self.assertEqual(
            [node.Value for node in tree.DepthFirstSearch(1, 7)], [1, 2, 3, 4, 5, 6, 7]
        )


if __name__ == "__main__":
    unittest.main()
