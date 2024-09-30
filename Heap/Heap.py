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
                max_value_index: int = right_child_index

            self.HeapArray[current_index], self.HeapArray[max_value_index] = (
                self.HeapArray[max_value_index],
                self.HeapArray[current_index],
            )

            current_index = max_value_index
            left_child_index: int = current_index * 2 + 1
            right_child_index: int = current_index * 2 + 2

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
