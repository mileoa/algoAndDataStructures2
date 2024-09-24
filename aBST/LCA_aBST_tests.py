import unittest
import random

from LCA_aBST import aBST


class aBSTTests(unittest.TestCase):

    def setUp(self) -> None:

        self.tree = aBST(3)
        self.tree.Tree[0] = 50
        self.tree.Tree[1] = 25
        self.tree.Tree[2] = 75
        self.tree.Tree[4] = 37
        self.tree.Tree[5] = 62
        self.tree.Tree[6] = 84
        self.tree.Tree[9] = 31
        self.tree.Tree[10] = 43
        self.tree.Tree[11] = 55
        self.tree.Tree[14] = 92

    def test_regression_LCA(self):
        self.assertEqual(self.tree.LCA(9, 10), 4)
        self.assertEqual(self.tree.LCA(9, 4), 1)
        self.assertEqual(self.tree.LCA(9, 14), 0)
        self.assertEqual(self.tree.LCA(9, 11), 0)
        self.assertEqual(self.tree.LCA(11, 14), 2)

        self.assertIsNone(self.tree.LCA(1, 0))


if __name__ == "__main__":
    unittest.main()
