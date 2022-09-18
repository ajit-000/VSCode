from collections import deque


class Tree:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None


def rev(root):
    res = []
    if root is None:
        return res
    que = deque([root])
    while que:
        for _ in range(len(que)):
            x = que.popleft()
            res.append(x.data)
            if x.left:
                que.appendleft(x.left)
            if x.right:
                que.appendleft(x.right)
    res.reverse()
    return res


if __name__ == "__main__":
    root = Tree(1)
    root.left = Tree(3)
    root.right = Tree(2)
    print(rev(root))
