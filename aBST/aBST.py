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
