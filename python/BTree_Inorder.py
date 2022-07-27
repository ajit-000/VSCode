class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def inOrder(root):
	current = root
	stack = [] 
	while True:
		if current is not None:
			stack.append(current)
			current = current.left

		elif(stack):
			current = stack.pop()
			print(current.data, end=" ")
			current = current.right

		else:
			break




if __name__ == "__main__":
    root = Node(5)
    root.left = Node(10)
    root.right = Node(6)
    root.left.left = Node(4)
    root.left.right = Node(8)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.left = Node(20)
    inOrder(root)