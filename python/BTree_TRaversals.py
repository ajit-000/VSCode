class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def PreOrder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def InOrder(self, root):
        if root is None:
            return
        self.InOrder(root.left)
        print(root.data,end=" ")
        self.InOrder(root.right)

    def PostOrder(self, root):
        if root is None:
            return
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.data,end=" ")


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print("PreOrder Traversal : ", end="")
    tree.PreOrder(tree.root)
    print()
    print("InOrder Traversal : ", end="")
    tree.InOrder(tree.root)
    print()
    print("PostOrder Traversal : ", end="")
    tree.PostOrder(tree.root)
