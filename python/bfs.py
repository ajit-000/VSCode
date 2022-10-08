from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def bfs(root):
    que = deque([])
    que.append(root)
    res = []
    while len(que) != 0:
        st = []
        curlen = len(que)
        for _ in range(curlen):
            x = que.popleft()
            st.append(x.data)
            if x.left:
                que.append(x.left)
            if x.right:
                que.append(x.right)
        res.append(st)
    return res


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(10)
    root.right = Node(6)
    root.left.left = Node(4)
    root.left.right = Node(8)
    root.right.left = Node(12)
    root.right.right = Node(20)
    print(bfs(root))
