import unittest

from SimpleGraph import SimpleGraph, Vertex


class SimpleGraphTests(unittest.TestCase):

    def test_regression_AddVertex(self):
        graph: SimpleGraph = SimpleGraph(3)
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
        graph: SimpleGraph = SimpleGraph(3)
        graph.AddVertex(0)
        graph.AddVertex(10)
        graph.AddVertex(20)

        self.assertEqual(graph.m_adjacency[1][2], 0)
        self.assertEqual(graph.m_adjacency[2][1], 0)

        graph.AddEdge(1, 2)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                if (
                    (first_index == 1 and second_index == 2)
                    or first_index == 2
                    and second_index == 1
                ):
                    self.assertEqual(relation, 1)
                    self.assertEqual(relation, 1)
                    continue
                self.assertEqual(relation, 0)

    def test_border_AddEdge(self):
        graph: SimpleGraph = SimpleGraph(3)
        graph.AddVertex(0)
        graph.AddVertex(10)
        graph.AddVertex(20)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                self.assertEqual(relation, 0)
        graph.AddEdge(1, 3)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                self.assertEqual(relation, 0)

    def test_regression_RemoveEdge(self):
        graph: SimpleGraph = SimpleGraph(4)
        graph.AddVertex(0)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)

        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)

        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                if (
                    (first_index == 1 and second_index == 2)
                    or (first_index == 2 and second_index == 1)
                    or (first_index == 2 and second_index == 3)
                    or (first_index == 3 and second_index == 2)
                ):
                    self.assertEqual(relation, 1)
                    self.assertEqual(relation, 1)
                    continue
                self.assertEqual(relation, 0)

        graph.RemoveEdge(1, 2)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                if (
                    (first_index == 2 and second_index == 3)
                    or first_index == 3
                    and second_index == 2
                ):
                    self.assertEqual(relation, 1)
                    self.assertEqual(relation, 1)
                    continue
                self.assertEqual(relation, 0)

    def test_border_RemoveEdge(self):
        graph: SimpleGraph = SimpleGraph(4)
        graph.AddVertex(0)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)

        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)

        graph.RemoveEdge(0, 4)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                if (
                    (first_index == 1 and second_index == 2)
                    or (first_index == 2 and second_index == 1)
                    or (first_index == 2 and second_index == 3)
                    or (first_index == 3 and second_index == 2)
                ):
                    self.assertEqual(relation, 1)
                    self.assertEqual(relation, 1)
                    continue
                self.assertEqual(relation, 0)

    def test_regression_IsEdge(self):
        graph: SimpleGraph = SimpleGraph(4)
        graph.AddVertex(0)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)

        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)

        self.assertFalse(graph.IsEdge(1, 5))

        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                if (
                    (first_index == 1 and second_index == 2)
                    or (first_index == 2 and second_index == 1)
                    or (first_index == 2 and second_index == 3)
                    or (first_index == 3 and second_index == 2)
                ):
                    self.assertTrue(graph.IsEdge(first_index, second_index))
                    continue
                self.assertFalse(graph.IsEdge(first_index, second_index))

    def test_regression_RemoveVertex(self):
        graph: SimpleGraph = SimpleGraph(4)
        graph.AddVertex(0)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)

        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)

        graph.RemoveVertex(2)
        self.assertEqual(graph.vertex[0].Value, 0)
        self.assertEqual(graph.vertex[1].Value, 10)
        self.assertIsNone(graph.vertex[2])
        self.assertEqual(graph.vertex[3].Value, 30)
        for first_index, first_demension in enumerate(graph.m_adjacency):
            for second_index, relation in enumerate(first_demension):
                self.assertEqual(relation, 0)


if __name__ == "__main__":
    unittest.main()
