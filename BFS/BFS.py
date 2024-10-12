from typing import Optional


class Vertex:

    def __init__(self, val: int) -> None:
        self.Value: int = val
        self.hit: bool = False


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

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> list[Vertex]:
        self.unhit_all_vertexes()
        return self._DepthFirstSearch_recursive(VFrom, VTo, [])

    def _DepthFirstSearch_recursive(
        self, VFrom: int, VTo: int, path_stack: list[Vertex]
    ) -> list[Vertex]:
        if not self.vertex[VFrom].hit:
            path_stack.append(self.vertex[VFrom])
        self.vertex[VFrom].hit = True
        for i, relation in enumerate(self.m_adjacency[VFrom]):
            if relation == 1 and i == VTo:
                return path_stack + [self.vertex[VTo]]
            if relation == 1 and not self.vertex[i].hit:
                return self._DepthFirstSearch_recursive(i, VTo, path_stack)
        path_stack.pop()
        if len(path_stack) == 0:
            return []
        return self._DepthFirstSearch_recursive(
            self.vertex.index(path_stack[-1]), VTo, path_stack
        )

    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> list[Vertex]:
        self.unhit_all_vertexes()
        return self._BreadthFirstSearch_recursive(
            VFrom, VTo, [[VFrom, [self.vertex[VFrom]]]]
        )

    def _BreadthFirstSearch_recursive(
        self, VFrom: int, VTo: int, queue: list[int, list[Vertex]]
    ) -> list[Vertex]:
        current_vertex_index: int
        current_path: list[Vertex]
        current_vertex_index, current_path = queue.pop(0)
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

        path_lenghts: list[int] = []
        for v_index, v in enumerate(self.vertex):
            if v is None:
                continue
            self.unhit_all_vertexes()
            path_lenghts.append(
                self.find_farthest_vertexes_path_len_from_node_recursive(
                    v_index, [[v, 0]], 0
                )
            )
        return max(path_lenghts)

    def find_farthest_vertexes_path_len_from_node_recursive(
        self, start_index: int, queue: list[Vertex, list[int]], max_distance: int
    ) -> int:
        current_node: Vertex
        current_distance: int
        current_node, current_distance = queue.pop(0)
        current_node.hit = True

        max_distance = max(current_distance, max_distance)
        for i, relation in enumerate(self.m_adjacency[self.vertex.index(current_node)]):
            if relation == 1 and not self.vertex[i].hit:
                queue.append([self.vertex[i], current_distance + 1])

        if len(queue) == 0:
            return max_distance
        return self.find_farthest_vertexes_path_len_from_node_recursive(
            start_index, queue, max_distance
        )

    def find_all_cycles(self) -> list[list[int]]:
        if self.vertex.count(None) == len(self.vertex):
            return []
        all_cycles: list[list[int]] = []
        for i, node in enumerate(self.vertex):
            if node is None:
                continue
            all_cycles.extend(
                self.find_all_cycles_from_node_recursive(i, [[node, [i]]], [])
            )
        return filter(lambda cycle: cycle != [], all_cycles)

    def find_all_cycles_from_node_recursive(
        self, start_index: int, queue: list[Vertex, list[int]], cycle: list[int]
    ) -> list[int]:
        current_node: Vertex
        current_path: list[int]
        current_node, current_path = queue.pop(0)
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
