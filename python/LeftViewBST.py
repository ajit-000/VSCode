from collections import deque


class Tree:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None


def leftview(root):
    res = []
    if root is None:
        return res
    que = deque([root])
    while que:
        for i in range(len(que)):
            x = que.popleft()
            if i == 0:
                res.append(x.data)
            if x.left:
                que.append(x.left)
            if x.right:
                que.append(x.right)
    return res


if __name__ == "__main__":
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.right.left = Tree(6)
    root.right.right = Tree(7)
    print(leftview(root))
