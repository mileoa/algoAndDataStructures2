import unittest
import random

from WideAllNodes_aBST import aBST


class WideAllNodes_aBSTTests(unittest.TestCase):

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

    def test_regression_WideAllNodes(self):
        self.assertEqual(
            self.tree.WideAllNodes(),
            (50, 25, 75, 37, 62, 84, 31, 43, 55, 92),
        )


if __name__ == "__main__":
    unittest.main()
