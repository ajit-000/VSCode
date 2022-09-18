from collections import deque


class Node:
    def __init__(self, root):
        root = root
        left = right = None


queue = deque()


def burntree(root, targetNode):
    if root is None:
        return 0
    if root.data == targetNode:
        print(root.data)
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)
        return 1

    left = burntree(root.left, targetNode)
    if(left == 1):
        queueSize = len(queue)
        for i in range(queueSize):
            current = queue.popleft()
            print(current.data, end=" ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        if root.right is not None:
            queue.append(root.right)
        print(root.data)
        return 1

    right = burntree(root.right, targetNode)
    if(right == 1):
        queueSize = len(queue)
        for i in range(queueSize):
            current = queue.popleft()
            print(current.data, end=" ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        if root.left is not None:
            queue.append(root.left)
        print(root.data)
        return 1


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.right.left = Node(0)
    root.right.right = Node(8)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    target = int(input("Enter the target node: "))
    print(burntree(root, target))
