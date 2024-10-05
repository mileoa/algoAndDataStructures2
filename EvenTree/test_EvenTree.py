import unittest
import random

from EvenTree import SimpleTree, SimpleTreeNode


class SimpleTreeTests(unittest.TestCase):

    def test_regression_EvenTrees(self):
        tree = SimpleTree(SimpleTreeNode(1, None))
        tree.AddChild(tree.Root, SimpleTreeNode(2, None))
        tree.AddChild(tree.Root.Children[0], SimpleTreeNode(5, None))
        tree.AddChild(tree.Root.Children[0], SimpleTreeNode(7, None))

        tree.AddChild(tree.Root, SimpleTreeNode(3, None))
        tree.AddChild(tree.Root.Children[1], SimpleTreeNode(4, None))

        tree.AddChild(tree.Root, SimpleTreeNode(6, None))
        tree.AddChild(tree.Root.Children[2], SimpleTreeNode(8, None))
        tree.AddChild(tree.Root.Children[2].Children[0], SimpleTreeNode(9, None))
        tree.AddChild(tree.Root.Children[2].Children[0], SimpleTreeNode(10, None))

        self.assertEqual([node.NodeValue for node in tree.EvenTrees()], [1, 3, 1, 6])


if __name__ == "__main__":
    unittest.main()
