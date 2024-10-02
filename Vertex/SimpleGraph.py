from typing import Optional


class Vertex:

    def __init__(self, val: int) -> None:
        self.Value: int = val


class SimpleGraph:

    def __init__(self, size: int) -> None:
        self.max_vertex: int = size
        self.m_adjacency: list[list[int]] = [[0] * size for _ in range(size)]
        self.vertex: list[Optional[Vertex]] = [None] * size

    def AddVertex(self, v: int) -> None:
        if self.vertex.count(None) == 0:
            return None
        first_occurance_of_none: int = self.vertex.index(None)
        self.vertex[first_occurance_of_none] = Vertex(v)
        return None

    def RemoveVertex(self, v: int) -> None:
        # ваш код удаления вершины со всеми её рёбрами
        pass

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
