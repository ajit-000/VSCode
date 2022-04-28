class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree():
    def __init__(self) -> None:
        self.root = None


if __name__ == "__main__":
    root = BinaryTree()
    root.left = Node(10)
    root.right = Node(6)
    root.left.left = Node(4)
    root.left.right = Node(8)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.left = Node(20)
