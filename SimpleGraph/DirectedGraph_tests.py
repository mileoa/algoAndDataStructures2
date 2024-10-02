import unittest
import random

from DirectedGraph import DirectedGraph


class DirectedGraphTests(unittest.TestCase):

    def test_regression_AddVertex(self):
        graph: DirectedGraph = DirectedGraph(3)
        graph.AddVertex(3)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                self.assertEqual(relation, 0)
                if first_index == 0 and second_index == 0:
                    self.assertEqual(graph.vertex[first_index].Value, 3)
                    continue
                if first_index == second_index:
                    self.assertIsNone(graph.vertex[first_index])

        graph.AddVertex(4)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                self.assertEqual(relation, 0)
                if first_index == 0 and second_index == 0:
                    self.assertEqual(graph.vertex[first_index].Value, 3)
                    continue
                if first_index == 1 and second_index == 1:
                    self.assertEqual(graph.vertex[first_index].Value, 4)
                    continue
                if first_index == second_index:
                    self.assertIsNone(graph.vertex[first_index])

        graph.AddVertex(5)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                self.assertEqual(relation, 0)
                if first_index == 0 and second_index == 0:
                    self.assertEqual(graph.vertex[first_index].Value, 3)
                    continue
                if first_index == 1 and second_index == 1:
                    self.assertEqual(graph.vertex[first_index].Value, 4)
                    continue
                if first_index == 2 and second_index == 2:
                    self.assertEqual(graph.vertex[first_index].Value, 5)
                    continue
                if first_index == second_index:
                    self.assertIsNone(graph.vertex[first_index])

        graph.AddVertex(6)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                self.assertEqual(relation, 0)
                if first_index == 0 and second_index == 0:
                    self.assertEqual(graph.vertex[first_index].Value, 3)
                    continue
                if first_index == 1 and second_index == 1:
                    self.assertEqual(graph.vertex[first_index].Value, 4)
                    continue
                if first_index == 2 and second_index == 2:
                    self.assertEqual(graph.vertex[first_index].Value, 5)
                    continue
                if first_index == second_index:
                    self.assertIsNone(graph.vertex[first_index])

    def test_regression_AddEdge(self):
        graph: DirectedGraph = DirectedGraph(4)
        graph.AddVertex(0)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)

        graph.AddEdge(1, 3)
        graph.AddEdge(2, 1)
        graph.AddEdge(2, 2)

        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                if (
                    (first_index == 1 and second_index == 3)
                    or (first_index == 2 and second_index == 1)
                    or (first_index == 2 and second_index == 2)
                ):
                    self.assertEqual(relation, 1)
                    continue
                self.assertEqual(relation, 0)

    def test_regression_IsEdge(self):
        graph: DirectedGraph = DirectedGraph(4)
        graph.AddVertex(0)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)

        graph.AddEdge(1, 3)
        graph.AddEdge(2, 1)
        graph.AddEdge(2, 2)

        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                if (
                    (first_index == 1 and second_index == 3)
                    or (first_index == 2 and second_index == 1)
                    or (first_index == 2 and second_index == 2)
                ):
                    self.assertTrue(graph.IsEdge(first_index, second_index))
                    continue
                self.assertFalse(graph.IsEdge(first_index, second_index))

    def test_regression_RemoveEdge(self):
        graph: DirectedGraph = DirectedGraph(4)
        graph.AddVertex(0)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)

        graph.AddEdge(1, 3)
        graph.AddEdge(2, 1)
        graph.AddEdge(2, 2)

        graph.RemoveEdge(1, 3)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                if (first_index == 2 and second_index == 1) or (
                    first_index == 2 and second_index == 2
                ):
                    self.assertEqual(relation, 1)
                    continue
                self.assertEqual(relation, 0)

    def test_regression_RemoveVertex(self):
        graph: DirectedGraph = DirectedGraph(4)
        graph.AddVertex(0)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)

        graph.AddEdge(1, 3)
        graph.AddEdge(2, 1)
        graph.AddEdge(2, 2)
        graph.AddEdge(1, 2)

        graph.RemoveVertex(2)

        self.assertEqual(graph.vertex[0].Value, 0)
        self.assertEqual(graph.vertex[1].Value, 10)
        self.assertIsNone(graph.vertex[2])
        self.assertEqual(graph.vertex[3].Value, 30)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                if first_index == 1 and second_index == 3:
                    self.assertEqual(relation, 1)
                    continue
                self.assertEqual(relation, 0)

    def test_regression_is_cyclic(self):
        graph: DirectedGraph = DirectedGraph(4)
        graph.AddVertex(0)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)

        graph.AddEdge(1, 3)
        graph.AddEdge(2, 1)
        self.assertFalse(graph.is_cyclic())

        graph.AddEdge(0, 0)
        self.assertTrue(graph.is_cyclic())

        graph.RemoveEdge(0, 0)
        graph.AddEdge(2, 3)

        self.assertFalse(graph.is_cyclic())
        graph.AddEdge(3, 2)
        self.assertTrue(graph.is_cyclic())


if __name__ == "__main__":
    unittest.main()
