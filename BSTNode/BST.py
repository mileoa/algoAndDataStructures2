class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        return self.FindNodeByKeyRecursive(key, self.Root, BSTFind())

    def FindNodeByKeyRecursive(self, key, node, result):
        if node is None:
            return result
        result.Node = node
        if node.NodeKey == key:
            result.NodeHasKey = True
            return result
        if node.NodeKey > key:
            result.ToLeft = True
            return self.FindNodeByKeyRecursive(key, node.LeftChild, result)
        if node.NodeKey < key:
            result.ToLeft = False
            return self.FindNodeByKeyRecursive(key, node.RightChild, result)

    def AddKeyValue(self, key, val):
        place_for_node = self.FindNodeByKey(key)
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

    def FinMinMax(self, FromNode, FindMax):
        if FromNode is None:
            return None
        if FindMax and FromNode.RightChild is None:
            return FromNode
        if FindMax and FromNode.RightChild is not None:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        if FromNode.LeftChild is None:
            return FromNode
        return self.FinMinMax(FromNode.LeftChild, FindMax)

    def DeleteNodeByKey(self, key):
        found = self.FindNodeByKey(key)
        if not found.NodeHasKey:
            return False
        found_node = found.Node

        is_node_has_left_child = found_node.LeftChild is not None
        is_node_has_right_child = found_node.RightChild is not None

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

            successor_node = self.FinMinMax(found_node.RightChild, False)
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
                successor_node = found_node.LeftChild
            else:
                successor_node = found_node.RightChild

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

    def Count(self):
        return 0  # количество узлов в дереве
