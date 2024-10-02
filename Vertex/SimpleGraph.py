class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size: int):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v: int):
        if self.vertex.count(None) == 0:
            return None
        first_occurance_of_none: int = self.vertex.index(None)
        self.vertex[first_occurance_of_none] = Vertex(v)
        return None

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        pass

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        pass

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        pass
