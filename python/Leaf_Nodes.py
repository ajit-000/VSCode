class Node:
    def __init__(self, root):
        self.root = root
        self.left = self.right = None


class LeafNode:
    def __init__(self):
        self.root = None

    def leaf(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return self.leaf(root.left)+self.leaf(root.right)


if __name__ == "__main__":
    A = LeafNode()
    A.root = Node(1)
    A.root.left = Node(2)
    A.root.right = Node(3)
    A.root.left.left = Node(4)
    A.root.left.right = Node(5)
    A.root.right.left = Node(6)
    A.root.right.right = Node(7)
    print(A.leaf(A.root))
