from typing import Optional


class SimpleTreeNode:

    def __init__(self, val: int, parent: Optional["SimpleTreeNode"]) -> None:
        self.NodeValue: int = val
        self.Parent: Optional[SimpleTreeNode] = parent
        self.Children: list[SimpleTreeNode] = []


class SimpleTree:

    def __init__(self, root: Optional[SimpleTreeNode]) -> None:
        self.Root: Optional[SimpleTreeNode] = root

    def AddChild(
        self, ParentNode: Optional[SimpleTreeNode], NewChild: SimpleTreeNode
    ) -> None:
        if ParentNode is None:
            if self.Root is not None:
                self.Root.Parent = NewChild
                NewChild.Children.append(self.Root)
                self.Root = NewChild
            self.Root = NewChild
            return None
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        return None

    def DeleteNode(self, NodeToDelete: SimpleTreeNode) -> None:
        assert NodeToDelete.Parent is not None
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None
        while NodeToDelete.Children != []:
            self.DeleteNode(NodeToDelete.Children[0])
        return None

    def GetAllNodes(self) -> list[SimpleTreeNode]:
        return self.GetAllNodesRecursive(self.Root)

    def GetAllNodesRecursive(
        self, node: Optional[SimpleTreeNode]
    ) -> list[SimpleTreeNode]:
        if node is None:
            return []
        nodes: list[SimpleTreeNode] = [node]
        for n in node.Children:
            nodes.extend(self.GetAllNodesRecursive(n))
        return nodes

    def FindNodesByValue(self, val: int) -> list[SimpleTreeNode]:
        return self._FindNodesByValueRecursive(self.Root, val)

    def _FindNodesByValueRecursive(
        self, node: Optional[SimpleTreeNode], val: int
    ) -> list[SimpleTreeNode]:
        if node is None:
            return []
        nodes: list[SimpleTreeNode] = []
        if node.NodeValue == val:
            nodes.append(node)
        for n in node.Children:
            nodes.extend(self._FindNodesByValueRecursive(n, val))
        return nodes

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode) -> None:
        assert OriginalNode.Parent is not None
        OriginalNode.Parent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent
        return None

    def Count(self) -> int:
        return len(self.GetAllNodesRecursive(self.Root))

    def LeafCount(self) -> int:
        return len(
            [
                node
                for node in self.GetAllNodesRecursive(self.Root)
                if node.Children == []
            ]
        )

    def EvenTrees(self) -> list[SimpleTreeNode]:
        if self.Root is None:
            return []
        return self.EvenTree_recursive(self.Root)

    def EvenTree_recursive(self, node: SimpleTreeNode) -> list[SimpleTreeNode]:
        edges_to_delete: list[SimpleTreeNode] = []
        for child in node.Children:
            if len(self.GetAllNodesRecursive(child)) % 2 == 0:
                edges_to_delete.extend([node])
                edges_to_delete.extend([child])
            edges_to_delete.extend(self.EvenTree_recursive(child))
        return edges_to_delete

    def balance_binary_even(self) -> None:
        nodes_sorted: list[SimpleTreeNode] = self.GetAllNodes()
        if len(nodes_sorted) == 0:
            return None
        nodes_sorted.sort(key=lambda node: node.NodeValue)
        for node in nodes_sorted:
            node.Parent = None
            node.Children = []
        self.AddChild(None, self._balance_binary_even_recursive(nodes_sorted))
        return None

    def _balance_binary_even_recursive(
        self, nodes_sorted: list[SimpleTreeNode]
    ) -> Optional[SimpleTreeNode]:
        if len(nodes_sorted) == 0:
            return None
        central_element_index: int = len(nodes_sorted) // 2
        left_side: list[SimpleTreeNode] = nodes_sorted[:central_element_index]
        right_side: list[SimpleTreeNode] = nodes_sorted[central_element_index + 1 :]
        left_child: Optional[SimpleTreeNode] = self._balance_binary_even_recursive(
            left_side
        )
        right_child: Optional[SimpleTreeNode] = self._balance_binary_even_recursive(
            right_side
        )
        if left_child is not None:
            self.AddChild(nodes_sorted[central_element_index], left_child)
        if right_child is not None:
            self.AddChild(nodes_sorted[central_element_index], right_child)
        return nodes_sorted[central_element_index]

    def count_even_subtrees(self) -> int:
        if self.Root is None:
            return 0
        even_subtrees_amount: int = 0
        for subtree_root, node_amount in self.get_nodes_amount_for_every_subtree(
            self.Root, {}
        ).items():
            if node_amount % 2 == 0 and node_amount != 0:
                even_subtrees_amount += 1
        return even_subtrees_amount

    def get_nodes_amount_for_every_subtree(
        self,
        subtree_root: SimpleTreeNode,
        subtrees_node_amount: dict[SimpleTreeNode, int],
    ) -> dict[SimpleTreeNode, int]:
        subtrees_node_amount[subtree_root] = 1
        for child in subtree_root.Children:
            subtrees_node_amount[
                subtree_root
            ] += self.get_nodes_amount_for_every_subtree(child, subtrees_node_amount)[
                child
            ]
        return subtrees_node_amount
