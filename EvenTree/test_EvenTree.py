import unittest
import random

from EvenTree import SimpleTree, SimpleTreeNode


class EvenTreeTests(unittest.TestCase):
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

    def test_binary_even(self):
        self.tree.DeleteNode(self.tree.Root.Children[1])
        self.tree.balance_binary_even()

        self.assertEqual(self.tree.Root.NodeValue, 7)
        self.assertEqual(self.tree.Root.Children[0].NodeValue, 5)
        self.assertEqual(self.tree.Root.Children[1].NodeValue, 9)
        self.assertEqual(self.tree.Root.Children[0].Children[0].NodeValue, 2)
        self.assertEqual(self.tree.Root.Children[0].Children[1].NodeValue, 6)
        self.assertEqual(
            self.tree.Root.Children[0].Children[0].Children[0].NodeValue, 1
        )
        self.assertEqual(self.tree.Root.Children[0].Children[1].Children, [])
        self.assertEqual(self.tree.Root.Children[1].Children[0].NodeValue, 8)
        self.assertEqual(self.tree.Root.Children[1].Children[0].Children, [])
        self.assertEqual(self.tree.Root.Children[1].Children[1].NodeValue, 10)
        self.assertEqual(self.tree.Root.Children[1].Children[1].Children, [])
        self.assertEqual(len(self.tree.Root.Children[0].Children[0].Children), 1)


if __name__ == "__main__":
    unittest.main()
