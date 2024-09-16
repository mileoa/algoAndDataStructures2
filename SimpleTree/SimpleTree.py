class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
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

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete is None:
            return None
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None
        while NodeToDelete.Children != []:
            self.DeleteNode(NodeToDelete.Children[0])
        return None

    def GetAllNodes(self):
        return self.GetAllNodesRecursive(self.Root)

    def GetAllNodesRecursive(self, node):
        if node is None:
            return []
        nodes = [node]
        for n in node.Children:
            nodes.extend(self.GetAllNodesRecursive(n))
        return nodes

    def FindNodesByValue(self, val):
        return self.FindNodesByValueRecursive(self.Root, val)

    def FindNodesByValueRecursive(self, node, val):
        if node is None:
            return []
        nodes = []
        if node.NodeValue == val:
            nodes.append(node)
        for n in node.Children:
            nodes.extend(self.FindNodesByValueRecursive(n, val))
        return nodes

    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent
        return None

    def Count(self):
        return len(self.GetAllNodesRecursive(self.Root))

    def LeafCount(self):
        return len(
            [
                node
                for node in self.GetAllNodesRecursive(self.Root)
                if node.Children == []
            ]
        )



