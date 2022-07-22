class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Num_Nodes:
    def __init__(self):
        self.root = None

    def NumNodes(self, root):
        if root is None:
            return 0
        return 1+self.NumNodes(root.left)+self.NumNodes(root.right)


if __name__ == "__main__":
    A = Num_Nodes()
    A.root = Node(1)
    A.root.left = Node(2)
    A.root.right = Node(3)
    A.root.left.left = Node(4)
    A.root.left.right = Node(5)
    A.root.right.left = Node(6)
    A.root.right.right = Node(7)
    print(A.NumNodes(A.root))
