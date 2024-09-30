import unittest
import random

from Heap import Heap


class HeapTests(unittest.TestCase):

    def setUp(self) -> None:
        self.heap = Heap()

    def test_regression_MakeHeap(self):
        self.heap.MakeHeap([0], 0)
        self.assertEqual(self.heap.HeapArray, [0])
        self.assertEqual(len(self.heap.HeapArray), 1)

        self.heap.MakeHeap([3, 2, 5], 1)
        self.assertEqual(self.heap.HeapArray, [5, 3, 2])
        self.assertEqual(len(self.heap.HeapArray), 3)

        self.heap.MakeHeap([75, 62, 84, 37, 25, 50, 20], 2)
        self.assertEqual(self.heap.HeapArray, [84, 75, 62, 50, 37, 25, 20])
        self.assertEqual(len(self.heap.HeapArray), 7)

    def test_regression_GetMax(self):
        self.heap.MakeHeap([84, 75, 62, 50, 37, 25, 20], 2)
        self.assertEqual(self.heap.GetMax(), 84)
        self.assertEqual(self.heap.HeapArray, [75, 50, 62, 20, 37, 25, None])
        self.assertEqual(self.heap.GetMax(), 75)
        self.assertEqual(self.heap.HeapArray, [62, 50, 25, 20, 37, None, None])
        self.assertEqual(self.heap.GetMax(), 62)
        self.assertEqual(self.heap.HeapArray, [50, 37, 25, 20, None, None, None])
        self.assertEqual(self.heap.GetMax(), 50)
        self.assertEqual(self.heap.HeapArray, [37, 20, 25, None, None, None, None])
        self.assertEqual(self.heap.GetMax(), 37)
        self.assertEqual(self.heap.HeapArray, [25, 20, None, None, None, None, None])
        self.assertEqual(self.heap.GetMax(), 25)
        self.assertEqual(self.heap.HeapArray, [20, None, None, None, None, None, None])
        self.assertEqual(self.heap.GetMax(), 20)
        self.assertEqual(
            self.heap.HeapArray, [None, None, None, None, None, None, None]
        )
        self.assertEqual(self.heap.GetMax(), -1)
        self.assertEqual(
            self.heap.HeapArray, [None, None, None, None, None, None, None]
        )


if __name__ == "__main__":
    unittest.main()
