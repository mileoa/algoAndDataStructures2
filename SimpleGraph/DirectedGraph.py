from SimpleGraph import SimpleGraph, Vertex


class DirectedGraph(SimpleGraph):

    def __init__(self, size: int):
        super().__init__(size)

    def RemoveVertex(self, v: int) -> None:
        if v >= self.max_vertex or v < 0:
            return None
        for i, demension in enumerate(self.m_adjacency):
            self.RemoveEdge(i, v)
            self.RemoveEdge(v, i)
        # Must set to None after deleting edges because
        # RemoveEdge checks if node on given index is None.
        self.vertex[v] = None
        return None

    def IsEdge(self, v1: int, v2: int) -> bool:
        if v1 >= self.max_vertex or v2 >= self.max_vertex or v1 < 0 or v2 < 0:
            return False
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1: int, v2: int) -> None:
        if v1 >= self.max_vertex or v2 >= self.max_vertex or v1 < 0 or v2 < 0:
            return None
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return None
        self.m_adjacency[v1][v2] = 1
        return None

    def RemoveEdge(self, v1: int, v2: int) -> None:
        if v1 >= self.max_vertex or v2 >= self.max_vertex or v1 < 0 or v2 < 0:
            return None
        if self.vertex[v1] is None or self.vertex[v2] is None:
            return None
        self.m_adjacency[v1][v2] = 0
        return None

    def is_cyclic(self) -> bool:
        is_cyclic_graph: bool = False
        for v, element in enumerate(self.vertex):
            if element is None:
                continue
            is_cyclic_graph = is_cyclic_graph or self._is_cyclic_recursive(v, [])
            if is_cyclic_graph:
                break
        return is_cyclic_graph

    def _is_cyclic_recursive(self, v, visited_v: list[int]) -> bool:
        if v in visited_v:
            return True
        v_to_visit: list[int] = []
        for i, relation in enumerate(self.m_adjacency[v]):
            if relation == 0:
                continue
            v_to_visit.append(i)

        is_cyclic_graph: bool = False
        for i in v_to_visit:
            is_cyclic_graph = is_cyclic_graph or self._is_cyclic_recursive(
                i, visited_v + [v]
            )
            if is_cyclic_graph:
                break

        return is_cyclic_graph
