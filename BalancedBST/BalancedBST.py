from typing import Optional


class BSTNode:

    def __init__(self, key: int, parent):
        self.NodeKey: int = key
        self.Parent: Optional[BSTNode] = parent
        self.LeftChild: Optional[BSTNode] = None
        self.RightChild: Optional[BSTNode] = None
        self.Level: int = 0


class BalancedBST:

    def __init__(self) -> None:
        self.Root: Optional[BSTNode] = None

    def GenerateTree(self, a: list[int]):
        if len(a) == 0:
            return None
        a_sorted: list[int] = a[:]
        a_sorted.sort()
        central_index: int = len(a_sorted) // 2
        self.Root = BSTNode(a_sorted[central_index], None)
        self.Root.LeftChild = self._generate_subtree(
            self.Root, a_sorted[:central_index]
        )
        self.Root.RightChild = self._generate_subtree(
            self.Root, a_sorted[central_index + 1 :]
        )

    def _generate_subtree(
        self, parent: BSTNode, a_side: list[int]
    ) -> Optional[BSTNode]:
        if len(a_side) == 0:
            return None
        central_index: int = len(a_side) // 2
        node = BSTNode(a_side[central_index], parent)
        node.Level = parent.Level + 1
        node.LeftChild = self._generate_subtree(node, a_side[:central_index])
        node.RightChild = self._generate_subtree(node, a_side[central_index + 1 :])
        return node

    def is_valid_tree(self) -> bool:
        return self.is_valid_subrtree(self.Root)

    def is_valid_subrtree(self, root_node: Optional[BSTNode]) -> bool:
        if root_node is None:
            return True
        return (
            (
                root_node.LeftChild is None
                or root_node.LeftChild.NodeKey < root_node.NodeKey
            )
            and (
                root_node.RightChild is None
                or root_node.RightChild.NodeKey > root_node.NodeKey
            )
            and self.is_valid_subrtree(root_node.LeftChild)
            and self.is_valid_subrtree(root_node.RightChild)
        )

    def IsBalanced(self, root_node: Optional[BSTNode]) -> bool:
        if root_node is None:
            return True
        return (
            abs(
                max(self.max_depth(root_node.LeftChild), root_node.Level)
                - max(self.max_depth(root_node.RightChild), root_node.Level)
            )
            <= 1
            and self.IsBalanced(root_node.LeftChild)
            and self.IsBalanced(root_node.RightChild)
        )

    def max_depth(self, node: Optional[BSTNode]) -> int:
        child_nodes_depth: list[int] = [
            node.Level for node in self.crawl_wide_nodes(node)
        ]
        if len(child_nodes_depth) == 0:
            return 0
        return max(child_nodes_depth)

    def crawl_wide_nodes(self, node: Optional[BSTNode]) -> tuple[BSTNode, ...]:
        return self._WideAllNodes_recursive([node], ())

    def _WideAllNodes_recursive(
        self, current_nodes: list[Optional[BSTNode]], result: tuple[BSTNode, ...]
    ) -> tuple[BSTNode, ...]:
        if current_nodes.count(None) == len(current_nodes):
            return result
        childs_of_current_nodes: list[Optional[BSTNode]] = []
        for node in current_nodes:
            if node is None:
                continue
            result += (node,)
            childs_of_current_nodes.append(node.LeftChild)
            childs_of_current_nodes.append(node.RightChild)
        return self._WideAllNodes_recursive(childs_of_current_nodes, result)
