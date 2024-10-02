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

    def test_empty(self):
        pass

    def test_random(self):
        pass

    def test_border(self):
        pass


if __name__ == "__main__":
    unittest.main()
