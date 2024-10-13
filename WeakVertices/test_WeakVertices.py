import unittest
import random

from WeakVertices import SimpleGraph


class SimpleGraphTests(unittest.TestCase):

    def setUp(self):
        self.tree = SimpleGraph(9)
        for i in range(9):
            self.tree.AddVertex(i)
        self.tree.AddEdge(0, 1)
        self.tree.AddEdge(0, 2)
        self.tree.AddEdge(0, 3)
        self.tree.AddEdge(1, 3)
        self.tree.AddEdge(2, 3)
        self.tree.AddEdge(1, 4)
        self.tree.AddEdge(3, 5)
        self.tree.AddEdge(4, 5)
        self.tree.AddEdge(5, 6)
        self.tree.AddEdge(5, 7)
        self.tree.AddEdge(6, 7)
        self.tree.AddEdge(7, 8)

    def test_regression(self):
        self.assertCountEqual(
            self.tree.WeakVertices(), [self.tree.vertex[4], self.tree.vertex[8]]
        )
        self.tree.RemoveEdge(5, 6)
        self.assertCountEqual(
            self.tree.WeakVertices(),
            [
                self.tree.vertex[4],
                self.tree.vertex[8],
                self.tree.vertex[5],
                self.tree.vertex[6],
                self.tree.vertex[7],
            ],
        )

    def test_empty(self):
        pass

    def test_random(self):
        pass

    def test_border(self):
        pass


if __name__ == "__main__":
    unittest.main()
