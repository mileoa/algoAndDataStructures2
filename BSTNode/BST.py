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
        node_to_delete_find = self.FindNodeByKey(key)
        if not node_to_delete_find.NodeHasKey:
            return False
        node_to_be_replaced_by = self.FinMinMax(
            node_to_delete_find.Node.RightChild, False
        )

        # удаляем узел по ключу
        return False  # если узел не найден

    def Count(self):
        return 0  # количество узлов в дереве
