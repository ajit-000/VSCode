# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.left, self.right = None, None


# def matchseq(root, seq, index):
#     if root is None:
#         return False
#     if index >= len(seq) or root.data != seq[index]:
#         return False
#     if seq[index] == root.data and root.left is None and root.right is None:
#         return True
#     return matchseq(root.left, seq, index+1) or matchseq(root.right, seq, index+1)


# if __name__ == "__main__":
#     root = Tree(3)
#     root.left = Tree(7)
#     root.left.left = Tree(9)
#     root.right = Tree(1)
#     root.right.left = Tree(2)
#     root.right.right = Tree(5)
#     seq = list(map(int, input().split()))
#     index = 0
#     print(matchseq(root, seq, index))

i=1
d={3:1,2:4,5:8,0:1}
d[i*2]-=1
print(d[i*2])
# print(d[i*2])