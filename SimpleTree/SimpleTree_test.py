import unittest
import random

from SimpleTree import SimpleTree, SimpleTreeNode


class SimpleTreeTests(unittest.TestCase):

    def setUp(self):
        self.simple_tree = SimpleTree(None)

    def test_regression_AddChild(self):
        root = SimpleTreeNode(0, None)
        first_child = SimpleTreeNode(1, None)
        second_child = SimpleTreeNode(2, None)
        first_child_child = SimpleTreeNode(3, None)

        self.simple_tree.AddChild(None, root)
        self.simple_tree.AddChild(root, first_child)
        self.simple_tree.AddChild(root, second_child)
        self.simple_tree.AddChild(first_child, first_child_child)

        self.assertEqual(root.Children, [first_child, second_child])
        self.assertEqual(root.Parent, None)

        self.assertEqual(first_child.Parent, root)
        self.assertEqual(first_child.Children, [first_child_child])

        self.assertEqual(second_child.Parent, root)
        self.assertEqual(second_child.Children, [])

        self.assertEqual(first_child_child.Parent, first_child)
        self.assertEqual(first_child_child.Children, [])

    def test_empty_AddChild(self):
        root = SimpleTreeNode(0, None)
        self.simple_tree.AddChild(None, root)
        self.assertEqual(root.Children, [])
        self.assertEqual(root.Parent, None)

    def test_border_AddChild(self):
        first_root = SimpleTreeNode(0, None)
        second_root = SimpleTreeNode(1, None)

        self.simple_tree.AddChild(None, first_root)
        self.simple_tree.AddChild(None, second_root)

        self.assertEqual(first_root.Children, [])
        self.assertEqual(first_root.Parent, second_root)

        self.assertEqual(second_root.Children, [first_root])
        self.assertEqual(second_root.Parent, None)

    def test_regression_DeleteNode(self):
        root = SimpleTreeNode(0, None)
        first_child = SimpleTreeNode(1, None)
        second_child = SimpleTreeNode(2, None)
        first_child_first_child = SimpleTreeNode(3, None)
        first_child_second_child = SimpleTreeNode(4, None)
        first_child_second_child_first_child = SimpleTreeNode(2, None)
        self.simple_tree.AddChild(None, root)
        self.simple_tree.AddChild(root, first_child)
        self.simple_tree.AddChild(root, second_child)
        self.simple_tree.AddChild(first_child, first_child_first_child)
        self.simple_tree.AddChild(first_child, first_child_second_child)
        self.simple_tree.AddChild(
            first_child_second_child, first_child_second_child_first_child
        )

        self.simple_tree.DeleteNode(first_child)

        self.assertEqual(root.Children, [second_child])

        self.assertEqual(first_child.Children, [])
        self.assertEqual(first_child.Parent, None)

        self.assertEqual(first_child_first_child.Parent, None)

        self.assertEqual(first_child_second_child.Children, [])
        self.assertEqual(first_child_second_child.Parent, None)

        self.assertEqual(first_child_second_child_first_child.Parent, None)

    def test_regression_GetAllNodes(self):
        root = SimpleTreeNode(0, None)
        first_child = SimpleTreeNode(1, None)
        second_child = SimpleTreeNode(2, None)
        first_child_first_child = SimpleTreeNode(3, None)
        first_child_second_child = SimpleTreeNode(4, None)
        first_child_second_child_first_child = SimpleTreeNode(2, None)
        self.simple_tree.AddChild(None, root)
        self.simple_tree.AddChild(root, first_child)
        self.simple_tree.AddChild(root, second_child)
        self.simple_tree.AddChild(first_child, first_child_first_child)
        self.simple_tree.AddChild(first_child, first_child_second_child)
        self.simple_tree.AddChild(
            first_child_second_child, first_child_second_child_first_child
        )

        self.assertCountEqual(
            self.simple_tree.GetAllNodes(),
            [
                root,
                first_child,
                second_child,
                first_child_first_child,
                first_child_second_child,
                first_child_second_child_first_child,
            ],
        )

    def test_empty_GetAllNodes(self):
        self.assertCountEqual(self.simple_tree.GetAllNodes(), [])

    def test_regression_FindNodesByValue(self):
        root = SimpleTreeNode(0, None)
        first_child = SimpleTreeNode(1, None)
        second_child = SimpleTreeNode(2, None)
        first_child_first_child = SimpleTreeNode(3, None)
        first_child_second_child = SimpleTreeNode(4, None)
        first_child_second_child_first_child = SimpleTreeNode(2, None)
        self.simple_tree.AddChild(None, root)
        self.simple_tree.AddChild(root, first_child)
        self.simple_tree.AddChild(root, second_child)
        self.simple_tree.AddChild(first_child, first_child_first_child)
        self.simple_tree.AddChild(first_child, first_child_second_child)
        self.simple_tree.AddChild(
            first_child_second_child, first_child_second_child_first_child
        )

        self.assertCountEqual(self.simple_tree.FindNodesByValue(0), [root])
        self.assertCountEqual(
            self.simple_tree.FindNodesByValue(2),
            [second_child, first_child_second_child_first_child],
        )
        self.assertCountEqual(self.simple_tree.FindNodesByValue(-1), [])

    def test_regression_MoveNode(self):
        root = SimpleTreeNode(0, None)
        first_child = SimpleTreeNode(1, None)
        second_child = SimpleTreeNode(2, None)
        first_child_first_child = SimpleTreeNode(3, None)
        first_child_second_child = SimpleTreeNode(4, None)
        first_child_second_child_first_child = SimpleTreeNode(2, None)
        self.simple_tree.AddChild(None, root)
        self.simple_tree.AddChild(root, first_child)
        self.simple_tree.AddChild(root, second_child)
        self.simple_tree.AddChild(first_child, first_child_first_child)
        self.simple_tree.AddChild(first_child, first_child_second_child)
        self.simple_tree.AddChild(
            first_child_second_child, first_child_second_child_first_child
        )

        self.simple_tree.MoveNode(first_child, second_child)

        self.assertCountEqual(
            first_child.Children, [first_child_first_child, first_child_second_child]
        )
        self.assertEqual(first_child.Parent, second_child)

        self.assertCountEqual(second_child.Children, [first_child])

        self.assertEqual(first_child_first_child.Parent, first_child)
        self.assertEqual(first_child_first_child.Children, [])

        self.assertEqual(first_child_second_child.Parent, first_child)
        self.assertEqual(
            first_child_second_child.Children, [first_child_second_child_first_child]
        )

        self.assertEqual(
            first_child_second_child_first_child.Parent, first_child_second_child
        )
        self.assertEqual(first_child_second_child_first_child.Children, [])

    def test_regression_Count(self):
        root = SimpleTreeNode(0, None)
        first_child = SimpleTreeNode(1, None)
        second_child = SimpleTreeNode(2, None)
        first_child_first_child = SimpleTreeNode(3, None)
        first_child_second_child = SimpleTreeNode(4, None)
        first_child_second_child_first_child = SimpleTreeNode(2, None)
        self.simple_tree.AddChild(None, root)
        self.simple_tree.AddChild(root, first_child)
        self.simple_tree.AddChild(root, second_child)
        self.simple_tree.AddChild(first_child, first_child_first_child)
        self.simple_tree.AddChild(first_child, first_child_second_child)
        self.simple_tree.AddChild(
            first_child_second_child, first_child_second_child_first_child
        )

        self.assertEqual(self.simple_tree.Count(), 6)

    def test_empty_Count(self):
        self.assertEqual(self.simple_tree.Count(), 0)

    def test_regression_LeafCount(self):
        root = SimpleTreeNode(0, None)
        first_child = SimpleTreeNode(1, None)
        second_child = SimpleTreeNode(2, None)
        first_child_first_child = SimpleTreeNode(3, None)
        first_child_second_child = SimpleTreeNode(4, None)
        first_child_second_child_first_child = SimpleTreeNode(2, None)
        self.simple_tree.AddChild(None, root)
        self.simple_tree.AddChild(root, first_child)
        self.simple_tree.AddChild(root, second_child)
        self.simple_tree.AddChild(first_child, first_child_first_child)
        self.simple_tree.AddChild(first_child, first_child_second_child)
        self.simple_tree.AddChild(
            first_child_second_child, first_child_second_child_first_child
        )

        self.assertEqual(self.simple_tree.LeafCount(), 3)

    def test_empty_LeafCount(self):
        self.assertEqual(self.simple_tree.LeafCount(), 0)


if __name__ == "__main__":
    unittest.main()
