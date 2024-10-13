from typing import Optional, List
from collections import deque


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

    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> List[Vertex]:
        self.unhit_all_vertexes()
        return self._BreadthFirstSearch_recursive(
            VFrom, VTo, deque([[VFrom, [self.vertex[VFrom]]]])
        )

    def _BreadthFirstSearch_recursive(
        self, VFrom: int, VTo: int, queue: deque
    ) -> List[Vertex]:
        current_vertex_index: int
        current_path: List[Vertex]
        current_vertex_index, current_path = queue.popleft()
        self.vertex[VFrom].hit = True

        for i, relation in enumerate(self.m_adjacency[current_vertex_index]):
            if relation == 1 and i == VTo:
                return current_path + [self.vertex[VTo]]
            if relation == 1 and not self.vertex[i].hit:
                queue.append(
                    [
                        i,
                        current_path + [self.vertex[i]],
                    ]
                )
        if len(queue) == 0:
            return []

        return self._BreadthFirstSearch_recursive(current_vertex_index, VTo, queue)

    def find_farthest_vertexes_path_len(self) -> int:
        if self.vertex.count(None) == len(self.vertex):
            return 0

        max_path_len: int = 0
        for v_index, v in enumerate(self.vertex):
            if v is None:
                continue
            farthest_vertex_path_len: int = (
                len(self.find_farthest_vertex_from_given(v_index)) - 1
            )
            max_path_len = max(max_path_len, farthest_vertex_path_len)
        return max_path_len

    def find_farthest_vertex_from_given(self, given_index: int) -> List[Vertex]:
        path_to_farthest_vertex: List[Vertex] = []
        for i, v in enumerate(self.vertex):
            if v is None:
                continue
            path_to_v: List[Vertex] = self.BreadthFirstSearch(given_index, i)
            if len(path_to_v) > len(path_to_farthest_vertex):
                path_to_farthest_vertex = path_to_v
        return path_to_farthest_vertex

    def find_all_cycles(self) -> List[List[int]]:
        if self.vertex.count(None) == len(self.vertex):
            return []
        all_cycles: List[List[int]] = []
        for i, node in enumerate(self.vertex):
            if node is None:
                continue
            all_cycles.extend(
                self.find_all_cycles_from_node_recursive(i, deque([[node, [i]]]), [])
            )
        return list(filter(lambda cycle: cycle != [], all_cycles))

    def find_all_cycles_from_node_recursive(
        self, start_index: int, queue: deque, cycle: List[List[int]]
    ) -> List[List[int]]:
        current_node: Vertex
        current_path: List[int]
        current_node, current_path = queue.popleft()
        for i, relation in enumerate(self.m_adjacency[self.vertex.index(current_node)]):
            if relation == 1 and i == start_index and len(current_path) > 2:
                cycle.append(current_path + [start_index])
            if relation == 1 and i not in current_path:
                queue.append([self.vertex[i], current_path + [i]])

        if len(queue) == 0:
            return cycle
        return self.find_all_cycles_from_node_recursive(start_index, queue, cycle)

    def unhit_all_vertexes(self) -> None:
        for v in self.vertex:
            if v is None:
                continue
            v.hit = False
