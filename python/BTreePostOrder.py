class Node:

    def __init__(self, x):

        self.data = x
        self.right = None
        self.left = None


def postOrderIterative(root):

    stack = []

    while(True):
        while(root != None):
            stack.append(root)
            stack.append(root)
            root = root.left

        if (len(stack) == 0):
            return

        root = stack.pop()

        if (len(stack) > 0 and stack[-1] == root):
            root = root.right
        else:
            print(root.data, end=" ")
            root = None


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    postOrderIterative(root)
