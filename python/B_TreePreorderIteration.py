class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def iteration(root):
    if root is None:
        return

    stk = []
    stk.append(root)
    while len(stk) > 0:
        nod = stk.pop()
        print(nod.data, end=",")
        if nod.right is not None:
            stk.append(nod.right)
        if nod.left is not None:
            stk.append(nod.left)


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(10)
    root.right = Node(6)
    root.left.left = Node(4)
    root.left.right = Node(8)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.left = Node(20)
    iteration(root)