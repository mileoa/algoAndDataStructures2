from typing import Optional


def GenerateBBSTArray(a: list[int]) -> list[Optional[int]]:
    a_sorted: list[int] = a[:]
    a_sorted.sort()
    return GenerateBBSTArray_recursive(a_sorted, 0, [None] * len(a))


def GenerateBBSTArray_recursive(
    a_sorted: list[int],
    BST_node_index: int,
    BST: list[Optional[int]],
) -> list[Optional[int]]:
    if BST_node_index > len(BST) - 1:
        return []
    central_element_index: int = len(a_sorted) // 2
    BST[BST_node_index] = a_sorted[central_element_index]
    left_side: list[int] = a_sorted[:central_element_index]
    right_side: list[int] = a_sorted[central_element_index + 1 :]
    GenerateBBSTArray_recursive(
        left_side,
        BST_node_index * 2 + 1,
        BST,
    )
    GenerateBBSTArray_recursive(
        right_side,
        BST_node_index * 2 + 2,
        BST,
    )
    return BST
