import unittest
import random

from BalancedBST import BalancedBST, BSTNode


class BalancedBSTTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBST()

    def test_regression_GenerateTree(self):
        self.tree.GenerateTree([75, 62, 84, 37, 25, 50, 20])
        self.assertEqual(self.tree.Root.NodeKey, 50)
        self.assertEqual(self.tree.Root.Level, 0)
        self.assertIsNone(self.tree.Root.Parent)

        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 25)
        self.assertEqual(self.tree.Root.LeftChild.Level, 1)
        self.assertEqual(self.tree.Root.LeftChild.Parent, self.tree.Root)

        self.assertEqual(self.tree.Root.LeftChild.LeftChild.NodeKey, 20)
        self.assertEqual(self.tree.Root.LeftChild.LeftChild.Level, 2)
        self.assertEqual(
            self.tree.Root.LeftChild.LeftChild.Parent, self.tree.Root.LeftChild
        )
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild.RightChild)

        self.assertEqual(self.tree.Root.LeftChild.RightChild.NodeKey, 37)
        self.assertEqual(self.tree.Root.LeftChild.LeftChild.Level, 2)
        self.assertEqual(
            self.tree.Root.LeftChild.RightChild.Parent, self.tree.Root.LeftChild
        )
        self.assertIsNone(self.tree.Root.LeftChild.RightChild.LeftChild)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild.RightChild)

        self.assertEqual(self.tree.Root.RightChild.NodeKey, 75)
        self.assertEqual(self.tree.Root.RightChild.Level, 1)
        self.assertEqual(self.tree.Root.RightChild.Parent, self.tree.Root)

        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 62)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.Level, 2)
        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.Parent, self.tree.Root.RightChild
        )
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)

        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 84)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.Level, 2)
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.Parent, self.tree.Root.RightChild
        )
        self.assertIsNone(self.tree.Root.RightChild.RightChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.RightChild.RightChild)

    def test_empty_GenerateTree(self):
        self.tree.GenerateTree([])
        self.assertIsNone(self.tree.Root)

    def test_IsBalanced(self):
        self.tree.GenerateTree([75, 62, 84, 37, 25, 50, 20])
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))
        self.assertTrue(self.tree.IsBalanced(self.tree.Root.LeftChild))
        self.assertTrue(self.tree.IsBalanced(self.tree.Root.RightChild))

        additional_node_one: BSTNode = BSTNode(10, self.tree.Root.LeftChild.LeftChild)
        additional_node_one.Level = 3
        self.tree.Root.LeftChild.LeftChild.LeftChild = additional_node_one
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))

        additional_node_two: BSTNode = BSTNode(5, additional_node_one)
        additional_node_two.Level = 4
        additional_node_one.LeftChild = additional_node_two
        self.assertFalse(self.tree.IsBalanced(self.tree.Root))
        self.assertTrue(self.tree.IsBalanced(additional_node_one))

    def test_is_valid_tree(self):
        self.tree.GenerateTree([75, 62, 84, 37, 25, 50, 20])
        self.assertTrue(self.tree.is_valid_tree())

        self.tree.Root.LeftChild.NodeKey = 70
        self.assertFalse(self.tree.is_valid_tree())


if __name__ == "__main__":
    unittest.main()
