import unittest
import random

from EvenTree import SimpleTree, SimpleTreeNode


class SimpleTreeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = SimpleTree(SimpleTreeNode(1, None))
        self.tree.AddChild(self.tree.Root, SimpleTreeNode(2, None))
        self.tree.AddChild(self.tree.Root.Children[0], SimpleTreeNode(5, None))
        self.tree.AddChild(self.tree.Root.Children[0], SimpleTreeNode(7, None))

        self.tree.AddChild(self.tree.Root, SimpleTreeNode(3, None))
        self.tree.AddChild(self.tree.Root.Children[1], SimpleTreeNode(4, None))

        self.tree.AddChild(self.tree.Root, SimpleTreeNode(6, None))
        self.tree.AddChild(self.tree.Root.Children[2], SimpleTreeNode(8, None))
        self.tree.AddChild(
            self.tree.Root.Children[2].Children[0], SimpleTreeNode(9, None)
        )
        self.tree.AddChild(
            self.tree.Root.Children[2].Children[0], SimpleTreeNode(10, None)
        )

    def test_regression_EvenTrees(self):

        self.assertEqual(
            [node.NodeValue for node in self.tree.EvenTrees()], [1, 3, 1, 6]
        )

    def test_regression_count_even_subtrees(self):
        self.assertEqual(self.tree.count_even_subtrees(), 3)


if __name__ == "__main__":
    unittest.main()
