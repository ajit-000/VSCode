from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None


def level_ord_suc(root, key):
    if root.data == key:
        return
    que = deque([])
    que.append(root)
    while len(que) != 0:
        x = que.popleft()
        if x.left:
            que.append(x.left)
        if x.right:
            que.append(x.right)
        if x.data == key:
            res = que.popleft()
            return res.data


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    key = int(input("Enter predecessor : "))
    print(level_ord_suc(root, key))
