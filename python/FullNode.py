class Node:
    def __init__(self, root):
        self.root = root
        self.left = self.right = None


class FullNode:
    def __init__(self):
        self.root = None

    def full(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        return self.full(root.left)+self.full(root.right)+(1 if root.left != None and root.right != None else 0)


if __name__ == "__main__":
    A = FullNode()
    A.root = Node(1)
    A.root.left = Node(2)
    A.root.right = Node(3)
    A.root.left.left = Node(4)
    A.root.left.right = Node(5)
    A.root.right.left = Node(6)
    A.root.right.right = Node(7)
    print(A.full(A.root))
