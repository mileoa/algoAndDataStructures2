import unittest

from invert_tree_BST import BSTNode, BST


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

    def test_regression_invert_tree(self):
        self.tree.invert_tree()

        self.assertEqual(self.tree.Root, self.root)
        self.assertEqual(self.tree.Root.LeftChild, self.root_right)
        self.assertEqual(self.tree.Root.RightChild, self.root_left)

        self.assertIsNone(self.tree.Root.RightChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.RightChild)

        self.assertEqual(self.tree.Root.LeftChild.LeftChild, self.root_right_right)
        self.assertEqual(self.tree.Root.LeftChild.RightChild, self.root_right_left)

    def test_empty_invert_tree(self):
        empty_tree = BST(None)
        empty_tree.invert_tree()
        self.assertIsNone(empty_tree.Root)


if __name__ == "__main__":
    unittest.main()
