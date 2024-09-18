import unittest
import random

from BST import BSTNode, BST


class BSTTests(unittest.TestCase):

    def setUp(self):
        self.root = BSTNode(3, 1, None)
        self.root_left = BSTNode(1, 2, self.root)
        self.root_right = BSTNode(7, 2, self.root)
        self.root_right_left = BSTNode(5, 3, self.root_right)
        self.root_right_right = BSTNode(9, 3, self.root_right)
        self.root_right.LeftChild = self.root_right_left
        self.root_right.RightChild = self.root_right_right
        self.root.LeftChild = self.root_left
        self.root.RightChild = self.root_right

        self.tree = BST(self.root)

    def test_regression_FindNodeByKey(self):
        found_node = self.tree.FindNodeByKey(10)
        self.assertEqual(found_node.Node, self.root_right_right)
        self.assertFalse(found_node.NodeHasKey)
        self.assertFalse(found_node.ToLeft)

        found_node = self.tree.FindNodeByKey(4)
        self.assertEqual(found_node.Node, self.root_right_left)
        self.assertFalse(found_node.NodeHasKey)
        self.assertTrue(found_node.ToLeft)

        found_node = self.tree.FindNodeByKey(7)
        self.assertEqual(found_node.Node, self.root_right)
        self.assertTrue(found_node.NodeHasKey)

    def test_empty_FindNodeByKey(self):
        tree = BST(None)
        found_node = tree.FindNodeByKey(0)
        self.assertEqual(found_node.Node, None)
        self.assertFalse(found_node.NodeHasKey)
        self.assertFalse(found_node.ToLeft)

    def test_regression_AddKeyValue(self):
        # Add existing key, nothon happens.
        self.assertFalse(self.tree.AddKeyValue(3, 100))
        self.assertEqual(self.root.NodeKey, 3)
        self.assertEqual(self.root.NodeValue, 1)

        # Add left side.
        self.assertTrue(self.tree.AddKeyValue(4, 101))
        self.assertIsNotNone(self.root_right_left.LeftChild)
        self.assertEqual(self.root_right_left.LeftChild.NodeKey, 4)
        self.assertEqual(self.root_right_left.LeftChild.NodeValue, 101)
        self.assertEqual(self.root_right_left.LeftChild.Parent, self.root_right_left)

        # Add right side.
        self.assertTrue(self.tree.AddKeyValue(10, 102))
        self.assertIsNotNone(self.root_right_right.RightChild)
        self.assertEqual(self.root_right_right.RightChild.NodeKey, 10)
        self.assertEqual(self.root_right_right.RightChild.NodeValue, 102)
        self.assertEqual(self.root_right_right.RightChild.Parent, self.root_right_right)

    def test_empty_AddKeyValue(self):
        empty_tree = BST(None)
        self.assertTrue(empty_tree.AddKeyValue(0, 10))
        self.assertEqual(empty_tree.Root.NodeKey, 0)
        self.assertEqual(empty_tree.Root.NodeValue, 10)
        self.assertEqual(empty_tree.Root.LeftChild, None)
        self.assertEqual(empty_tree.Root.RightChild, None)
        self.assertEqual(empty_tree.Root.Parent, None)

    def test_regression_FinMinMax(self):
        max_node_from_root = self.tree.FinMinMax(self.root, True)
        self.assertEqual(max_node_from_root, self.root_right_right)

        min_node_from_root = self.tree.FinMinMax(self.root, False)
        self.assertEqual(min_node_from_root, self.root_left)

        max_node_from_subtree = self.tree.FinMinMax(self.root_right, True)
        self.assertEqual(max_node_from_subtree, self.root_right_right)

        mim_node_from_subtree = self.tree.FinMinMax(self.root_right, False)
        self.assertEqual(mim_node_from_subtree, self.root_right_left)

    def test_empty_FinMinMax(self):
        empty_tree = BST(None)
        self.assertIsNone(empty_tree.FinMinMax(empty_tree.Root, True))
        self.assertIsNone(empty_tree.FinMinMax(empty_tree.Root, False))

    def test_regression_DeleteNodeByKey(self):
        self.assertFalse(self.assertFalse(self.tree.DeleteNodeByKey(2)))
        self.assertTrue(self.assertFalse(self.tree.DeleteNodeByKey(3)))

        self.assertIsNone(self.root.LeftChild)
        self.assertIsNone(self.root.RightChild)
        self.assertIsNone(self.root.Parent)
        self.assertEqual(self.tree.Root, self.root_right_left)

        self.assertIsNone(self.root_right_left.Parent)
        self.assertEqual(self.root_right_left.LeftChild, self.root_left)
        self.assertEqual(self.root_right_left.RightChild, self.root_right)

        self.assertIsNone(self.root_right.LeftChild)

        self.assertEqual(self.root_left.Parent, self.root_right_left)

    def test_empty_DeleteNodeByKey(self):
        empty_tree = BST(None)
        self.assertFalse(empty_tree.DeleteNodeByKey(1))


if __name__ == "__main__":
    unittest.main()
