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
        self.assertEqual(self.heap.HeapArray, [5, 2, 3])
        self.assertEqual(len(self.heap.HeapArray), 3)

        self.heap.MakeHeap([75, 62, 84, 37, 25, 50, 20], 2)
        self.assertEqual(self.heap.HeapArray, [84, 62, 75, 37, 25, 50, 20])
        self.assertEqual(len(self.heap.HeapArray), 7)

        self.heap.MakeHeap([75, 62, 84, 37, None, None, None], 2)
        self.assertEqual(self.heap.HeapArray, [84, 62, 75, 37, None, None, None])
        self.assertEqual(len(self.heap.HeapArray), 7)

        self.heap.MakeHeap([75, 62, 84, 37], 2)
        self.assertEqual(self.heap.HeapArray, [84, 62, 75, 37, None, None, None])
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

    def test_regression_Add(self):
        self.heap.HeapArray = [1, None, None, None, None, None, None]
        self.assertTrue(self.heap.Add(3))
        self.assertEqual(self.heap.HeapArray, [3, 1, None, None, None, None, None])
        self.assertTrue(self.heap.Add(5))
        self.assertEqual(self.heap.HeapArray, [5, 1, 3, None, None, None, None])
        self.assertTrue(self.heap.Add(7))
        self.assertEqual(self.heap.HeapArray, [7, 5, 3, 1, None, None, None])
        self.assertTrue(self.heap.Add(0))
        self.assertEqual(self.heap.HeapArray, [7, 5, 3, 1, 0, None, None])
        self.assertTrue(self.heap.Add(3))
        self.assertEqual(self.heap.HeapArray, [7, 5, 3, 1, 0, 3, None])
        self.assertTrue(self.heap.Add(10))
        self.assertEqual(self.heap.HeapArray, [10, 5, 7, 1, 0, 3, 3])
        self.assertFalse(self.heap.Add(2))

    def test_regression_is_valid(self):
        self.heap.MakeHeap([75, 62, 84, 37, 25, 50, 20], 2)
        self.assertTrue(self.heap.is_valid())
        self.heap.HeapArray[5] = 76
        self.assertFalse(self.heap.is_valid())

    def test_regression_find_max_in_range(self):
        self.heap.MakeHeap([75, 62, 84, 37, 25, 50, 20], 2)
        self.assertEqual(self.heap.find_max_in_range(0, 1), -1)
        self.assertEqual(self.heap.find_max_in_range(37, 37), 37)
        self.assertEqual(self.heap.find_max_in_range(21, 60), 50)

    def test_empty_find_max_in_range(self):
        empty_heap = Heap()
        empty_heap.MakeHeap([], 2)
        self.assertEqual(empty_heap.find_max_in_range(0, 10000), -1)

    def test_regression_union_from_heap(self):
        heap_one = Heap()
        heap_one.MakeHeap([75, 62, 84], 1)
        heap_two = Heap()
        heap_two.MakeHeap([37, 25, 50], 1)
        heap_three = Heap()
        heap_three.MakeHeap([20], 0)

        heap_one.union_from_heap(heap_two)
        self.assertEqual(len(heap_one.HeapArray), 7)
        self.assertCountEqual(heap_one.HeapArray, [75, 62, 84, 37, 25, 50, None])
        heap_one.union_from_heap(heap_three)
        self.assertEqual(len(heap_one.HeapArray), 7)
        self.assertCountEqual(heap_one.HeapArray, [75, 62, 84, 37, 25, 50, 20])


if __name__ == "__main__":
    unittest.main()
