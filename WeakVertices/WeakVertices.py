from typing import Optional, List


class Vertex:

    def __init__(self, val: int) -> None:
        self.Value: int = val
        self.hit: bool = False


class SimpleGraph:

    def __init__(self, size: int) -> None:
        self.max_vertex: int = size
        self.m_adjacency: List[List[int]] = [[0] * size for _ in range(size)]
        self.vertex: List[Optional[Vertex]] = [None] * size

    def AddVertex(self, v: int) -> None:
        if self.vertex.count(None) == 0:
            return None
        first_occurance_of_none: int = self.vertex.index(None)
        self.vertex[first_occurance_of_none] = Vertex(v)
        return None

    def RemoveVertex(self, v: int) -> None:
        if v >= self.max_vertex or v < 0:
            return None
        for i, demension in enumerate(self.m_adjacency):
            if self.m_adjacency[i][v] == 0:
                continue
            self.RemoveEdge(i, v)
        # Must set to None after deleting edges because
        # RemoveEdge checks if node on given index is None.
        self.vertex[v] = None
        return None

    def IsEdge(self, v1: int, v2: int) -> bool:
        if v1 >= self.max_vertex or v2 >= self.max_vertex or v1 < 0 or v2 < 0:
            return False
        return self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1

    def AddEdge(self, v1: int, v2: int) -> None:
        if v1 >= self.max_vertex or v2 >= self.max_vertex or v1 < 0 or v2 < 0:
            return None
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return None
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        return None

    def RemoveEdge(self, v1: int, v2: int) -> None:
        if v1 >= self.max_vertex or v2 >= self.max_vertex or v1 < 0 or v2 < 0:
            return None
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return None
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        return None

    def WeakVertices(self) -> List[Vertex]:
        return [v for v in self.vertex if not self.is_part_of_triangle(v)]

    def is_part_of_triangle(self, examined_vertex: Vertex) -> bool:
        if examined_vertex is None:
            return False

        vertex_connected: List[Vertex] = [
            self.vertex[v_index]
            for v_index, relation in enumerate(
                self.m_adjacency[self.vertex.index(examined_vertex)]
            )
            if relation == 1
        ]
        for v in vertex_connected:
            for i, relation in enumerate(self.m_adjacency[self.vertex.index(v)]):
                if relation == 1 and self.vertex[i] in vertex_connected:
                    return True
        return False
