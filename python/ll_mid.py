# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LL:
#     def __init__(self):
#         self.head = None

#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data, end=" ")
#             temp = temp.next

#     def midll(self):
#         headnode = self.head
#         cnt = 0
#         while headnode.next != None:
#             cnt += 1
#         print(cnt)


# if __name__ == "__main__":
#     link = LL()
#     link.head = Node(1)
#     sec = Node(2)
#     th = Node(3)
#     link.head.next = sec
#     sec.next = th
#     link.printList()
#     link.midll()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def midll(self):
        headnode = self.head
        cnt = 0
        while headnode.next != None:
            cnt += 1
        print(cnt)

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == "__main__":
    link = LL()
    link.head = Node(input())
    sec = Node(input())
    th = Node(input())
    link.head.next = sec
    sec.next = th
    link.printList()
    link.midll()
