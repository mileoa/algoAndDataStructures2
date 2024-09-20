import unittest
import random

from AllNodes import BST, BSTNode


class AllNodesTests(unittest.TestCase):

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

    @unittest.skip
    def test_regression_DeepAllNodes(self):
        self.assertEqual(
            self.tree.DeepAllNodes(0),
            (
                self.root_left,
                self.root,
                self.root_right,
                self.root_right_left,
                self.root_right_right,
            ),
        )
        self.assertEqual(
            self.tree.DeepAllNodes(1),
            (
                self.root_left,
                self.root_right_left,
                self.root_right_right,
                self.root_right,
                self.root,
            ),
        )
        self.assertEqual(
            self.tree.DeepAllNodes(2),
            (
                self.root,
                self.root_left,
                self.root_right,
                self.root_right_left,
                self.root_right_right,
            ),
        )

    def test_empty_DeepAllNodes(self):
        empty_tree = BST(None)
        self.assertEqual(empty_tree.DeepAllNodes(0), ())
        self.assertEqual(empty_tree.DeepAllNodes(1), ())
        self.assertEqual(empty_tree.DeepAllNodes(2), ())

    def test_regression_WideAllNodes(self):
        self.assertEqual(
            self.tree.WideAllNodes(),
            (
                self.root,
                self.root_left,
                self.root_right,
                self.root_right_left,
                self.root_right_right,
            ),
        )

    def test_empty_WideAllNodes(self):
        empty_tree = BST(None)
        self.assertEqual(empty_tree.WideAllNodes(), ())


if __name__ == "__main__":
    unittest.main()
