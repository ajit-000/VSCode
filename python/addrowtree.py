from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def bfs(root, depth, elem):
    if depth == 1:
        return Node(elem, left=root)
    que = deque()
    que.append(root)
    cnt = 1
    while depth-1 > cnt:
        cnt += 1
        st = []
        curlen = len(que)
        for _ in range(curlen):
            x = que.popleft()
            st.append(x)
            if x.left:
                que.append(x.left)
            if x.right:
                que.append(x.right)
    while que:
        x = que.popleft()
        temp = Node(elem)
        temp.left = x.left
        x.left = temp
        temp = Node(elem)
        temp.right = x.right
        x.right = temp
    return root


def traverse(root):
    if root is None:
        return None
    print(root.data, end=" ")
    traverse(root.left)
    traverse(root.right)


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(3)
    root.left.right = Node(1)
    root.right.left = Node(5)
    print("Add depth: ")
    depth = int(input())
    print("Add Elem: ")
    elem = int(input())
    bfs(root, depth, elem)
    traverse(root)
