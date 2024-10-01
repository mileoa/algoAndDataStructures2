from typing import Optional


class Heap:

    def __init__(self) -> None:
        self.HeapArray: list[Optional[int]] = []

    def MakeHeap(self, a: list[int], depth: int) -> None:
        heap_size: int = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * heap_size
        for node in a:
            if node is None:
                continue
            self.Add(node)

    def GetMax(self) -> int:
        if self.HeapArray.count(None) == len(self.HeapArray):
            return -1
        last_nonempty_element_index: int = max(
            index for index, value in enumerate(self.HeapArray) if value is not None
        )
        assert self.HeapArray[0] is not None
        max_element: int = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[last_nonempty_element_index]
        self.HeapArray[last_nonempty_element_index] = None
        if last_nonempty_element_index == 0:
            return max_element

        current_index: int = 0
        left_child_index: int = current_index * 2 + 1
        right_child_index: int = current_index * 2 + 2
        is_balanced = False
        while (
            not is_balanced
            and left_child_index < len(self.HeapArray)
            and right_child_index < len(self.HeapArray)
        ):
            max_value: int = max(
                self.HeapArray[current_index],
                (
                    self.HeapArray[left_child_index]
                    if self.HeapArray[left_child_index] is not None
                    else self.HeapArray[current_index]
                ),
                (
                    self.HeapArray[right_child_index]
                    if self.HeapArray[right_child_index] is not None
                    else self.HeapArray[current_index]
                ),
            )
            if max_value == self.HeapArray[current_index]:
                is_balanced = True
                continue
            if (
                self.HeapArray[left_child_index] is not None
                and max_value == self.HeapArray[left_child_index]
            ):
                max_value_index: int = left_child_index
            else:
                max_value_index = right_child_index

            self.HeapArray[current_index], self.HeapArray[max_value_index] = (
                self.HeapArray[max_value_index],
                self.HeapArray[current_index],
            )

            current_index = max_value_index
            left_child_index = current_index * 2 + 1
            right_child_index = current_index * 2 + 2

        return max_element

    def Add(self, key: int) -> bool:
        if self.HeapArray.count(None) == 0:
            return False
        last_empty_element_index: int = self.HeapArray.index(None)
        self.HeapArray[last_empty_element_index] = key

        current_index: int = last_empty_element_index
        parent_index: int = (current_index - 1) // 2
        is_balanced = False
        while not is_balanced and parent_index >= 0:
            if self.HeapArray[current_index] <= self.HeapArray[parent_index]:
                is_balanced = True
                continue

            self.HeapArray[current_index], self.HeapArray[parent_index] = (
                self.HeapArray[parent_index],
                self.HeapArray[current_index],
            )

            current_index = parent_index
            parent_index = (current_index - 1) // 2

        return True

    def is_valid(self) -> bool:
        return self._is_valid_subheap(0)

    def _is_valid_subheap(self, node_index: int) -> bool:
        if self.HeapArray[node_index] is None:
            return True
        left_child_index: int = node_index * 2 + 1
        right_child_index: int = node_index * 2 + 2
        if left_child_index >= len(self.HeapArray) or right_child_index >= len(
            self.HeapArray
        ):
            return True
        return (
            (
                self.HeapArray[left_child_index] is None
                or self.HeapArray[left_child_index] <= self.HeapArray[node_index]
            )
            and (
                self.HeapArray[right_child_index] is None
                or self.HeapArray[right_child_index] <= self.HeapArray[node_index]
            )
            and self._is_valid_subheap(left_child_index)
            and self._is_valid_subheap(right_child_index)
        )

    def find_max_in_range(self, from_value: int, to_value: int) -> int:
        return self._find_max_in_range_recursive(from_value, to_value, 0)

    def _find_max_in_range_recursive(
        self, from_value: int, to_value: int, node_index: int
    ) -> int:
        if self.HeapArray[node_index] is None:
            return -1
        if self.HeapArray[node_index] < from_value:
            return -1
        if (
            self.HeapArray[node_index] >= from_value
            and self.HeapArray[node_index] <= to_value
        ):
            return self.HeapArray[node_index]

        left_child_index: int = node_index * 2 + 1
        right_child_index: int = node_index * 2 + 2
        if left_child_index >= len(self.HeapArray) or right_child_index >= len(
            self.HeapArray
        ):
            return -1
        if (
            self.HeapArray[left_child_index] is None
            and self.HeapArray[right_child_index] is None
        ):
            return -1
        if self.HeapArray[left_child_index] is None:
            return self._find_max_in_range_recursive(
                from_value, to_value, right_child_index
            )
        if self.HeapArray[right_child_index] is None:
            return self._find_max_in_range_recursive(
                from_value, to_value, left_child_index
            )
        return max(
            self._find_max_in_range_recursive(from_value, to_value, left_child_index),
            self._find_max_in_range_recursive(from_value, to_value, right_child_index),
        )

    def add_level(self) -> None:
        new_depth: int = 0
        new_size: int = 0
        while new_size <= len(self.HeapArray):
            new_depth += 1
            new_size = 2 ** (new_depth + 1) - 1
        add_size_amount: int = new_size - len(self.HeapArray)
        self.HeapArray += [None] * add_size_amount

    def union_from_heap(self, heap) -> None:
        new_elment: int = heap.GetMax()
        while new_elment != -1:
            if not self.Add(new_elment):
                self.add_level()
                self.Add(new_elment)
            new_elment: int = heap.GetMax()
