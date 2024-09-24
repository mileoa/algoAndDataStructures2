from typing import Optional


class aBST:

    def __init__(self, depth: int) -> None:
        tree_size: int = pow(2, depth + 1) - 1
        self.Tree: list[Optional[int]] = [None] * tree_size

    def FindKeyIndex(self, key: int) -> Optional[int]:
        return self._FindKeyIndex_recursive(key, 0)

    def _FindKeyIndex_recursive(
        self, key: int, current_node_index: int
    ) -> Optional[int]:
        if current_node_index > len(self.Tree):
            return None
        if self.Tree[current_node_index] == key:
            return current_node_index
        if self.Tree[current_node_index] is None:
            return -current_node_index
        if self.Tree[current_node_index] > key:
            return self._FindKeyIndex_recursive(key, 2 * current_node_index + 1)
        return self._FindKeyIndex_recursive(key, 2 * current_node_index + 2)

    def AddKey(self, key: int) -> int:
        index_for_insertion: Optional[int] = self.FindKeyIndex(key)
        if index_for_insertion is None:
            return -1
        self.Tree[abs(index_for_insertion)] = key
        return abs(index_for_insertion)

    def LCA(self, first_node_index: int, second_node_index: int) -> Optional[int]:
        first_node_parents_inedexes: list[int] = []
        firtst_parent_index: int = (first_node_index - 1) // 2
        while firtst_parent_index >= 0:
            first_node_parents_inedexes.append(firtst_parent_index)
            firtst_parent_index = (firtst_parent_index - 1) // 2

        second_node_parents_inedexes: list[int] = []
        second_parent_index: int = (second_node_index - 1) // 2
        while second_parent_index >= 0:
            second_node_parents_inedexes.append(second_parent_index)
            second_parent_index = (second_parent_index - 1) // 2

        lowest_parent_index: int = -1
        for i in range(
            min(len(first_node_parents_inedexes), len(second_node_parents_inedexes))
        ):
            if (
                first_node_parents_inedexes[-(i + 1)]
                == second_node_parents_inedexes[-(i + 1)]
            ):
                lowest_parent_index = first_node_parents_inedexes[-(i + 1)]
        if lowest_parent_index == -1:
            return None
        return lowest_parent_index
