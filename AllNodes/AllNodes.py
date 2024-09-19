from typing import Any


class BSTNode:

    def __init__(self, key: Any, val: Any, parent) -> None:
        self.NodeKey: Any = key
        self.NodeValue: Any = val
        self.Parent: BSTNode | None = parent
        self.LeftChild: BSTNode | None = None
        self.RightChild: BSTNode | None = None


class BSTFind:

    def __init__(self) -> None:
        self.Node: BSTNode | None = None
        self.NodeHasKey: bool = False
        self.ToLeft: bool = False


class BST:

    def __init__(self, node: BSTNode | None):
        self.Root: BSTNode | None = node

    def FindNodeByKey(self, key: Any) -> BSTFind:
        return self.FindNodeByKeyRecursive(key, self.Root, BSTFind())

    def FindNodeByKeyRecursive(
        self, key: Any, node: BSTNode | None, result: BSTFind
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

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
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

        assert isinstance(
            found.Node, BSTNode
        ), "If found None node, it must be procceed earlier."
        found_node: BSTNode = found.Node

        is_node_has_left_child: bool = found_node.LeftChild is not None
        is_node_has_right_child: bool = found_node.RightChild is not None

        if not is_node_has_left_child and not is_node_has_right_child:

            if found_node is self.Root:
                self.Root = None
            else:
                if found.ToLeft:
                    found_node.Parent.LeftChild = None
                else:
                    found_node.Parent.RightChild = None
                found_node.Parent = None

        elif is_node_has_left_child and is_node_has_right_child:

            successor_node: BSTNode = self.FinMinMax(found_node.RightChild, False)
            self.DeleteNodeByKey(successor_node.NodeKey)
            if found_node is not self.Root:
                found_node.Parent.RightChild = successor_node
            else:
                self.Root = successor_node
            successor_node.Parent = found_node.Parent
            successor_node.RightChild = found_node.RightChild
            successor_node.LeftChild = found_node.LeftChild
            successor_node.RightChild.Parent = successor_node
            successor_node.LeftChild.Parent = successor_node
            found_node.Parent = None
            found_node.LeftChild = None
            found_node.RightChild = None

        else:
            if is_node_has_left_child:
                successor_node: BSTNode = found_node.LeftChild
            else:
                successor_node: BSTNode = found_node.RightChild

            if found_node is not self.Root:
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
        return self.Count_recursive(self.Root)

    def Count_recursive(self, node: BSTNode) -> int:
        if node is None:
            return 0
        return (
            1
            + self.Count_recursive(node.RightChild)
            + self.Count_recursive(node.LeftChild)
        )

    def WideAllNodes(self) -> None:
        pass

    def DeepAllNodes(self) -> None:
        pass
