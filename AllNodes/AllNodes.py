from typing import Any, Optional


class BSTNode:

    def __init__(self, key: Any, val: Any, parent) -> None:
        self.NodeKey: Any = key
        self.NodeValue: Any = val
        self.Parent: Optional[BSTNode] = parent
        self.LeftChild: Optional[BSTNode] = None
        self.RightChild: Optional[BSTNode] = None


class BSTFind:

    def __init__(self) -> None:
        self.Node: Optional[BSTNode] = None
        self.NodeHasKey: bool = False
        self.ToLeft: bool = False


class BST:

    def __init__(self, node: Optional[BSTNode]):
        self.Root: Optional[BSTNode] = node

    def FindNodeByKey(self, key: Any) -> BSTFind:
        return self.FindNodeByKeyRecursive(key, self.Root, BSTFind())

    def FindNodeByKeyRecursive(
        self, key: Any, node: Optional[BSTNode], result: BSTFind
    ) -> BSTFind:
        if node is None:
            return result
        result.Node = node
        if node.NodeKey == key:
            result.NodeHasKey = True
            return result
        if node.NodeKey > key:
            result.ToLeft = True
            return self.FindNodeByKeyRecursive(key, node.LeftChild, result)
        result.ToLeft = False
        return self.FindNodeByKeyRecursive(key, node.RightChild, result)

    def AddKeyValue(self, key: Any, val: Any) -> bool:
        place_for_node: BSTFind = self.FindNodeByKey(key)
        if place_for_node.Node is None:
            self.Root = BSTNode(key, val, None)
            return True
        if place_for_node.NodeHasKey:
            return False
        if place_for_node.ToLeft:
            place_for_node.Node.LeftChild = BSTNode(key, val, place_for_node.Node)
        else:
            place_for_node.Node.RightChild = BSTNode(key, val, place_for_node.Node)
        return True

    def FinMinMax(
        self, FromNode: Optional[BSTNode], FindMax: bool
    ) -> Optional[BSTNode]:
        if FromNode is None:
            return None
        if FindMax and FromNode.RightChild is None:
            return FromNode
        if FindMax and FromNode.RightChild is not None:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        if FromNode.LeftChild is None:
            return FromNode
        return self.FinMinMax(FromNode.LeftChild, FindMax)

    def DeleteNodeByKey(self, key: Any) -> bool:
        found: BSTFind = self.FindNodeByKey(key)
        if not found.NodeHasKey:
            return False

        assert isinstance(found.Node, BSTNode)
        found_node: BSTNode = found.Node

        is_node_has_left_child: bool = found_node.LeftChild is not None
        is_node_has_right_child: bool = found_node.RightChild is not None

        if not is_node_has_left_child and not is_node_has_right_child:

            if found_node is self.Root:
                self.Root = None
            else:
                assert isinstance(found_node.Parent, BSTNode)
                if found.ToLeft:
                    found_node.Parent.LeftChild = None
                else:
                    found_node.Parent.RightChild = None
                found_node.Parent = None

        elif is_node_has_left_child and is_node_has_right_child:

            successor_node: Optional[BSTNode] = self.FinMinMax(
                found_node.RightChild, False
            )
            assert isinstance(successor_node, BSTNode)
            self.DeleteNodeByKey(successor_node.NodeKey)

            if found_node is not self.Root:
                assert isinstance(found_node.Parent, BSTNode)
                found_node.Parent.RightChild = successor_node
            else:
                self.Root = successor_node

            successor_node.Parent = found_node.Parent
            successor_node.RightChild = found_node.RightChild
            successor_node.LeftChild = found_node.LeftChild
            if successor_node.RightChild is not None:
                successor_node.RightChild.Parent = successor_node
            if successor_node.LeftChild is not None:
                successor_node.LeftChild.Parent = successor_node
            found_node.Parent = None
            found_node.LeftChild = None
            found_node.RightChild = None

        else:
            if is_node_has_left_child:
                successor_node = found_node.LeftChild
            else:
                successor_node = found_node.RightChild
            assert isinstance(successor_node, BSTNode)
            if found_node is not self.Root:
                assert isinstance(found_node.Parent, BSTNode)
                if found.ToLeft:
                    found_node.Parent.LeftChild = successor_node
                else:
                    found_node.Parent.RightChild = successor_node
                successor_node.Parent = found_node.Parent
            else:
                self.Root = successor_node
                successor_node.Parent = None

            found_node.LeftChild = None
            found_node.RightChild = None
            found_node.Parent = None

        return True

    def Count(self) -> int:
        return self._Count_recursive(self.Root)

    def _Count_recursive(self, node: Optional[BSTNode]) -> int:
        if node is None:
            return 0
        return (
            1
            + self._Count_recursive(node.RightChild)
            + self._Count_recursive(node.LeftChild)
        )

    def WideAllNodes(self) -> tuple[BSTNode, ...]:
        return self._WideAllNodes_recursive([self.Root], ())

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

    def DeepAllNodes(self, order: int) -> tuple[BSTNode, ...]:
        return self._DeepAllNodes_recursive(order, self.Root)

    def _DeepAllNodes_recursive(
        self, order: int, from_node: Optional[BSTNode]
    ) -> tuple[BSTNode, ...]:
        if from_node is None:
            return ()
        # in-order
        if order == 0 and from_node is self.Root:
            return (
                self._DeepAllNodes_recursive(order, from_node.LeftChild)
                + (self.Root,)
                + self._DeepAllNodes_recursive(order, from_node.RightChild)
            )
        # post-order
        if order == 1 and from_node is self.Root:
            return (
                self._DeepAllNodes_recursive(order, from_node.LeftChild)
                + self._DeepAllNodes_recursive(order, from_node.RightChild)
                + (self.Root,)
            )
        # pre-order
        if order == 2 and from_node == self.Root:
            return (
                (self.Root,)
                + self._DeepAllNodes_recursive(order, from_node.LeftChild)
                + self._DeepAllNodes_recursive(order, from_node.RightChild)
            )

        return self._DeepAllNodes_recursive(
            order, from_node.LeftChild
        ) + self._DeepAllNodes_recursive(order, from_node.RightChild)
