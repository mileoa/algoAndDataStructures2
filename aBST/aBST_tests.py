import unittest
import random

from aBST import aBST


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

    def test_regression_init(self):
        first_tree: aBST = aBST(0)
        self.assertEqual(len(first_tree.Tree), 1)

        second_tree: aBST = aBST(1)
        self.assertEqual(len(second_tree.Tree), 3)

        third_tree: aBST = aBST(10)
        self.assertEqual(len(third_tree.Tree), 2047)

        fourth_tree: aBST = aBST(3)
        self.assertEqual(len(fourth_tree.Tree), 15)

    def test_regression_FindKeyIndex(self):
        self.assertEqual(self.tree.FindKeyIndex(50), 0)
        self.assertEqual(self.tree.FindKeyIndex(31), 9)
        self.assertEqual(self.tree.FindKeyIndex(55), 11)
        self.assertEqual(self.tree.FindKeyIndex(92), 14)

        self.assertIsNone(self.tree.FindKeyIndex(30))
        self.assertIsNone(self.tree.FindKeyIndex(54))
        self.assertIsNone(self.tree.FindKeyIndex(93))

        self.assertEqual(self.tree.FindKeyIndex(23), -3)
        self.assertEqual(self.tree.FindKeyIndex(63), -12)
        self.assertEqual(self.tree.FindKeyIndex(83), -13)

    def test_regression_AddKey(self):
        self.assertEqual(self.tree.AddKey(61), -1)
        self.assertEqual(
            self.tree.Tree,
            [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92],
        )

        self.assertEqual(self.tree.AddKey(63), 12)
        self.assertEqual(
            self.tree.Tree,
            [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, 63, None, 92],
        )

        self.assertEqual(self.tree.AddKey(93), -1)
        self.assertEqual(
            self.tree.Tree,
            [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, 63, None, 92],
        )

        self.assertEqual(self.tree.AddKey(24), 3)
        self.assertEqual(
            self.tree.Tree,
            [50, 25, 75, 24, 37, 62, 84, None, None, 31, 43, 55, 63, None, 92],
        )

        self.assertEqual(self.tree.AddKey(75), 2)
        self.assertEqual(
            self.tree.Tree,
            [50, 25, 75, 24, 37, 62, 84, None, None, 31, 43, 55, 63, None, 92],
        )

    def test_empty_AddKey(self):
        empty_tree: aBST = aBST(3)
        self.assertEqual(empty_tree.AddKey(100), 0)
        self.assertEqual(empty_tree.Tree, [100] + [None] * (len(empty_tree.Tree) - 1))


if __name__ == "__main__":
    unittest.main()
